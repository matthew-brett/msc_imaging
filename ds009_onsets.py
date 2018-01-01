""" Utilties for writing ds009 3-column event files.

Run with something like:

    python ds009_onsets.py ds000009_R2.0.3 event_file_dir stopsignal

where "ds000009_R2.0.3" is the path containing the subject directories, such as
"sub-01", "event_file_dir" is a directory in which to write the new .txt event
files, and "stopsignal" is the name of an event.

Try:

    python ds009_onsets.py --help

for more information.
"""
from __future__ import print_function
"""
See check_ds009_onsets.py for tests.
"""

from glob import glob
from os import mkdir
from os.path import join as pjoin, split as psplit, isdir, dirname, exists
from argparse import ArgumentParser

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


# Code goes from button number to value on rating scale.  Reverse engineered
# from the original rating_par_orig field.
ER_RESPONSE_MAP = {'114': 4, '103': 3, '121': 2, '98': 1, '0': 0,
                   'n/a': np.nan}

def er_preprocessor(df):
    """ Process dataframe for ER trial types """
    onset, duration, trial_type, image_type, response, rt = [
        df[name].copy() for name in
        ['onset', 'duration', 'trial_type', 'image_type',
         'response', 'reaction_time']]
    # Recode the response values using the map above.
    response = response.map(ER_RESPONSE_MAP)
    tt = trial_type.copy()  # A pandas series
    tt[(trial_type == 'attend') & (image_type == 'negative')] = 'attendneg'
    tt[(trial_type == 'attend') & (image_type == 'neutral')] = 'attendneu'
    tt[(trial_type == 'suppress') & (image_type == 'negative')] = 'suppressneg'
    assert not any((trial_type == 'suppress') & (image_type == 'neutral'))
    tt[(trial_type == "rate") & (response == 0)] = 'ratemiss'
    tt[(trial_type == "rate") & (response != 0)] = 'rate'
    # Use RTs as durations for rate
    good_rates = tt == 'rate'
    # Foo
    duration[good_rates] = pd.to_numeric(rt[good_rates])
    # Make main set of events (excluding parametric regressor)
    amplitude = pd.Series(np.ones(len(df)), name='amplitude')
    main_trials = pd.concat([tt, onset, duration, amplitude], axis=1)
    # Add parametric trial type
    good_onsets = onset[good_rates]
    good_durations = duration[good_rates]
    good_responses = response[good_rates]
    amp_extra = good_responses - np.mean(good_responses)
    amp_extra.name = 'amplitude'
    tt_extra = tt[good_rates]
    tt_extra[:] = 'ratepar'
    # Put the new trials at the end
    extra = pd.concat([tt_extra, good_onsets, good_durations, amp_extra],
                      axis=1)
    return pd.concat([main_trials, extra], axis=0, ignore_index=True)


TASK_DEFS = dict(
    balloonanalogrisktask=dict(old_no=1,
                               preprocessor=bart_preprocessor,
                               conditions= ['inflate', 'beforeexplode',
                                            'cashout', 'explode'],
                               ok = True,  # Set False to disable processing
                               ),
    stopsignal=dict(old_no=2,
                    preprocessor=ss_preprocessor,
                    conditions=['gocorrect', 'stopcorrect',
                                'stopincorrect', 'goincorrect'],
                    ok = True,  # Set False to disable processing
                    ),
    emotionalregulation=dict(old_no=3,
                             preprocessor=er_preprocessor,
                             conditions=['attendneg', 'attendneu',
                                         'rate',
                                         'ratepar',
                                         'suppressneg',
                                         'ratemiss',
                                        ],
                             ok = True,  # Set True to enable processing
                             ),
    discounting=dict(old_no=4,
                     preprocessor=None,
                     conditions=[],
                     ok = False,  # Set True to enable processing
                     )
)

# Throw away incomplete TASK_DEFS (where field 'ok' is not True).
TASK_DEFS = {name: task_def for name, task_def in TASK_DEFS.items()
             if task_def.get('ok')}


