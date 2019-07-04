def file_not_found_error(start_response, fname):
    response_headers = [('Content-type', 'text/plain')]
    start_response('404', response_headers)
    return bytes('File %s not found' % fname, 'utf-8')


def url_not_found(start_response, url):
    response_headers = [('Content-type', 'text/plain')]
    start_response('404', response_headers)
    return bytes('Url %s not found' % url, 'utf-8')
