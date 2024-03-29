#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/13 上午11:06
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : fix_one.py
# @Software: PyCharm

import os
import re


def main(more_core):
    shs = 'find -type f -name *xml|xargs grep "GALAXY_SLOTS"'
    a = os.popen(shs).read()
    use_file_list = real_use_file_list(a)
    for use_file in use_file_list:
        rr = re.compile(r'\\\${GALAXY_SLOTS:-[0-9]+}')
        with open(use_file, 'r') as f:
            texts = f.read()
        m = rr.findall(texts)
        if m:
            find_str = m[0]
            rep_str = find_str.replace('\${GALAXY_SLOTS:-', '')
            rep_str = rep_str.replace('}', '')
            new_texts = texts.replace(find_str, more_str(rep_str, more_core))
            with open(use_file, 'w') as g:
                g.write(new_texts)
        else:
            rr = re.compile(r'\${GALAXY_SLOTS:-[0-9]+}')
            m = rr.findall(texts)
            if m:
                find_str = m[0]
                rep_str = find_str.replace('${GALAXY_SLOTS:-', '')
                rep_str = rep_str.replace('}', '')
                print(find_str, rep_str)
                print(find_str, more_str(rep_str, more_core))
                new_texts = texts.replace(find_str, more_str(rep_str, more_core))
                with open(use_file, 'w') as g:
                    g.write(new_texts)
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


def real_use_file_list(system_stdout):
    uu = system_stdout.split('\n')
    use_file_list = []
    for i in uu:
        if "xml:" in i:
            use_file, text = i.split('xml:')[0] + "xml", i.split('xml:')[1]
            use_file_list.append(use_file)
    use_file_list = list(set(use_file_list))
    return use_file_list


def main_samtools(more_core, sam_movement="sort"):
    shs = 'find -type f -name *xml|xargs grep "samtools %s"' % sam_movement
    a = os.popen(shs).read()
    use_file_list = real_use_file_list(a)
    for q in use_file_list:
        with open(q, 'r') as f:
            texts = f.read()
        new_texts = texts.replace("samtools %s" % sam_movement,
                                  "samtools %s -@ %s" % (sam_movement, str(more_core)))
        with open(q, 'w') as g:
            g.write(new_texts)
        # print(i, i + "@ %s" % str(more_core))


if __name__ == '__main__':
    main(16)
    main_samtools(16)
    main_samtools(16, sam_movement='view')
