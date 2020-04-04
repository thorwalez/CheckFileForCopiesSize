#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
# @author Mike Hartl <mike_hartl@gmx.de>
# @copyright 2020 Mike Hartl
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
# @version 0.0.1

class Exemplar:
    def inspect(self, content):
        del content[0]

        for row in content:
            columns = list(row)

            value = columns[24]

            if (int(value) > 70):
                raise Exception("Fehler falsche Exemplar Groesse {}".format(value))
