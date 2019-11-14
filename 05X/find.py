#!/usr/bin/env python3
#

import sys
import os
import shutil

def usage():
  print ('usage: ./find.py [--copy dirname] root file')

def find(root, filename):
    return [ os.path.join(d, filename)
            for d, _subds, files in os.walk(root)
            if filename in files ]

def copy(found, new_dir):
    path = f'{os.path.join(os.getcwd(), new_dir)}'
    if not os.path.exists(path):
        os.mkdir(path)
    for f in found:
        shutil.copyfile(f, os.path.join(path, f[1:].replace('/', '_')))


def main():
  if len(sys.argv) < 2: usage()
  if sys.argv[1] == '--copy':
     if len(sys.argv) < 5: usage()
     new_dir = sys.argv[2]
     root = sys.argv[3]
     filename = sys.argv[4]
     found = find(root,filename)
     for f in found:
       print(f)
     copy(found,new_dir)
  else:
     if len(sys.argv) < 3: usage()
     root = sys.argv[1]     
     filename = sys.argv[2]
     found = find(root,filename)
     for f in found:
       print(f)

if __name__ == '__main__':
  main()
