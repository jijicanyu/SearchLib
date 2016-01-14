#!/usr/bin/python
# coding:utf-8
#author:sunrain
#       tdifg.com
#Create on 16/1/14

from libsearch import Search


if __name__ == "__main__":
    a = Search("redis",searchPages=3)
    b = a.searching(usingEngineNames=["zoomeye"])