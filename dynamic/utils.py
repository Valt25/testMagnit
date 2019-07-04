import json
from urllib import parse


class Response:

    def __init__(self, status=200, data='', headers=None):
        if not headers:
            headers = []
        self.status = status
        self.data = data
        self.headers = headers


def jsonify(view_func):
    def new_view_func(*args, **kwargs):
        response = view_func(*args, **kwargs)

        response.data = json.dumps(response.data)
        response.headers.append(('Content-Type', 'application/json'))

        return response

    return new_view_func


def get_params_in_dict(view_func):
    def new_view_func(environ, *args, **kwargs):
        get_params = parse_get_params(environ)

        environ['QUERY_DICT'] = get_params

        return view_func(environ, *args, **kwargs)

    return new_view_func


def parse_post_in_dict(view_func):
    def new_view_func(environ, *args, **kwargs):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = environ['wsgi.input'].read(request_body_size)
        post_dict = dict(parse.parse_qsl(request_body.decode('utf-8')))
        environ['POST_DICT'] = post_dict
        return view_func(environ, *args, **kwargs)

    return new_view_func


def parse_get_params(environ):
    return dict(parse.parse_qsl(parse.urlsplit(environ['REQUEST_URI']).query))
