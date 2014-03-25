__author__ = 'koo'

import pkg_resources


def read_file_string(path):
    split_path = path.split('/')
    sub_path = ''
    for p in split_path:
        if not p is split_path[0]:
            sub_path += p + '/'
    return pkg_resources.resource_string(split_path[0], sub_path.rstrip('/'))