#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
# @author Mike Hartl <mike_hartl@gmx.de>
# @copyright 2020 Mike Hartl
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
# @version 0.0.1


import sys

from Reader.Reader import Reader
from Inspector.Exemplar import Exemplar
from List.Pd5Files import Pd5Files

try:
    ## bei größer 1 wurde ein Parameter mit geben
    if len(sys.argv) == 1:
        raise Exception("Kein Pfad angegeben")

    path = sys.argv[1]

    instance = Pd5Files()
    pd5FilenameList = instance.list(path)

    ## Instance Reader Class
    readerInstance = Reader()
    ## reade File and give content

    for filename in pd5FilenameList:
        content = readerInstance.read(path+filename)

        inspector = Exemplar()
        inspector.inspect(content)

    print("Prüfung ist fertig")

except Exception as err:
    print("{}".format(err))
