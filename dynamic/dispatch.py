from dynamic.urls import urls
from dynamic.utils import Response
from utils import url_not_found


def get_view_func_from_urls(environ, urls):
    for url in urls:
        if environ['PATH_INFO'].split('?')[0].strip('/') == url[0] and environ['REQUEST_METHOD'] == url[1]:
            return url[2]


def generate_wsgi_response(start_response, response: Response):
    start_response(str(response.status), response.headers)
    return bytes(str(response.data), 'utf-8')


def dispatch(environ, start_response):
    view_func = get_view_func_from_urls(environ, urls)
    if view_func:
        response = view_func(environ)
        return generate_wsgi_response(start_response, response)
    else:
        return url_not_found(start_response, environ['REQUEST_URI'])
