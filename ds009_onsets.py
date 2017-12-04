""" Utilties for working with ds009 onsets
"""

import numpy as np

def query2ons_dur(df, query):
    ons_dur = np.atleast_2d(df.query(query)[['onset', 'duration']])
    return np.column_stack((ons_dur, np.ones(len(ons_dur))))


def get_ss_go_correct(df):
    return query2ons_dur(df,
        'trial_type=="GO" & '
        'PresentedStimulusArrowDirection==SubjectResponseButton')


def get_ss_stop_correct(df):
    return query2ons_dur(df,
        'trial_type=="STOP" & '
        'SubjectResponseButtonCode==0')


def get_ss_stop_incorrect(df):
    return query2ons_dur(df,
        'trial_type=="STOP" & '
        'SubjectResponseButtonCode!=0')


def get_ss_go_incorrect(df):
    return query2ons_dur(df,
        'trial_type=="GO" & '
        'PresentedStimulusArrowDirection!=SubjectResponseButton')


TASK_DEFS = dict(
    balloonanalogrisktask=dict(old_no=1,
                               preprocessor=None,
                               conditions=(
                                   ('go_correct', get_ss_go_correct),
                                   ('stop_correct', get_ss_stop_correct),
                                   ('stop_incorrect', get_ss_stop_incorrect),
                                   ('go_incorrect', get_ss_go_incorrect)
                               )),
    stopsignal=dict(old_no=2,
                    preprocessor=None,
                    conditions=(
                        ('go_correct', get_ss_go_correct),
                        ('stop_correct', get_ss_stop_correct),
                        ('stop_incorrect', get_ss_stop_incorrect),
                        ('go_incorrect', get_ss_go_incorrect)
                    )),
    emotionalregulation=dict(old_no=3,
                             preprocessor=None,
                             conditions=(
                             )),
    discounting=dict(old_no=4,
                     preprocessor=None,
                     conditions=(
                     ))
)


def parse_tsv(tsv_name):
    """ Parse tsv file name, return subject no, task name, run_no
    """
    parts = tsv_name.split('_')
    if len(parts) == 3:
        run_no = 1  # run_no 1 is implied if omitted
    else:
        run_parts = parts.pop(2).split('-')
        assert run_parts[0] == 'run'
        run_no = int(run_parts[1])
    sub_parts = parts[0].split('-')
    assert sub_parts[0] == 'sub'
    sub_no = int(sub_parts[1])
    task_name = parts[1].split('-')[1]
    return sub_no, task_name, run_no



def test_parse_tsv():
    assert (parse_tsv('sub-01_task-stopsignal_run-01_events.tsv') ==
            (1, 'stopsignal', 1))
    assert (parse_tsv('sub-13_task-balloonanalogrisktask_events.tsv') ==
            (13, 'balloonanalogrisktask', 1))
    assert (parse_tsv('sub-09_task-stopsignal_run-02_events.tsv') ==
            (9, 'stopsignal', 2))


