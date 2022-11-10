#!/usr/bin/python3
import os, re
import sqlite3

con = sqlite3.connect('/storage/test.db')

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

def add_var(var, val):
  print("Insert Val")

if __name__ == '__main__':
  print("Version 0.0.6")
  for file in find_files('/src', '.js'):
    with open(file, 'r', encoding='utf-8') as f:
      for ln in f:
        if ln.startswith("$.lang.register"):
          line_data = find_regex(ln)
          add_var(line_data[0],line_data[1])
    
