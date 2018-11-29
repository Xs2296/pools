# -*- coding: utf-8 -*-
import logging
import config
import random
import json
from flask import Flask
from pools.items import Pools

logger = logging.getLogger(__file__)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/one', methods=['GET'])
def getOne():
    proxys = Pools.select().where(Pools.status == 1)
    proxy = random.choice(proxys)
    return json.dumps({'http': proxy.http, 'host': proxy.host, 'port': proxy.port})


@app.route('/all', methods=['GET'])
def getAll():
    proxys = Pools.select().where(Pools.status == 1).order_by(Pools.check_time).limit(100).distinct()
    res_list = []
    for k, p in enumerate(proxys):
        keys = ['http', 'host', 'port']
        datas = [p.http, p.host, p.port]
        res_list.append(dict(zip(keys, list(datas))))
    return json.dumps(res_list)


def start_server():
    logger.info('start web server')
    app.debug = False
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT)


if __name__ == '__main__':
    start_server()
