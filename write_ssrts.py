""" Write mean-corrected SSRTs for higher-level analysis
"""
from __future__ import division

from glob import glob
from os.path import join as pjoin, basename

import numpy as np
import pandas as pd


DATA_SDIR = 'ds000009_R2.0.3'


def get_old_ssrts():
    # Read SSRT from `participants.tsv` file.
    #
    # File is part of revision 2.0.3 of the "Metadata and MRIQC" archive at
    # https://openfmri.org/dataset/ds000009/
    subjects = pd.read_table('ds009_participants.tsv')
    return subjects['m_SSRTquant'].values


def test_ssrts():
    # Check old against calculated SSRTS
    old_ssrts = get_old_ssrts()
    ssrts = [ssrt for path, ssrt in SSRTS]
    assert np.corrcoef(ssrts, old_ssrts)[0, 1] >= 0.94


def get_gos_ssd(df):
    """ Get data for calculation of SSRT from FMRI events

    Parameters
    ----------
    df : data frame
        Event data for FMRI run.

    Returns
    -------
    stop_corrects : int
        Number of correct stops.
    stop_incorrects : int
        Number of incorrect stops (go when stop requested)
    go_rts : array
        Reaction times for correct go trials.
    ssds : array
        All non-zero Stop Signal Delays.
    """
    trial_type, rt, arrow, button, button_code, ssd = [
        df[name] for name in
        ['trial_type', 'ReactionTime',
         'PresentedStimulusArrowDirection',
         'SubjectResponseButton',
         'SubjectResponseButtonCode',
         'StopSignalDelay'
        ]]
    stop_corrects = sum((trial_type == "STOP") & (button_code == 0))
    stop_incorrects = sum((trial_type == "STOP") & (button_code != 0))
    go_corrects = (trial_type == 'GO') & (arrow == button)
    return stop_corrects, stop_incorrects, rt[go_corrects].values, ssd[ssd > 0].values


def ssrt(df1, df2):
    """ Calculate SSRT from data frames of two FMRI event files
    """
    sc1, si1, rts1, ssds1 = get_gos_ssd(df1)
    sc2, si2, rts2, ssds2 = get_gos_ssd(df2)
    n_correct = sc1 + sc2
    p_correct = n_correct / (n_correct + si1 + si2)
    all_rts = np.concatenate([rts1, rts2], axis=0)
    rt_quantile = np.percentile(all_rts, p_correct * 100)
    mean_ssd = np.mean(np.concatenate([ssds1, ssds2], axis=0))
    # Return results in milliseconds
    return (rt_quantile - mean_ssd) * 1000


def get_ssrts(data_root):
    """ Calculate SSRTs per subject
    """
    ssrts = []
    ss_file_glob = 'sub-*_task-stopsignal_run-*_events.tsv'
    for sub_path in glob(pjoin(data_root, 'sub-*')):
        dfs = []
        for tsv_path in sorted(glob(pjoin(sub_path, 'func', ss_file_glob))):
            dfs.append(pd.read_table(tsv_path))
        ssrts.append((basename(sub_path), ssrt(*dfs)))
    return ssrts


# Calculate the SSRTs for each subject
SSRTS = get_ssrts(DATA_SDIR)


def main():
    # Write mean-corrected SSRT value
    ssrts = [ssrt for path, ssrt in SSRTS]
    mean_ssrt = np.mean(ssrts)
    with open('ssrts.tsv', 'wt') as fobj:
        for sub_no, ssrt in SSRTS:
            fobj.write('{}\t{:0.2f}\n'.format(sub_no, ssrt - mean_ssrt))
    # Check the correlation against the old values still holds
    written = pd.read_table('ssrts.tsv', header=None)
    old_ssrts = get_old_ssrts()
    assert np.corrcoef(written[[1]].values.ravel(), old_ssrts.ravel())[0, 1] > 0.94


if __name__ == '__main__':
    main()
