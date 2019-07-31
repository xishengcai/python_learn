#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 实时读取shell命令的结果

import subprocess


def run(command):
    subprocess.call(command, shell=True)


def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode("gbk")   # utf-8, gbk, utf-16, gb2312  , windows: gbk, linux: utf-8
        print line
    return p.wait()


if __name__ == "__main__":
    # case1 success, return code 0
    cmd = "ping www.baidu.com"
    print sh(cmd)

    # case2 cmd not found, linux return code 127, windows return code 1
    cmd = "pingggg www.baidu.com"
    print sh(cmd)