def parse_tsv_name(tsv_path):
    """ Parse tsv file name, return subject no, task name, run_no

    Parameters
    ----------
    tsv_path : str
        .tsv filename.

    Returns
    -------
    subject_no : str
        E.g. "sub-12"
    task_name : str
        E.g. "stopsignal"
    run_no : None or int
        None if no run number specified, otherwise a 1-based integer giving the
        run number, where 1 is the first run.
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
    """ Return 3-column onset, duration, amplitude data frame for event `name`
    """
    ons_dur_amp = df[df['trial_type'] == name]
    return ons_dur_amp[['onset', 'duration', 'amplitude']].values


def tsv2events(tsv_path):
    """ Return dictionary of 3-column event dataframes from `tsv_path`
    """
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    if task_name not in TASK_DEFS:  # Task not properly defined
        return {}
    info = TASK_DEFS[task_name]
    df = pd.read_table(tsv_path)
    if info['preprocessor']:
        df = info['preprocessor'](df)
    return {name: three_column(df, name) for name in info['conditions']}


def write_task(tsv_path, out_path=None):
    """ Write .txt event files for .tsv event definitions

    Parameters
    ----------
    tsv_path : str
        Path to .tsv file.
    out_path : None or str
        If str, directory to write output .txt files.  If None, use directory
        containing the .tsv file in `tsv_path`.
    """
    sub_no, task_name, run_no = parse_tsv_name(tsv_path)
    events = tsv2events(tsv_path)
    if len(events) == 0:
        return
    tsv_dir, fname = psplit(tsv_path)
    path = tsv_dir if out_path is None else out_path
    run_part = '' if run_no is None else '_run-%02d' % run_no
    fname_prefix = pjoin(
        path,
        'sub-%02d_task-%s%s_label-' % (sub_no, task_name, run_part))
    for name in events:
        new_fname = fname_prefix + name + '.txt'
        oda = events[name]
        if len(oda):
            print('Writing from', tsv_path, 'to', new_fname)
            np.savetxt(new_fname, oda, '%f', '\t')


def write_all_tasks(start_path, out_path=None, event_names='all'):
    """ Write .txt event files for all tasks with defined processing.

    Parameters
    ----------
    start_path : str
        Path containing subject directories such as ``sub-01`` etc.
    out_path : None or str, optional
        If str, directory to write output .txt files.  If None, use directory
        containing the .tsv file, found by searching in `start_path`.
    event_names : list or "all", optional
        List of event names to process.  If string "all", process all known
        event names.
    """
    event_names = list(TASK_DEFS) if event_names == 'all' else event_names
    strange_events = set(event_names).difference(TASK_DEFS)
    if len(strange_events):
        raise ValueError("One or more event names without processors: " +
                           ', '.join(strange_events))
    for tsv_path in glob(pjoin(start_path,
                               'sub-*',
                               'func',
                               'sub*tsv')):
        sub_no, task_name, run_no = parse_tsv_name(tsv_path)
        if task_name in event_names:
            write_task(tsv_path, out_path)


def main():
    # Process the command-line arguments to the script.
    parser = ArgumentParser(description="Write event files for ds009")
    parser.add_argument('data_dir',
                        help='Directory containing subject directories')
    parser.add_argument('out_dir', default=None, nargs='?',
                        help='Directory in which to write event files '
                        '(default is to write to same directory as .tsv file)')
    parser.add_argument('event_name', default='all', nargs='*',
                        help='Name(s) of events to write (can have more than '
                        'one, separated by spaces)')
    args = parser.parse_args()
    # Create the output directory if it does not exist.
    if args.out_dir is not None and not exists(args.out_dir):
        mkdir(args.out_dir)
    # Write the files
    write_all_tasks(args.data_dir, args.out_dir, args.event_name)


if __name__ == '__main__':
    # This code gets run if this Python file gets executed as a script.
    # It does not get run if the file is just imported.
    # https://stackoverflow.com/a/419185
    main()
