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

from common import getpagewithchrome,remove_control_characters
from lxml import etree

def __getUrlsInPage(url,url_xpath,next_xpath):
    page = getpagewithchrome(url)
    page = remove_control_characters(page)

    html = etree.HTML(page)

    # try:
    result = html.xpath(url_xpath)

    try:
        nextpage = html.xpath(next_xpath)[0]
    except Exception:
        nextpage = None
        #print page

    #print "Next:",nextpage
    r = []
    for temp in result:
        if 'ip:' in temp:
            temp = temp.split('ip:')[-1]
            r.append(temp)
    result = r

    return result, nextpage