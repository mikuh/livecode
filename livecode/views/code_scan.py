from aiohttp import web
import aiohttp_jinja2

class CodeScan(web.View):
    """扫码
    """

    @aiohttp_jinja2.template('code_scan.html')
    async def get(self):
        link_index = self.request.match_info['name']
        cursor = self.request.app['db'].cursor()
        qr_code_src = None
        try:
            cursor.execute("select scan_num, skip_num from link_code where link_index = ?", [link_index])
            link_info = cursor.fetchone()
            index = int(link_info['scan_num'] / link_info['skip_num'])
            cursor.execute("select img_src from qr_code where link_index = ? order by id", [link_index])
            qr_code_src = cursor.fetchall()[index]['img_src']
            cursor.execute("update link_code set scan_num = scan_num + 1 where link_index = ?", [link_index])
            self.request.app['db'].commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        if qr_code_src:
            return {'qr_code_src': qr_code_src}
        return web.json_response({"Note": "No valid qr code has been read. Please try again"})
