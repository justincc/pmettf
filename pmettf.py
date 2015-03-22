#!/usr/bin/python

import os
import os.path
import re
import shutil
import sys

#################
### CONSTANTS ###
#################
CONVERSION_DIR = "converted/"

#################
### FUNCTIONS ###
#################
def cleanString(dirtyString):
  return dirtyString.strip().replace(",", "").replace(".", "").replace("'", "").replace(" ", "-").lower()

############
### MAIN ###
############

with open(sys.argv[1]) as f:
  contents = f.readlines()
  #contents = f.read().splitlines()

contents = [line[:-2] for line in contents]

categories = {}
titleIndex = 0

for i in range(len(contents)):
  # A blank line with no additional CR indicates the end of a record
  if contents[i] == "":
    if contents[i-1][-1] != '\r':
      rawCategory = contents[i-1]
      rawCategory = cleanString(rawCategory)

      if not rawCategory in categories:
        categories[rawCategory] = []
      
      title = cleanString(contents[titleIndex])

      print "title [%s]" % (title)

      # text body includes the title
      text = contents[titleIndex:i-1]
      text = [line.rstrip() for line in text]
    
      categories[rawCategory].append({'title' : title, 'text' : text})

      # Next title will follow the category
      titleIndex = i + 1

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

for category, memos in categories.iteritems():
  print "%s" % (category)

  for memo in memos:
    print "  %s" % (memo['title'])

# Create file tree
if (os.path.exists(CONVERSION_DIR)):
  shutil.rmtree(CONVERSION_DIR)

os.mkdir(CONVERSION_DIR)

for category, memos in categories.iteritems():
  categoryDir = os.path.join(CONVERSION_DIR, category)
  os.mkdir(categoryDir)

  for memo in memos:
    titlePath = os.path.join(categoryDir, "%s.txt" % (memo['title']))

    with open(titlePath, "w") as f:
      for line in memo['text']:
        f.write("%s\n" % line)
