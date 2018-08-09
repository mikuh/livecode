from aiohttp import web
from aiohttp.web import middleware
import time
from livecode import utils


@middleware
async def check_me(request, handler):
    """登录校验
    """
    if str(request.rel_url).startswith('/code_scan') or str(request.rel_url).startswith('/static/'):
        pass
    else:
        _user = request.cookies.get("user", None)
        if _user and not str(request.rel_url).startswith('/sign_'):
            user, secret, indate = _user.split("|")
            if int(indate) < time.time():
                return web.HTTPFound('/sign_in')
            if utils.password_encrypt(user) != secret:
                return web.HTTPFound('/sign_in')
            request['user'] = user
        elif not _user and not str(request.rel_url).startswith('/sign_'):
            return web.HTTPFound('/sign_in')
    response = await handler(request)
    return response