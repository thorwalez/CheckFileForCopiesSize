#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
# @author Mike Hartl <mike_hartl@gmx.de>
# @copyright 2020 Mike Hartl
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
# @version 0.0.1


import csv

class Reader:
    def read(self, filename):
        with open(filename, encoding="ISO-8859-1") as csvFile:
            content = csv.reader(csvFile, delimiter=";")
            return list(content)

    def checkColumns(self, content):
        # return self.firstLine(content)
        # return len(self.firstLine(content))
        return len(self.firstLine(content)) == 62

    def firstLine(self, content):
        try:
            return content[0]
        except StopIteration:
            return None
