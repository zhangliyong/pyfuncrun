# -*- coding: utf8 -*-
"""
A couple of functions for pyfuncrun to test
"""
from __future__ import (absolute_import, print_function,
                        unicode_literals)
import sys
import unittest
from pyfuncrun import main


def return_true():
    return True


def return_false():
    return False


def return_sys_argv():
    return sys.argv


def func_with_args(a, b):
    return ((a + b), sys.argv)


def func_with_kwargs(a, b, c=1):
    return ((a + b + c), sys.argv)


class ClassCall(object):

    def __call__(self):
        return (True, sys.argv)


class_call = ClassCall()


class TestPyFuncRun(unittest.TestCase):

    def setUp(self):
        sys.argv = ['pyfuncrun', 'path.to.func', 1, 2, 3, 4]

    def test_true(self):
        sys.argv[1] = 'test.return_true'
        self.assertTrue(main())

    def test_false(self):
        sys.argv[1] = 'test.return_false'
        self.assertFalse(main())

    def test_sys_argv(self):
        sys.argv[1] = 'test.return_sys_argv'

        before_argv = sys.argv[:]
        before_argv.pop(1)
        self.assertEqual(before_argv, main())

    def test_args(self):
        sys.argv[1] = 'test.func_with_args'

        before_argv = sys.argv[:]
        before_argv[1:4] = []
        self.assertEqual((3, before_argv), main())

    def test_kwargs(self):
        sys.argv[1] = 'test.func_with_kwargs'

        before_argv = sys.argv[:]
        before_argv[1:5] = []
        self.assertEqual((6, before_argv), main())

    def test_non_func(self):
        sys.argv[1] = 'test.class_call'

        before_argv = sys.argv[:]
        before_argv[1:2] = []
        self.assertEqual((True, before_argv), main())
