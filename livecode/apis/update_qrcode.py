from aiohttp import web
import aiohttp_jinja2
from livecode.utils import sha1_encrypt
import time


class UpdateQrCode(web.View):
    """用户上传二维码
    """
    async def post(self):
        phone = self.request['user']
        form_data = await self.request.post()
        name = sha1_encrypt(phone + str(time.time()))
        print(name)
        img = form_data['qrcode']
        file_content = img.file.read()
        with open(f"./static/images/qrcode/{name}.png", 'wb') as f:
            f.write(file_content)
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute("insert into qr_code (link_index, img_src) values(?, ?)", [form_data['link_index'], name])
            self.request.app['db'].commit()
        except Exception as e:
            print(e)
            return web.json_response({"error_code": 1, "msg": "保存二维码失败，请稍后重试！"})
        finally:
            cursor.close()


        return web.json_response({"error_code": 0})
