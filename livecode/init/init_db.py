"""初始化数据库
"""
import os, sys
import sqlite3
import logging
sys.path.extend(['../live_code/'])
from livecode.utils import load_config
from livecode.utils import password_encrypt
configs = load_config('../configs/base.yaml')


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

conn = sqlite3.connect('../live_code.db')

cursor = conn.cursor()

def init_db():
    logging.info("正在初始化数据库...")

    # 创建用户表
    cursor.execute('CREATE TABLE users (id integer primary key AUTOINCREMENT, phone varchar(20), password varchar(40))')
    cursor.execute("CREATE INDEX phone ON users (phone)")
    # 插入默认的管理员账户
    cursor.execute("INSERT into users (phone, password) VALUES (?, ?)", [configs['default_account']['phone'], configs['default_account']['password']])

    # 创建用户链接码表
    cursor.execute('CREATE TABLE link_code (id integer primary key AUTOINCREMENT, phone varchar(20), link_index varchar(40), link_title varchar(64),skip_num integer, scan_num integer)')
    cursor.execute("CREATE INDEX link_index ON link_code (link_index)")
    cursor.execute("CREATE INDEX phone_index ON link_code (phone)")

    # 创建用户二维码表
    cursor.execute('CREATE TABLE qr_code (id integer primary key AUTOINCREMENT, link_index varchar(40), img_src varchar(100), label varchar(64))')
    cursor.execute('create index img_src on qr_code (img_src)')



    logging.info("初始化数据表完成。")

    cursor.close()
    conn.commit()
    conn.close()



def insert_user(phone, password):
    """插入新用户"""
    cursor.execute("INSERT into users (phone, password) VALUES (?, ?)",
                   [phone, password_encrypt(password)])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()