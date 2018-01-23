#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


if __name__ == '__main__':
    path = r'G:\python_web_site\web\webservice\apierror.py'
    with open(path, 'r') as f:
        for index, line in enumerate(f):
            print(str(index) + '=======' + line)