from aiohttp import web
import os


class DelQrcode(web.View):
    """删除二维码
    """
    async def get(self):
        img_src = self.request.match_info['img_src']
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute("delete from qr_code where img_src = ?", [img_src])
            self.request.app['db'].commit()
            qr_code_file = f'./static/images/qrcode/{img_src}.png'
            if os.path.exists(qr_code_file):
                os.remove(qr_code_file)
        except Exception as e:
            print(e)
            return web.json_response({"error_code": 1, "msg": "删除失败，请重试"})
        finally:
            cursor.close()
        return web.json_response({"error_code": 0, "msg": "删除成功"})