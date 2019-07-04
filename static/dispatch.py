import os

from utils import file_not_found_error


def dispatch(environ, start_response):
    fname = environ['REQUEST_URI'].strip('/')
    path = os.path.dirname(os.path.abspath(__file__)) + '/files/'
    try:
        if fname == '' or fname == '/':
            response_headers = [('Location', 'index.html')]
            start_response('301', response_headers)
            return b''
        if not os.path.isfile(path + fname):
            new_fname = fname + '.html'
            if not os.path.isfile(path + new_fname):
                return file_not_found_error(start_response, fname)
            else:
                fname = new_fname

        with open(path + fname, 'rb') as f:
            response_headers = [('Content-type', 'text/html')]

            start_response('200', response_headers)
            return f.read()
    except FileNotFoundError as e:
        return file_not_found_error(start_response, fname)
