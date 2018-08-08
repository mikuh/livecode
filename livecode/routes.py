from aiohttp import web
from livecode.views import index, sign_in, manage_code
from livecode.apis import update_qrcode
URLS = list()

# for web view
URLS.append(web.view('/', index.Index))
URLS.append(web.view('/sign_in', sign_in.SignIn))
URLS.append(web.view('/logout', sign_in.Logout))
URLS.append(web.view('/create_live_code', index.CreateLiveCode))
URLS.append(web.view('/manage_code/{id}', manage_code.ManageCode))
URLS.append(web.view('/update_qrcode', update_qrcode.UpdateQrCode))

def get_urls():
    return URLS


__all__ = ['get_urls']
