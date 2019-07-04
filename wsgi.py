import wsgiref.util

from dynamic.db import create_db, db_file_name
from static.dispatch import dispatch as static_dispatch
from dynamic.dispatch import dispatch as dynamic_dispatch


def application(environ, start_response):
    pref = wsgiref.util.shift_path_info(environ)

    if pref != 'api':
        return static_dispatch(environ, start_response)
    else:
        return dynamic_dispatch(environ, start_response)


create_db(db_file_name)
