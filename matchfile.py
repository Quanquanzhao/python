# -*- coding:utf-8 -*-

import os

if __name__ == '__main__':
    fname = "C:\code\\1.txt"
    fnamesrc = "C:\code\\app.txt"
    fdst = "C:\code\\2.txt"
    with open(fname, 'r') as fobj:
        with open(fdst, 'a+') as ft:
            for eachline in fobj:
                flag = 0
                eachline = eachline.lower().rstrip().lstrip()
                with open(fnamesrc, 'r') as fsrc:
                    for src in fsrc:
                        if src.lower().find(eachline) != -1:
                            newline = eachline + '\t' + src.rstrip() + '\n'
                            ft.write(newline)
                            flag = 1
                            break
                    if flag == 0:
                        ft.write(eachline + '\n')
