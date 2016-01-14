#!/usr/bin/python
# coding:utf-8
__author__ = 'Joker'
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
import requests
from lxml import etree
from common import remove_control_characters
import urlparse

def __getUrlsInPage(url,url_xpath,next_xpath):
    User_Agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    header = {}
    header["User-Agent"] = User_Agent

    rq = requests.get(url, headers=header, allow_redirects=True, verify=False)
    page = rq.text

    page = remove_control_characters(page)

    html = etree.HTML(page)
    # try:
    result = html.xpath(url_xpath)
    try:
        q = urlparse.urlparse(url).query
        q = q.split('&')
        if len(q) == 1:
            nextpage = url + "&p=2"
        else:
            nextpage = int(q[1].split('=')[1]) + 1
            nextpage = url.split('&')[0] + "&p=" + str(nextpage)
    except Exception:
        nextpage = None
        #print page

    #print "Next:",nextpage
    return result, nextpage