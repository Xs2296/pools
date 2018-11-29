# -*- coding: utf-8 -*-
import logging
import datetime
import config
import subprocess
import time
from apscheduler.schedulers.background import BackgroundScheduler
from pools.items import Pools
from utils import utils

logger = logging.getLogger(__file__)


# 抓取代理
def grab_task():
    try:
        logger.info('Run grab job')
        for spider in config.SPIDERS:
            subprocess.Popen("scrapy crawl " + spider, shell=True)
        logger.info('Grab job finished')
    except Exception as e:
        logger.error('Grab job failed \r\nError: %s' % str(e) + '\r\n')


# 验证新代理
def verify_task():
    try:
        logger.info('Run verify job')
        proxys = Pools.select().where(Pools.status == 0)
        for p in proxys:
            resp = utils.verifyProxy(p.host, p.port)
            if resp:
                query = Pools.update(status=1, check_time=datetime.datetime.now()).where(Pools.id == p.id)
                query.execute()
        logger.info('Verify job finished')
    except Exception as e:
        logger.error('Verify job failed \r\nError: %s' % str(e) + '\r\n')


# 二次验证
def re_verify():
    try:
        logger.info('Run verify job')
        # 上次验证时间
        last_time = datetime.datetime.fromtimestamp(int(time.time() - config.CHECK_TIMES * 60))
        proxys = Pools.select().where(Pools.status == 1, Pools.check_time < last_time)
        for p in proxys:
            resp = utils.verifyProxy(p.host, p.port)
            if resp:
                query = Pools.update(status=1, check_time=datetime.datetime.now()).where(Pools.id == p.id)
            else:
                query = Pools.update(status=0, check_time=datetime.datetime.now()).where(Pools.id == p.id)
            query.execute()
        logger.info('Verify job finished')
    except Exception as e:
        logger.error('Verify job failed \r\nError: %s' % str(e) + '\r\n')


# 后台执行任务
def start_background_scheduler():
    logger.info('Run scheduler')
    scheduler = BackgroundScheduler()
    scheduler.add_job(grab_task, 'interval', minutes=config.GRAB_TIMES)
    scheduler.add_job(verify_task, 'interval', minutes=config.CHECK_TIMES)
    scheduler.add_job(re_verify, 'interval', minutes=config.RE_CHECK_TIMES)
    scheduler.start()
    logger.info('Scheduler started')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_background_scheduler()
