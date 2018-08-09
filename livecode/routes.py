from aiohttp import web
from livecode.views import index, sign_in, manage_code, code_scan
from livecode.apis import update_qrcode
from livecode.views import del_live_code, del_qrcode
URLS = list()

# for web view
URLS.append(web.view('/', index.Index))
URLS.append(web.view('/sign_in', sign_in.SignIn))
URLS.append(web.view('/logout', sign_in.Logout))
URLS.append(web.view('/create_live_code', index.CreateLiveCode))
URLS.append(web.view('/manage_code/{id}', manage_code.ManageCode))
URLS.append(web.view('/update_qrcode', update_qrcode.UpdateQrCode))
URLS.append(web.view('/code_scan/{name}', code_scan.CodeScan))
URLS.append(web.view('/del_live_code/{link_index}', del_live_code.DelLiveCode))
URLS.append(web.view('/del_qrcode/{img_src}', del_qrcode.DelQrcode))

def get_urls():
    return URLS


__all__ = ['get_urls']
