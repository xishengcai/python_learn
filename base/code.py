#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

aa = '{"ab": "蔡锡生"}'


def josn_encode(dict, encoding):
    for k, v in dict:
        dict[k] = v.encode(encoding)
    return dict


def throw_error():
    # Exception: 抛出一个异常
    raise Exception("抛出一个异常")


if __name__ == "__main__":
    b = json.loads(aa)
    print b  # unicode
    print b["ab"]  # 自动解码

    b["ab"] = b["ab"].encode("utf-8")  # 重新编码
    print b
    print b["ab"] == "蔡锡生"

