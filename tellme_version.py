#!/usr/bin/python

import sys
print(sys.version_info)
if sys.version_info[0] < 3:
    raise Exception("Must be Using Python 3")

