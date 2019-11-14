#!/usr/bin/env python3

import sys
import os.path
from collections import defaultdict
from itertools import permutations

# Fill in the missing routines, using the Java versions
# from lab4/08X and 10X as prototypes.
#
def read_integer_graph(gname):
    with open(f'{gname}.ig') as file:
        next(file); next(file)
        return read_graph(file, ' ')

def read_string_graph(gname, delim):
    with open(f'{gname}.sg') as file:
        return read_graph(file, delim)

def read_graph(file, delim):
        graph = defaultdict(list)
        for (v1, v2) in [(v[0], v2)
                for v in [line[:-1].split(delim) for line in file]
                for v2 in v[1:]]:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return dict(graph)

def write_dot_graph(gname, g):
    visited = []
    print(f'graph {gname} {{')
    for v1 in g:
        edges = [f'"{v1}" -- "{v2}"' for v2 in g[v1] if v2 not in visited]
        if len(edges) > 0:
            print(*edges, sep='\n')
        visited.append(v1)
    print('}')

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
