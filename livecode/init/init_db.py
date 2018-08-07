"""初始化数据库
"""
import sqlite3
import logging
from livecode.utils import load_config

configs = load_config('../configs/base.yaml')


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

conn = sqlite3.connect('../live_code.db')

cursor = conn.cursor()

logging.info("正在初始化数据库...")

# 创建用户表
cursor.execute('CREATE TABLE users (id integer primary key AUTOINCREMENT, phone varchar(20), password varchar(40))')
cursor.execute("CREATE INDEX phone ON users (phone)")
# 插入默认的管理员账户
cursor.execute("INSERT into users (phone, password) VALUES (?, ?)", [configs['default_account']['phone'], configs['default_account']['password']])

# 创建用户链接码表
cursor.execute('CREATE TABLE link_code (id integer primary key AUTOINCREMENT, phone varchar(20), link_index integer, link_title varchar(64), scan_num integer)')
cursor.execute("CREATE INDEX phone_index ON link_code (phone, link_index)")

# 创建用户二维码表
cursor.execute('CREATE TABLE qr_code (id integer primary key AUTOINCREMENT, phone varchar(20), img_src varchar(100))')


logging.info("初始化数据表完成。")

cursor.close()
conn.commit()
conn.close()

