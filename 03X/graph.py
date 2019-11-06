#!/usr/bin/env python3

import sys
import os.path

# Fill in the missing routines, using the Java versions
# from lab4/08X and 10X as prototypes.
#
def read_integer_graph(gname):
    graph = {}
    with open(f'{gname}.ig') as file:
        next(file); next(file)
        for (v1, v2) in (int(s) for s in line.split() for line in file):
            graph.setdefault(v1, []).append(v2)
    return graph

def read_string_graph(gname, delim):
    graph = {}
    with open(f'{gname}.sg') as file:
        for v in (line[:-1].split(delim) for line in file):
            graph.setdefault(v[0], []).extend(v[1:])
    return graph

def write_dot_graph(gname, g):
    print(f'graph {gname} {{', *[f'"{v1}" -- "{v2}"' for v1 in g for v2 in g[v1]], '}', sep='\n')

def usage():
  print('usage: ./graph.py [ file.ig | file.sg sep ]')
  exit(0)

def main():
  if len(sys.argv) < 2: usage()    
  f = sys.argv[1]
  gname,kind = os.path.splitext(f)
  if kind == '.ig':
    if len(sys.argv) != 2: usage()
    g = read_integer_graph(gname)
  elif kind == '.sg':
    if len(sys.argv) != 3: usage()
    g = read_string_graph(gname,sys.argv[2])
  else: usage()
  write_dot_graph(gname,g)
  
if __name__ == '__main__':
  main()
