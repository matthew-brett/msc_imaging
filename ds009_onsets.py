""" Utilties for working with ds009 onsets
"""
from __future__ import print_function

from glob import glob

from os.path import join as pjoin, split as psplit, isdir, dirname
import numpy as np

import pandas as pd


# Where to look for condition files
NEW_COND_PATH=None
if isdir('ds000009_R2.0.3'):
    NEW_COND_PATH = pjoin(dirname(__file__), 'ds000009_R2.0.3')
elif isdir('sub-01'):
    NEW_COND_PATH = dirname(__file__)


def bart_preprocessor(df):
    """ Process dataframe for BART trial types """
    before_explode = np.zeros(len(df), dtype=bool)
    action = df['action']
    explodes = action == 'EXPLODE'
    before_explode[:-1] = explodes[1:]
    trial_type = action.apply(str.lower)
    trial_type[trial_type == 'accept'] = 'inflate'
    trial_type[before_explode] = 'beforeexplode'
    duration = df['reaction_time'].copy()
    duration[explodes] = 2
    amplitude = pd.Series(np.ones(len(df)))
    classified = pd.concat([trial_type, df['onset'], duration, amplitude],
                           axis=1)
    classified.columns = ['trial_type', 'onset', 'duration', 'amplitude']
    return classified


def ss_preprocessor(df):
    """ Process dataframe for SS trial types """
    trial_type_orig, onset, duration, arrow, button, button_code = [
        df[name] for name in
        ['trial_type', 'onset', 'duration',
         'PresentedStimulusArrowDirection',
         'SubjectResponseButton',
         'SubjectResponseButtonCode']]
    trial_type = trial_type_orig.copy()
    trial_type[(trial_type_orig == 'GO') & (arrow == button)] = 'gocorrect'
    trial_type[(trial_type == "STOP") & (button_code == 0)] = 'stopcorrect'
    trial_type[(trial_type == "STOP") & (button_code != 0)] = 'stopincorrect'
    trial_type[(trial_type_orig == 'GO') & (arrow != button)] = 'goincorrect'
    amplitude = pd.Series(np.ones(len(df)), name='amplitude')
    return pd.concat([trial_type, onset, duration, amplitude], axis=1)


TASK_DEFS = dict(
    balloonanalogrisktask=dict(old_no=1,
                               preprocessor=bart_preprocessor,
                               conditions= ['inflate', 'beforeexplode',
                                            'cashout', 'explode'],
                               ),
    stopsignal=dict(old_no=2,
                    preprocessor=ss_preprocessor,
                    conditions=['gocorrect', 'stopcorrect',
                                'stopincorrect', 'goincorrect']
                    ),
    emotionalregulation=dict(old_no=3,
                             preprocessor=None,
                             conditions=[],
                             ),
    discounting=dict(old_no=4,
                     preprocessor=None,
                     conditions=[],
                     )
)


def parse_tsv_name(tsv_path):
    """ Parse tsv file name, return subject no, task name, run_no
    """
    path, fname = psplit(tsv_path)
    parts = fname.split('_')
    if len(parts) == 3:
        run_no = None
    else:
        run_parts = parts.pop(2).split('-')
        assert run_parts[0] == 'run'
        run_no = int(run_parts[1])
    sub_parts = parts[0].split('-')
    assert sub_parts[0] == 'sub'
    sub_no = int(sub_parts[1])
    task_name = parts[1].split('-')[1]
    return sub_no, task_name, run_no


def three_column(df, name):
    ons_dur_amp = df[df['trial_type'] == name]
    return ons_dur_amp[['onset', 'duration', 'amplitude']].values


def tsv2events(tsv_path):
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    info = TASK_DEFS[task_name]
    if len(info['conditions']) == 0:
        return {}
    df = pd.read_table(tsv_path)
    if info['preprocessor']:
        df = info['preprocessor'](df)
    return {name: three_column(df, name) for name in info['conditions']}


def write_task(tsv_path):
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    events = tsv2events(tsv_path)
    if len(events) == 0:
        return
    path, fname = psplit(tsv_path)
    run_part = '' if run_no is None else '_run-%02d' % run_no
    fname_prefix = pjoin(
        path,
        'sub-%02d_task-%s%s_label-' % (sub_no, task_name, run_part))
    for name in events:
        new_fname = fname_prefix + name + '.txt'
        print('Writing', tsv_path, 'to', new_fname)
        oda = events[name]
        if len(oda):
            np.savetxt(new_fname, oda, '%f', '\t')


def write_all_tasks(start_path):
    for tsv_path in glob(pjoin(start_path,
                               'sub-*',
                               'func',
                               'sub*tsv')):
        write_task(tsv_path)


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
