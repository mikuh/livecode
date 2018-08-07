from aiohttp import web
import aiohttp_jinja2



class Index(web.View):
    """用户操作页面
    """
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        cursor = self.request.app['db'].cursor()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchone()
        print(row)
        cursor.close()
        return {"msg": "hello"}

