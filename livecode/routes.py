from aiohttp import web
from livecode.views import index

URLS = list()

# for web view
URLS.append(web.view('/', index.Index))


def get_urls():
    return URLS


__all__ = ['get_urls']
