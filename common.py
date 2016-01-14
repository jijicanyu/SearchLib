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
import re
import time
import logging

from selenium import webdriver

logging.getLogger("selenium").setLevel(logging.WARNING)

def remove_control_characters(html):
    def str_to_int(s, default, base=10):
        if int(s, base) < 0x10000:
            return unichr(int(s, base))
        return default
    html = re.sub(ur"&#(\d+);?", lambda c: str_to_int(c.group(1), c.group(0)), html)
    html = re.sub(ur"&#[xX]([0-9a-fA-F]+);?", lambda c: str_to_int(c.group(1), c.group(0), base=16), html)
    html = re.sub(ur"[\x00-\x08\x0b\x0e-\x1f\x7f]", "", html)
    return html

def getpagewithchrome(url,sleep=3):
    dr = webdriver.Chrome(executable_path=r"/Users/sunrain/code/chromedriver")
    dr.get(url)
    time.sleep(sleep)
    source = dr.page_source
    dr.quit()
    return source

def getpagewithjs(url,sleep=2):
    dr = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")
    dr.get(url)
    time.sleep(sleep)
    source = dr.page_source
    dr.quit()
    return source


if __name__ == "__main__":
    print getpagewithjs("http://www.zoomeye.org/search?q=service:http&p=2&t=host")