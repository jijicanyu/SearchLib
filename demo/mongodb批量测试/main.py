#!/usr/bin/python
# coding:utf-8
__author__ = 'Joker'
__version__ = 1.0
'''
子模块导入后工作目录是主模块目录，然后就会出错
'''
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
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
from search.libsearch import Search


def printdoc(ip="69.164.211.62"):
    con = MongoClient(host=ip)
    #con = Connection(ip,27017)
    systemdb = ["admin","local","test"]
    index = "system.indexes"

    try:
        dbs = con.database_names()
    except:
        return
    print '-'*8
    print ip
    for db in dbs:
        if db in systemdb:
            continue

        print db
        '''
        db = con[db]
        print '-' * 20
        collections = db.collection_names()
        for collection in collections:
            if collection == index:
                continue
            print '-' * 20
            print "\tCollection:", collection
            collection = db[collection]
            print '-' * 20
            print "\tCount:",collection.count()
            i = 3
            for item in collection.find():
                print "\t",item
                i -= 1
                if i == 0:
                    break
        '''
    print '-'*8
    con.close()


s = Search("port:27017",searchPages=-1)
a = s.searching(usingEngineNames=["zoomeye"])


for ip in a:
    try:
        printdoc(ip)
    except ConnectionFailure,OperationFailure:
        continue
