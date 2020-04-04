#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
# @author Mike Hartl <mike_hartl@gmx.de>
# @copyright 2020 Mike Hartl
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
# @version 0.0.1


import os
import types

class Pd1Files:
    def list(self, path):
        internalList = []
        for item in next(os.walk(path)):
            if (type(item) is list):
                for filename in item:
                    if 'ms_pd1' in filename:
                        internalList.append(filename)
        return internalList