#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import os.path


def count_code(path, key):
    # with open(path, 'r') as f:
    #     mylist = f.readlines()
    #     print(len(mylist))
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isdir(f_path):
            count_code(f_path)
        elif os.path.isfile(f_path) and os.path.splitext(f_path)[1] == key:
            with open(f_path, 'r', encoding='utf-8') as ff:
                mylist = ff.readlines()
                print(os.path.split(f_path)[1] + '------------' + str(len(mylist)))


if __name__ == '__main__':
    count_code(r'G:\python_web_site\web', '.py')