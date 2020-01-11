import json
from exception import ftp_exit

ftp_mode = 'upload'


def generate_ftp_tuple(host='',
                       port=21,
                       user='',
                       password='',
                       path=''):
    return (host, port, user, password, path)
    pass


def parse_json_file(json_path):
    try:
        file_handle = open(json_path, "r+")
        pass
    except FileNotFoundError as e:
        ftp_exit(1,'Config file not found')
    else:
        json_dict = json.loads(file_handle.read())
        file_handle.close()
        host = json_dict.get("host", "")
        port = json_dict.get('port', -1)
        user = json_dict.get('user', '')
        password = json_dict.get('password', '')
        path = json_dict.get('path', '')
        mode = json_dict.get('mode', 'upload')
        set_mode(mode)
        return generate_ftp_tuple(host, port, user, password, path)
        pass


def get_mode():
    return ftp_mode


def set_mode(mode='upload'):
    if mode in ('upload', 'server', 'client'):
        ftp_mode = mode
        pass
    else:
        ftp_exit(1,"Mode not allowed")