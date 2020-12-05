# Python爬虫学习笔记

## 第一章：爬虫基础知识

### 第一节：爬虫初始认识

> <font color=red>爬虫在适用场景中的分类</font>

- 通用爬虫：抓取系统重要组成部分

 		--抓取的是一整张页面的数据

- 聚焦爬虫：是建立在通用爬虫的基础之上

​		--抓取的是页面中特定的局部内容

- 增量式爬虫：检测网站中数据更新的情况

​		--只会抓取网站中最新更新出来的数据

> <font color=red>爬虫之中的矛盾</font>

- 反爬机制

​		--门户网站，可以通过制定相应的策略或者技术手段，防止爬虫程序进行网站数据爬取。

- 反反爬策略

​		--爬虫程序也可以通过制定相关的策略或者技术手段，破解门户网站中具备的反爬机制，从而可以获取门户网站的数据



> <font color=red>君子协议robots.txt协议</font>

​	君子协议，规定了网站中哪些数据可以被爬虫爬取，哪些数据不可以，但是并没有强制作用，只在于人是否遵守。

​	例如可以访问：www.taobao.com/robots.txt文件进行查看

![image-20201205172523033](note.assets\image-20201205172523033.png)



### 第二节：HTTP与HTTPS协议

> <font color=red>HTTP协议</font>

- 概念：就是服务器和客户端进行数据交互的一种形式
- 常用请求头信息

​		--User-Agent：请求载体的身份标识（浏览器或其他程序访问）

​		--Connection：请求完毕后，是断开连接还是保持连接

![image-20201205173121203](note.assets\image-20201205173121203.png)

- 常用响应头信息

​		--Content-Type：服务器相应回客户端的数据类型

》HTTPS协议

- 概念：安全的超文本传输协议（连接加密、传输加密）
- 加密方式

​		--对称秘钥加密

​		--非对称秘钥加密

​		--证书秘钥加密



## 第二章：Python—Request模块



### 第一节：requests模块认识

​	requests模块：python中原生的一款基于网络请求的模块，功能强大，简单便捷，效率搞笑

​	作用：模拟浏览器发请求

> <font color=red>如何使用requests模块（requests模块编码流程）</font>

- 指定URL
- 发起请求
- 获取响应数据
- 持久化存储

> <font color=red>requests模块安装</font>

​	pip install requests

![image-20201205173326011](note.assets\image-20201205173326011.png)



> <font color=red>实战编码</font>

- 需求：爬取搜狗首页的页面数据

​		--代码：[requests_01.py](https://github.com/augus-xiaochen/python_item/blob/main/requests_item/requests_01.py)

![image-20201205175651308](note.assets\image-20201205175651308.png)

### 第二节：requests模块巩固案例实践

> <font color=red>实战巩固</font>

- 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）

​		--代码：[requests_02.py](https://github.com/augus-xiaochen/python_item/blob/main/requests_item/requests_02.py)

![image-20201205175341256.png](note.assets\image-20201205175341256.png)

- 破解百度翻译
- 爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详细数据
- 爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点餐厅数量
- 爬取国家要付监督管理总局中基于中哈UR恩民共和国化妆品生产许可证相关数据



