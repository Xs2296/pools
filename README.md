# pools

自建免费代理IP池

## 系统功能

- 自动抓取免费代理IP（西刺代理、快代理、data5u）
- 定期验证代理IP（周期性检查）
- 提供Api接口获取可用IP


## 项目源码结构
- /logs 日志存储文件夹
- /pools 爬虫程序
- /schedule 定时任务调度器
- /web Api接口
- config.py 配置文件
- scrapy.cfg scrapy配置文件
- start.py 启动文件
- utils.py 工具类


## 部署运行

- 安装依赖
- Python3
- APScheduler（任务调度器）
- Flask（web框架）
- Scrapy（爬虫程序）
- PyMySQL（数据库连接）
- Peewee（Orm）

```
```
- 导入数据库文件 pools.sql
- 修改配置文件 config.py
- 运行 start.py
```
python start.py
```


## HTTP接口

### 1. 获取单条数据

##### 基本信息

URL|http://pools.xscode.cn/one
:---|:---
HTTP请求方式|GET
方法返回|JSON

##### JSON返回示例

```
{
	"code": 200,
	"msg": "success",
	"datas": {
		"http": "http",
		"host": "61.183.233.6",
		"port": "54896"
	}
}
```

### 2. 获取多条数据

##### 基本信息

URL|http://pools.xscode.cn/all
:---|:---
HTTP请求方式|GET
方法返回|JSON

##### JSON返回示例

```
{
    "code": 200,
    "msg": "success",
    "datas": [
        {
            "http": "http",
            "host": "61.135.217.7",
            "port": "80"
        },
        {
            "http": "https",
            "host": "124.243.226.18",
            "port": "8888"
        },
        {
            "http": "https",
            "host": "118.190.94.224",
            "port": "9001"
        },
        {
            "http": "https",
            "host": "121.33.220.158",
            "port": "8437"
        },
        {
            "http": "http",
            "host": "58.53.128.83",
            "port": "3128"
        },
        {
            "http": "http",
            "host": "117.191.11.103",
            "port": "8458"
        },
        {
            "http": "https",
            "host": "101.236.55.145",
            "port": "8866"
        },
        {
            "http": "http",
            "host": "117.191.11.77",
            "port": "8243"
        },
        {
            "http": "https",
            "host": "61.160.247.63",
            "port": "808"
        },
        {
            "http": "http",
            "host": "101.248.64.68",
            "port": "8422"
        }
    ]
}
```
