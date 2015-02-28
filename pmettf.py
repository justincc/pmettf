#!/usr/bin/python

import os
import os.path
import re
import shutil
import sys

CONVERSION_DIR = "converted/"

with open(sys.argv[1]) as f:
  contents = f.readlines()
  #contents = f.read().splitlines()

contents = [line[:-2] for line in contents]

categories = {}

for i in range(len(contents)):
  if contents[i] == "":
    if contents[i-1][-1] != '\r':
      rawCategory = contents[i-1]
      rawCategory = rawCategory.replace(" ", "-").lower()

      if not rawCategory in categories:
        categories[rawCategory] = 1
      else:
        categories[rawCategory] += 1

  # Line with just the extra \r
#  if re.match('\r', contents[i]) and i > 2:
    # Just the \r\n in this case
#    if len(contents[i-1]) == 2:
"""
    print contents[i]
    print contents[i-1]
    print contents[i-2]
"""
"""
  if len(contents[i]) == 2:
    print contents[i-1]
"""

# categories = [c.replace(" ", "-").lower() for c in categories]

print "Cateogries are:"

for c, n in categories.iteritems():
  print "%s: %s" % (c, n)

if (os.path.exists(CONVERSION_DIR)):
  shutil.rmtree(CONVERSION_DIR)

os.mkdir(CONVERSION_DIR)

for c in categories.keys():
  os.mkdir(os.path.join(CONVERSION_DIR, c))
