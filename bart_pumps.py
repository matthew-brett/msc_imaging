""" Calculate number of pumps per run for BART
"""

from os.path import join as pjoin, split as psplit
from glob import glob

import pandas as pd

start_path = 'ds000009_R2.0.3'
pumps = []
for tsv_path in glob(pjoin(start_path,
                               'sub-*',
                               'func',
                               'sub*balloon*tsv')):
    df = pd.read_table(tsv_path)
    inflates = len(df[df['action'] == 'ACCEPT'])
    pumps.append((psplit(tsv_path)[1], inflates))

# Write text file with pump numbers
with open('bart_pumps.txt', 'wt') as fobj:
    for name, n in pumps:
        fobj.write('{}\t{}\n'.format(name, n))

