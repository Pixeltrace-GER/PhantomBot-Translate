#!/usr/bin/python3

import os
import re

def find_files(root, ext):
  for root, dirs, files in os.walk(root):
    for f in files:
      if f.lower().endswith(ext):
        f = os.path.join(root, f)
        yield f

    for d in dirs:
      d = os.path.join(root, d)
      find_files(d, ext)
