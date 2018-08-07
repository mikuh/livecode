import sqlite3

async def attach_db(app):
    app['db'] = sqlite3.connect('./live_code.db')






