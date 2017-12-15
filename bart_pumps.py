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

# Mean of the regressor
counts = [count for name, count in pumps]
mean_count = sum(counts) / len(counts)

# Write text file with pump numbers
with open('bart_pumps.txt', 'wt') as fobj:
    for name, count in pumps:
        centred = count - mean_count
        fobj.write('{}\t{:.2f}\n'.format(name, centred))
