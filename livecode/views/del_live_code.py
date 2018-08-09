from aiohttp import web
import os


class DelLiveCode(web.View):
    """删除活码
    """
    async def get(self):
        link_index = self.request.match_info['link_index']
        cursor = self.request.app['db'].cursor()
        try:
            cursor.execute("select img_src from qr_code where link_index = ?", [link_index])
            rows = cursor.fetchall()
            cursor.execute("delete from link_code where link_index = ?", [link_index])
            cursor.execute("delete from qr_code where link_index = ?", [link_index])
            self.request.app['db'].commit()
            live_code_file = f'./static/images/link/{link_index}.png'
            if os.path.exists(live_code_file):
                os.remove(live_code_file)
            for row in rows:
                qr_code_file = f'./static/images/qrcode/{row["img_src"]}.png'
                if os.path.exists(qr_code_file):
                    os.remove(qr_code_file)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return web.HTTPFound('/')