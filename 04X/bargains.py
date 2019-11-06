#!/usr/bin/env python3

import sys
import os.path

QUANTITY = 0
NAME = 1
GRADE = 2
COLOR = 3
PRICE = 4
COST = 5

def usage():
    print('usage: ./bargains.py file')
    exit(0)

def main():
    # try:
    bargains = []
    filename = sys.argv[1]
    with open(filename) as file:
        outfile = f'{filename.split(".")[0]}.bargains'
        next(file)
        products = [
                [*d, int(d[QUANTITY]) * float(d[PRICE])]
                for d in (line[:-1].split(',') for line in file)]
        budget = sum(p[COST] for p in products)/len(products) * 1.5
        bargains = [
                p[NAME]
                for p in products
                if p[COST] < budget
                and (p[GRADE] == 'superior'
                or p[COLOR] == 'blue')]
        with open(outfile, 'w') as out:
            out.write('\n'.join(bargains))

if __name__ == '__main__':
    main()