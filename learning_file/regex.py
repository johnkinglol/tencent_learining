#!/usr/bin/env python
# coding=utf-8
import re


# use to verify email
if __name__ == '__main__':
    regex = re.compile("^(\w+)@(\w+)\.com$")
    print(regex.match("someon@gmail.com").groups())