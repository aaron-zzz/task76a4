# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3b69de3(1),5,'fail')
if __name__ == '__main__':
    unittest.main()