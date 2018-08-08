from aiohttp import web
import aiohttp_jinja2
import time
from livecode import utils


class SignIn(web.View):
    """登录
    """
    @aiohttp_jinja2.template('sign_in.html')
    async def get(self):
      error = self.request.query.get('error', 0)
      return {'error': error}

    async def post(self):
        data = await self.request.post()
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute('SELECT password FROM users where phone = ?', [data['phone']])
            row = cursor.fetchone()
            cursor.close()
        except:
            row = None
        if row and row['password'] == utils.password_encrypt(data['password']):
            response = web.HTTPFound('/')
            user_cookie = "{}|{}|{}".format(data['phone'], utils.password_encrypt(data['phone']),
                                            int(time.time() + self.request.app['config']['expires']))
            response.set_cookie("user", user_cookie, expires=self.request.app['config']['expires'])
            return response
        else:
            return web.HTTPFound('/sign_in?error=1')



class Logout(web.View):
    """退出登录"""
    async def get(self):
        response = web.HTTPFound('/')
        response.del_cookie('user')
        return response