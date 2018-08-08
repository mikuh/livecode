from aiohttp import web
import aiohttp_jinja2


class ManageCode(web.View):
    """用户操作页面
    """
    @aiohttp_jinja2.template('manage_code.html')
    async def get(self):
        id = self.request.match_info['id']
        cursor = self.request.app['db'].cursor()
        live_code_info, qr_codes = None, None
        try:
            cursor.execute('select id,link_index, link_title, skip_num, scan_num, (select count(1) from qr_code where img_src=link_code.link_index) as pic_num from link_code where link_index = ?', [id])
            live_code_info = cursor.fetchone()

            cursor.execute("select id, img_src from qr_code where link_index = ?", [id])
            qr_codes = cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return {"live_code_info": live_code_info, "qr_codes": qr_codes}
