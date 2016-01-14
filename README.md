# search
###简介
一个用于爬行所有搜索引擎的库

![效果图1](http://7xktnl.com1.z0.glb.clouddn.com/zoomeeye抓取.png)
![效果图2](http://7xktnl.com1.z0.glb.clouddn.com/百度搜索结果.png)

###优点
1. 支持面广，可拓展
能支持几乎所有搜索引擎
2. 防屏蔽
不使用api,可自定义每种搜索引擎延迟时间，单线程
3. 易用
已经写好了几个常用搜索引擎配置，可直接使用

###如何安装
    
    pip install SearchLib


###如何使用
修改search.cfg文件6行和7行的路径到你自己的驱动路径（如果不修改，无法查询进行了js跳转的搜索引擎）
导入本库中的Search类，指定查询字符串，查询页数，搜索引擎名称
详见demo

###TODO
1. 重构
2. 修改page倒序显示的小问题       √
3. 修复导入时的依赖问题           √
4. 写两个Demo                  √
5. 发布到pypi                  √
