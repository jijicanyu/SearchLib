# search
###简介
一个用于爬行所有搜索引擎的库
搜索效果图：
![效果图1](http://7xktnl.com1.z0.glb.clouddn.com/Snip20160114_1.png)
可以搜索zoomeye结果，10页内，需安装selenium库，并设置zoomeye_callback.py中的chromedriver地址：
![效果图2](http://7xktnl.com1.z0.glb.clouddn.com/Snip20160114_2.png)

###优点
1. 支持面广，可拓展
能支持几乎所有搜索引擎
2. 防屏蔽
不使用api,可自定义每种搜索引擎延迟时间，单线程
3. 易用
已经写好了几个常用搜索引擎配置，可直接使用

###如何安装
    
    git clone https://github.com/tdifg/SearchLib.git
    cd SearchLib
    pip install -r requirements.txt


###如何使用

详见demo
如欲加入新搜索引擎支持，可以参照search.cfg其他设置，并酌情增加callback

###TODO
1. 重构
2. 修改page倒序显示的小问题       √
3. 修复导入时的依赖问题           √
4. 写两个Demo                  √
5. 发布到pypi                  


