#! /usr/bin/env python3
from aiohttp import web
import aiohttp_jinja2
import jinja2
import argparse
import sys
sys.path.extend(['../../livecode'])
from livecode import routes
from livecode.utils import load_config
from livecode.db import attach_db
from livecode.middlewares import check_me

# 运行参数
parser = argparse.ArgumentParser(description="start live code service")
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', default=8081)
args = parser.parse_args()

# 加载配置文件
configs = load_config('./configs/base.yaml')

# 初始化服务器
app = web.Application(middlewares=[check_me])


app['config'] = configs

# 添加路由
app.add_routes(routes.get_urls())
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app['static_root_url'] = '/static'
app.router.add_static('/static/', 'static/')

# 初始化必要的资源
app.on_startup.append(attach_db)


web.run_app(app, host=args.host, port=args.port)
