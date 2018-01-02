""" Check against older event files

Run tests with:

    py.test check_ds009_onsets.py

You need to install pytest first. At the terminal:

    pip install pytest
"""
from os import unlink as remove
from os.path import join as pjoin, exists, dirname, split as psplit
from glob import glob
from tempfile import mkdtemp
from shutil import rmtree

import numpy as np
import pandas as pd

from ds009_onsets import (TASK_DEFS, parse_tsv_name, tsv2events, NEW_COND_PATH,
                          three_column, write_all_tasks)

import pytest

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


def check_task(tsv_path, old_path, fail=False, onset_field='onset'):
    path, fname = psplit(tsv_path)
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    run_part = '_run-%02d' % run_no if run_no is not None else ''
    cond_fnames = older_cond_filenames(sub_no, task_name, run_no)
    orig_df = pd.read_table(tsv_path)
    events = tsv2events(tsv_path)
    new_cond_prefix = pjoin(
        path, 'sub-%02d_task-%s%s_label-' %
        (sub_no, task_name, run_part))
    for i, name in enumerate(TASK_DEFS[task_name]['conditions']):
        ons_dur_amp = events[name]
        # Check new event file
        new_cond_fname = new_cond_prefix + name + '.txt'
        if len(ons_dur_amp) == 0:
            assert not exists(new_cond_fname)
        else:
            new_cond_res = np.loadtxt(new_cond_fname)
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
            print_disjoint_events(ons_dur_amp, old_events, orig_df,
                                  onset_field)
            if fail:
                assert False
        elif not np.allclose(ons_dur_amp, old_events, atol=1e-4):
            print(msg)
            print('onsets / durations / amplitudes do not match '
                  'to given precision')
            if fail:
                assert False


def print_disjoint_events(new, old, data_frame, onset_field='onset'):
    new_not_old = ons_difference(new, old)
    if new_not_old:
        print('Events in new not old')
        print(difference_report(new_not_old, data_frame, onset_field))
    old_not_new = ons_difference(old, new)
    if old_not_new:
        print('Events in old not new')
        print(difference_report(old_not_new, data_frame, onset_field))


def ons_difference(first, second):
    difference = set()
    ons_2 = second[:, 0]
    for onset in first[:, 0]:
        if not np.any(np.isclose(ons_2, onset, atol=1e-4)):
            difference.add(onset)
    return difference


def difference_report(rounded_onsets, data_frame, onset_field='onset'):
    for onset in rounded_onsets:
        filtered = data_frame[
            np.isclose(data_frame[onset_field], onset, atol=1e-4)
                      ]
        assert len(filtered) == 1
        print(filtered)


def test_parse_tsv_name():
    assert (parse_tsv_name(
        'sub-01_task-stopsignal_run-01_events.tsv') ==
        (1, 'stopsignal', 1))
    assert (parse_tsv_name(
        pjoin('foo', 'bar', 'sub-01_task-stopsignal_run-01_events.tsv')) ==
        (1, 'stopsignal', 1))
    assert (parse_tsv_name(
        'sub-13_task-balloonanalogrisktask_events.tsv') ==
        (13, 'balloonanalogrisktask', None))
    assert (parse_tsv_name('sub-09_task-stopsignal_run-02_events.tsv') ==
            (9, 'stopsignal', 2))


def test_stopsignal():
    for tsv_path in glob(pjoin(NEW_COND_PATH,
                               'sub-*',
                               'func',
                               'sub*stopsignal*.tsv')):
        check_task(tsv_path, OLD_COND_PATH)


def test_er():
    for tsv_path in glob(pjoin(NEW_COND_PATH,
                               'sub-*',
                               'func',
                               'sub*emotionalregulation*.tsv')):
        check_task(tsv_path, OLD_COND_PATH, fail=False)


def test_td():
    for tsv_path in glob(pjoin(NEW_COND_PATH,
                               'sub-*',
                               'func',
                               'sub*discounting*.tsv')):
        check_task(tsv_path, OLD_COND_PATH, fail=False,
                   onset_field='onset_orig')


def test_older_cond_filenames():
    assert older_cond_filenames(1, 'stopsignal', 1) == [
        pjoin('sub001', 'model', 'model001', 'onsets', 'task002_run001',
              'cond%03d.txt' % j) for j in range(1, 5)]


def test_three_column():
    if NEW_COND_PATH is None:
        return
    cond_file = pjoin(NEW_COND_PATH, 'sub-09', 'func',
                      'sub-09_task-stopsignal_run-02_events.tsv')
    df = pd.read_table(cond_file)
    info = TASK_DEFS['stopsignal']
    df = info['preprocessor'](df)
    oda = three_column(df, 'gocorrect')
    assert oda.shape == (96, 3)


def test_tsv2events():
    if NEW_COND_PATH is None:
        return
    cond_file = pjoin(NEW_COND_PATH, 'sub-09', 'func',
                      'sub-09_task-stopsignal_run-02_events.tsv')
    events = tsv2events(cond_file)
    assert len(events) == 4
    assert sorted(events) == ['gocorrect', 'goincorrect', 'stopcorrect',
                              'stopincorrect']


def test_write_all_tasks():
    if NEW_COND_PATH is None:
        return
    # Make a temporary directory
    out_dir = mkdtemp()
    try:
        for to_write in (['stopsignal'], 'all'):
            # Write the files again
            write_all_tasks(NEW_COND_PATH, out_dir, to_write)
            # Check they are the same as the original run, or missing.
            for path in glob(pjoin(NEW_COND_PATH, 'sub-*', 'func', '*.txt')):
                _, fname = psplit(path)
                made_path = pjoin(out_dir, fname)
                sub_no, task_name, run_no = parse_tsv_name(path)
                if to_write != 'all' and task_name not in to_write:
                    assert not exists(made_path)
                continue
                with open(path, 'rt') as fobj:
                    original_contents = fobj.read()
                with open(made_path, 'rt') as fobj:
                    made_contents = fobj.read()
                assert original_contents == made_contents
                remove(made_path)
    finally:
        rmtree(out_dir)


def test_write_all_events():
    # Check write_all_tasks gives error for not-known tasks.
    if NEW_COND_PATH is None:
        return
    with pytest.raises(ValueError) as e_info:
        write_all_tasks(NEW_COND_PATH, 'tmp', ['foo'])
    with pytest.raises(ValueError) as e_info:
        write_all_tasks(NEW_COND_PATH, 'tmp', ['stopsignal', 'foo'])
