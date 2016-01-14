#!/usr/bin/python
# coding:utf-8
__author__ = 'Sunrain'
__version__ = 1.0

#                            _ooOoo_  
#                           o8888888o  
#                           88" . "88  
#                           (| -_- |)  
#                            O\ = /O  
#                        ____/`---'\____  
#                      .   ' \\| |// `.  
#                       / \\||| : |||// \  
#                     / _||||| -:- |||||- \  
#                       | | \\\ - /// | |  
#                     | \_| ''\---/'' | |  
#                      \ .-\__ `-` ___/-. /  
#                   ___`. .' /--.--\ `. . __  
#                ."" '< `.___\_<|>_/___.' >'"".  
#               | | : `- \`.;`\ _ /`;.`/ - ` : | |  
#                 \ \ `-. \_ __\ /__ _/ .-` / /  
#         ======`-.____`-.___\_____/___.-`____.-'======  
#                            `=---='  
# 
#        .............................................  
#                  佛祖保佑             永无BUG 
#          佛曰:  
#                  写字楼里写字间，写字间里程序员；  
#                  程序人员写程序，又拿程序换酒钱。  
#                  酒醒只在网上坐，酒醉还来网下眠；  
#                  酒醉酒醒日复日，网上网下年复年。  
#                  但愿老死电脑间，不愿鞠躬老板前；  
#                  奔驰宝马贵者趣，公交自行程序员。  
#                  别人笑我忒疯癫，我笑自己命太贱；  
#                  不见满街漂亮妹，哪个归得程序员？
import ConfigParser
from urllib import quote
import urlparse
import time
import os
import importlib
import sys

from lxml import etree
import requests

from common import remove_control_characters
import json

class Search(object):
    def __init__(self,keyword,searchPages=30):
        self.keyword = keyword
        self.next = ""
        self.searchPages = searchPages
        self.finalUrls = []
        self.sleepingTimeBetweenEachSearch = 1
        self.modulePath = os.path.dirname(__file__)
        self.config_file = os.path.join(self.modulePath,"search.cfg")
        self.supportedSearchEngines = []
        self.searchEngineName = []
        sys.path.append(self.modulePath)
        parser = ConfigParser.ConfigParser()
        parser.read(self.config_file)
        allSectionsInConfigFile = parser.sections()
        for section in allSectionsInConfigFile:
            engine = dict()
            engine["baseurl"] = parser.get(section,"baseurl")
            engine["urlinpage"] = parser.get(section,"urlinpage")
            engine["nextpage"] = parser.get(section,"nextpage")
            engine["count"] = parser.get(section,"count")
            engine["callback"] = parser.get(section,"callback")
            engine["timeout"] = int(parser.get(section,"timeout"))
            engine["name"] = parser.get(section,"name")
            self.supportedSearchEngines.append(engine)
            self.searchEngineName.append(engine["name"].lower())


    def __getUrlsInPage(self, url, wantedXpath, nextUrlXpath):
        User_Agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        header = {}
        header["User-Agent"] = User_Agent

        try:
            rq = requests.get(url, headers=header,allow_redirects=True,verify=False)
        except:
            return None,None

        html = rq.text

        html = remove_control_characters(html)
        page = etree.HTML(html)
        result = page.xpath(wantedXpath)
        try:
            nextpage = page.xpath(nextUrlXpath)[0]
        except Exception:
            nextpage = None

        return result, nextpage

    def __importFuncFromModule(self,moduleName, funcName):
        importedModule = importlib.import_module(moduleName)
        if hasattr(importedModule,funcName):
            return getattr(importedModule,funcName)
        return getattr(self,funcName) if hasattr(self,funcName) else None

    def __getGetUrlFunction(self,engine):
        if engine["callback"] != "None":
            moduleName = engine["callback"].split('.')[0]
            geturlinpage = self.__importFuncFromModule(moduleName,"__getUrlsInPage")
        else:
            geturlinpage = self.__getUrlsInPage

        return geturlinpage if geturlinpage else self.__getUrlsInPage

    def __handleCallback(self,engine,urlsInPage):
        if engine["callback"] != "None":
            moduleName = engine["callback"].split('.')[0]
            callback = self.__importFuncFromModule(moduleName,"callback")

            if callback:
                real_one = []
                for temp_url in urlsInPage:
                    temp_url = callback(temp_url)
                    if temp_url == None:
                        continue
                    real_one.append(temp_url)
                urlsInPage = real_one

        return urlsInPage

    def __log(self,message):
        print message


    def searching(self,usingEngineNames=["bing","baidu","google2","sogou","360"]):


        for currentEngine in self.supportedSearchEngines:

            if usingEngineNames != None and currentEngine["name"].lower() not in usingEngineNames:
                continue

            self.__log("[*] Searching in Engine {}".format(currentEngine['name']))

            currentUrl = currentEngine["baseurl"]+quote(self.keyword)
            page = 0

            while page != self.searchPages:

                    self.__log("[*] Current url is {}".format(currentUrl))
                    geturlinpage = self.__getGetUrlFunction(currentEngine)

                    urlsInPage, nextUrl = geturlinpage(currentUrl,currentEngine["urlinpage"],currentEngine["nextpage"])

                    if urlsInPage == None or len(urlsInPage)==0:
                        break
                    urlsInPage = self.__handleCallback(currentEngine,urlsInPage)
                    nextUrl =  urlparse.urljoin(currentEngine["baseurl"],nextUrl)
                    page += 1

                    if currentEngine["timeout"] != 0:
                        sleepingTimeBetweenEachSearch = max(self.sleepingTimeBetweenEachSearch,currentEngine["timeout"])
                        time.sleep(sleepingTimeBetweenEachSearch)

                    self.__log("[*] Got urls :\n{}".format('\n'.join(urlsInPage)))

                    self.finalUrls.extend(urlsInPage)

                    if nextUrl == currentUrl or nextUrl == None:
                        break
                    currentUrl = nextUrl

        self.finalUrls = list(set(self.finalUrls))

        return self.finalUrls

if __name__ == "__main__":

    a = Search("mongo",5)
    b = a.searching(usingEngineNames=["zoomeye"])


