### requirements.txt

-------

* flask是核心包
* flask-swagger + flask-swagger-ui 是用来做Swagger UI的，flask-bootstrap 用来乱糊 HTML页面的
* SQLAlchemy + pymysql + 一个是数据库ORM框架，一个是数据库驱动
* pydantic 用来配合SQLAlchemy完成Model数据转换，解决一些奇怪的序列化反序列化问题
* requests 用来对接外部HTTP接口或者写爬虫脚本
* loguru 简易日志框架，from loguru import logger 就完事了
* gunicorn 多进程部署

## introduce
* cli带命令行启动服务器，可灵活配置host， port
* BaseResful类，继承后实现post，put，get，delete，带swagger带测试用例
* loguru config中配置,支持可变级别，自定义日志
* 中台只配置服务，不做具体路由分发，由router_view配置视图，router_rest配置接口
* 

--------------
基于flask的快速部署脚手架，具体功能如下（更新中）

1. sql连接模块，
2. swagger接口识别模块
3. logger日志模块
1. flask_restplus进行restful接口开发


## v0.01 2022年3月8日

--------------------
需要实现内容：
1. 

## todo 
* 基础架构的编写
* click使用命令行创建用户，开启服务
* 自定义注解
