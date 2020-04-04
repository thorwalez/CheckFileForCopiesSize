#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
# @author Mike Hartl <mike_hartl@gmx.de>
# @copyright 2020 Mike Hartl
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
# @version 0.0.1


import unittest

from .Inspector.Exemplar import Exemplar

class ExemplarTestCase(unittest.TestCase):
    def test_inspect(self):
        instance = Exemplar()

        contentRow = ["","","","","","","","","","","","","","","","","","","","","","","","","70"]

        content = []
        content.insert(0,[])
        content.insert(1,contentRow)

    def test_inspectRaiseCall(self):
        instance = Exemplar()

        contentRow = ["","","","","","","","","","","","","","","","","","","","","","","","","90"]

        content = []
        content.insert(0,[])
        content.insert(1,contentRow)

        try:
            instance.inspect(content)
        except Exception as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
# the comment lines are not running exectly
#        with self.assertRaises(Exception, instance.inspect(content)) as context:
#        self.assertRaises(Exception, instance.inspect(content))

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
