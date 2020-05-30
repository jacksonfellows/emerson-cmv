#!/usr/bin/env python3
import csv

associated_tcrs = set()

def make_tuple(csv_row):
    return (
        row[0], # amino_acid
        row[1], # v_family
        row[2], # v_gene
        int(row[3]) if row[3] != 'NA' else float('nan'), # v_allele
        row[4], # j_family
        row[5], # j_gene
        int(row[6]) if row[6] != 'NA' else float('nan') # j_allele
    )

# init associated_tcrs
with open('cmv_associated_tcrs.csv') as f:
    f.readline() # skip header
    for row in csv.reader(f):
        tup = make_tuple(row)
        associated_tcrs.add(tup)

from sys import argv
from os.path import basename

for name in argv[1:]:
    patient_name = basename(name).split('.')[0]
    n = k = 0
    with open(name) as f:
        f.readline() # skip header
        for row in csv.reader(f):
            tup = make_tuple(row)
            if tup in associated_tcrs:
                k += 1
            n += 1
    print(','.join([patient_name, int(n), int(k)]))
