#!/usr/bin/env python
""" Show slice order for JSON file
"""

import sys
import json

import numpy as np

def main():
    for fname in sys.argv[1:]:
        with open(fname, 'rt') as fobj:
            info = json.load(fobj)
        slice_times = info['SliceTiming']
        print("Slice order for " + fname + " where 1 is the first")
        print(np.argsort(slice_times) + 1)


if __name__ == '__main__':
    main()
