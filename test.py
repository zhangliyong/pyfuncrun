# -*- coding: utf8 -*-
"""
A couple of functions for pyfuncrun to test
"""
from __future__ import (absolute_import, print_function,
                        unicode_literals)
import sys


def print_hello():
    print("Hello, pyfuncrun")


def print_argv():
    print(sys.argv)


def func_with_args(a, b):
    print(a + b)
