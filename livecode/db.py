import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


async def attach_db(app):
    conn = sqlite3.connect('./live_code.db')
    conn.row_factory = dict_factory
    app['db'] = conn


