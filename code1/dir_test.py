
# Script Name		: dir_test.py
# Author			: Craig Richards
# Created			: 29th November 2011
# Last Modified		:
# Version			: 1.0
# Modifications		:

# Description		: Tests to see if the directory testdir exists, if not it will create the directory for you

from __future__ import print_function
from code1.color_print import Logger
import os

try:
    home = os.path.expanduser('~')
    Logger.warn(home)
    if not os.path.exists(home):
        print(home + 'not exists.')
except Exception as e:
    print(e)
