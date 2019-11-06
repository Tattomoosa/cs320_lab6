#!/usr/bin/env python3
#

import sys
import os
import shutil

def usage():
  print ('usage: ./find.py [--copy dirname] root file')

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
