#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/13 上午11:06
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : fix_one.py
# @Software: PyCharm

import os
import sys
import re


def main(more_core):
    shs = 'find -type f -name *xml|xargs grep "GALAXY_SLOTS"'
    a = os.popen(shs).read().split('\n')
    for i in a:
        if "xml:" in i:
            use_file, text = i.split('xml:')[0] + "xml", i.split('xml:')[1]
            print file, text
            if "\\" in text:
                rr = re.compile(r'\\\${GALAXY_SLOTS:-[0-9]+}')
                with open(use_file, 'r') as f:
                    texts = f.read()
                m = rr.findall(texts)
                if m:
                    find_str = m[0]
                    rep_str = find_str.replace('\${GALAXY_SLOTS:-', '')
                    rep_str = rep_str.replace('}', '')
                    print(find_str, rep_str)
                    print(find_str, more_str(rep_str, more_core))
            else:
                rr = re.compile(r'\${GALAXY_SLOTS:-[0-9]+}')
                with open(use_file, 'r') as f:
                    texts = f.read()
                m = rr.findall(texts)
                if m:
                    find_str = m[0]
                    rep_str = find_str.replace('${GALAXY_SLOTS:-', '')
                    rep_str = rep_str.replace('}', '')
                    print(find_str, rep_str)
                    print(find_str, more_str(rep_str, more_core))
    pass


def more_str(rep_str, more_core):
    try:
        aa = int(rep_str)
        if aa != 1 and aa < more_core:
            return str(more_core)
        else:
            return rep_str
    except:
        pass


if __name__ == '__main__':
    main(16)
