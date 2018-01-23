#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import os.path


def count_code(path, key):
    # with open(path, 'r') as f:
    #     mylist = f.readlines()
    #     print(len(mylist))
    all_count = 0
    no_blank_count = 0
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isdir(f_path):
            count_code(f_path, key)
        elif os.path.isfile(f_path) and os.path.splitext(f_path)[1] == key:
            with open(f_path, 'r', encoding='utf-8') as ff:
                file_all_count = 0
                file_no_blank_count = 0
                for index, line in enumerate(ff):
                    all_count += 1
                    file_all_count += 1
                    if line.strip() == '':
                        continue
                    else:
                        file_no_blank_count += 1
                        no_blank_count += 1
                print(f_path + '------------' + '总行数=' + str(file_all_count) +
                      '         去掉空白行=' + str(file_no_blank_count))
                print('该路径下符合扩展名要求的文件总行数=' + str(all_count) + ' ,忽略空白行=' + str(no_blank_count))


if __name__ == '__main__':
    count_code(r'G:\python_web_site\web', '.py')