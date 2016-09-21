#
# Skeleton file for the Python "Hello World" exercise.
#
# -*- coding: utf-8 -*-

def hello(name=None):
    if name:
        print(name)
        return "Hello, {}!".format(name)
    else:
        return "Hello, World!"
