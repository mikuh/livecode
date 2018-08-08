from aiohttp import web
import aiohttp_jinja2
from livecode.utils import sha1_encrypt, create_live_code
import time

class Index(web.View):
    """用户操作页面
    """
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        # 获取我的活码
        phone = self.request['user']
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute("select id,link_index,link_title, skip_num, scan_num, (select count(1) from qr_code where img_src=link_code.link_index) as pic_num from link_code where phone = ?", [phone])
            rows = cursor.fetchall()
            print(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return {"phone": self.request['user'], "data": rows}


class CreateLiveCode(web.View):
    """创建活码
    """

    async def post(self):
        data = await self.request.post()
        src = sha1_encrypt(self.request['user'] + str(time.time()))
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute("insert into link_code (phone,link_index, link_title, skip_num, scan_num) VALUES (?, ?, ?, ?, 0)", [self.request['user'], src, data['link_title'], data['skip_num']])
            create_live_code(self.request.app, src)
            self.request.app['db'].commit()
        except Exception as e:
            print(e)
            return web.json_response({"error_code": 1, 'msg': "创建失败，请稍后重试"})
        finally:
            cursor.close()
        return web.json_response({'error_code': 0, 'msg': "创建活码成功！"})


