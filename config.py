# -*- coding: utf-8 -*-

# 数据库配置
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = 'fIsE5OSU'
DB_NAME = 'pools'
TABLE_NAME = 'proxys'

# 验证代理配置
VALIDATOR_URL = 'https://httpbin.org/'

# 定时任务配置
GRAB_TIMES = 60  # 代理抓取间隔（分钟）
CHECK_TIMES = 10  # 验证代理间隔（分钟）
RE_CHECK_TIMES = 30  # 重新验证代理间隔（分钟）

# 爬虫列表
SPIDERS = ['xici', 'data5u', 'kuaidaili']

# Api服务配置
SERVER_HOST = 'localhost'
SERVER_PORT = '5000'
