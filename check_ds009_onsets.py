""" Check against older event files
"""
from os.path import join as pjoin, exists, dirname, split as psplit
from glob import glob

import numpy as np
import pandas as pd

from ds009_onsets import TASK_DEFS, parse_tsv_name, tsv2events, NEW_COND_PATH

OLD_COND_PATH = pjoin(dirname(__file__), 'old_onsets')


def older_cond_filenames(sub_no, task_name, run_no, model_no=1):
    info = TASK_DEFS[task_name]
    old_task_no = info['old_no']
    run_no = run_no if run_no is not None else 1
    root = pjoin('sub%03d' % sub_no,
                 'model',
                 'model%03d' % model_no,
                 'onsets',
                 'task%03d_run%03d' % (old_task_no, run_no))
    filenames = []
    for i, name in enumerate(info['conditions']):
        filenames.append(pjoin(root, 'cond%03d.txt' % (i + 1)))
    return filenames


def check_stopsignal(tsv_path, old_path):
    path, fname = psplit(tsv_path)
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    cond_fnames = older_cond_filenames(sub_no, task_name, run_no)
    orig_df = pd.read_table(tsv_path)
    events = tsv2events(tsv_path)
    new_cond_prefix = pjoin(
        path, 'sub-%02d_task-stopsignal_run-%02d_label-' %
        (sub_no, run_no))
    for i, name in enumerate(TASK_DEFS['stopsignal']['conditions']):
        ons_dur_amp = events[name]
        # Check new event file
        new_cond_fname = new_cond_prefix + name + '.txt'
        new_cond_res = np.loadtxt(new_cond_fname)
        if ons_dur_amp.size == 0:
            assert new_cond_res.size == 0
        else:
            assert np.allclose(ons_dur_amp, new_cond_res, atol=1e-5)
        old_cond_fname = pjoin(old_path, cond_fnames[i])
        if not exists(old_cond_fname):
            assert(len(ons_dur_amp) == 0)
            continue
        old_events = np.atleast_2d(np.loadtxt(old_cond_fname))
        run_part = '' if run_no is None else ' run {}'.format(run_no)
        msg = 'check sub {}{} condition {} (cond no {})'.format(
            sub_no, run_part, name, (i + 1))
        if len(ons_dur_amp) != len(old_events):
            print(msg)
            print_disjoint_events(ons_dur_amp, old_events, orig_df)
        elif not np.allclose(ons_dur_amp, old_events, atol=1e-4):
            print(msg)
            print('onsets do not match to given precision')


def print_disjoint_events(new, old, data_frame):
    new_not_old = ons_difference(new, old)
    if new_not_old:
        print('Events in new not old')
        print(difference_report(new_not_old, data_frame))
    old_not_new = ons_difference(old, new)
    if old_not_new:
        print('Events in old not new')
        print(difference_report(old_not_new, data_frame))


def ons_difference(first, second):
    difference = set()
    ons_2 = second[:, 0]
    for onset in first[:, 0]:
        if not np.any(np.isclose(ons_2, onset, atol=1e-4)):
            difference.add(onset)
    return difference


def difference_report(rounded_onsets, data_frame):
    for onset in rounded_onsets:
        filtered = data_frame[
            np.isclose(data_frame['onset'], onset, atol=1e-4)
                      ]
        assert len(filtered) == 1
        print(filtered)


def test_stopsignal():
    for tsv_path in glob(pjoin(NEW_COND_PATH,
                               'sub-*',
                               'func',
                               'sub*stopsignal*tsv')):
        check_stopsignal(tsv_path, OLD_COND_PATH)


def test_older_cond_filenames():
    assert older_cond_filenames(1, 'stopsignal', 1) == [
        pjoin('sub001', 'model', 'model001', 'onsets', 'task002_run001',
              'cond%03d.txt' % j) for j in range(1, 5)]
