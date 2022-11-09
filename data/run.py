#!/usr/bin/python3
import os, re
import pysondb


def find_files(root, ext):
  for root, dirs, files in os.walk(root):
    for f in files:
      if f.lower().endswith(ext):
        f = os.path.join(root, f)
        yield f

    for d in dirs:
      d = os.path.join(root, d)
      find_files(d, ext)
      
      
def replace_regex(text):
  print(re.sub("'(?:[^\\']|\\\\|\\')*'", "", text))
      
def find_regex(line):
  return re.findall(r"'(?:[^\\']|\\\\|\\')*'", line)



if __name__ == '__main__':
  print("List Dir")
  os.listdir('/src')
  
  print("List Files")
  for f in find_files('/src', '.js'):
    print(f)
    
