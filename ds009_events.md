# Generating the event files

Subjects 1 and 2 for current revision:

```
$ find . -name "sub-*_task*.nii.gz" -exec n_vols.py {} \;
./ds000009_R2.0.3/sub-01/func/sub-01_task-balloonanalogrisktask_bold.nii.gz (64, 64, 34, 245)
./ds000009_R2.0.3/sub-01/func/sub-01_task-discounting_bold.nii.gz (64, 64, 34, 293)
./ds000009_R2.0.3/sub-01/func/sub-01_task-emotionalregulation_run-01_bold.nii.gz (64, 64, 34, 200)
./ds000009_R2.0.3/sub-01/func/sub-01_task-emotionalregulation_run-02_bold.nii.gz (64, 64, 34, 200)
./ds000009_R2.0.3/sub-01/func/sub-01_task-stopsignal_run-01_bold.nii.gz (64, 64, 34, 184)
./ds000009_R2.0.3/sub-01/func/sub-01_task-stopsignal_run-02_bold.nii.gz (64, 64, 34, 184)
./ds000009_R2.0.3/sub-02/func/sub-02_task-balloonanalogrisktask_bold.nii.gz (64, 64, 34, 286)
./ds000009_R2.0.3/sub-02/func/sub-02_task-discounting_bold.nii.gz (64, 64, 34, 293)
./ds000009_R2.0.3/sub-02/func/sub-02_task-emotionalregulation_run-01_bold.nii.gz (64, 64, 34, 200)
./ds000009_R2.0.3/sub-02/func/sub-02_task-emotionalregulation_run-02_bold.nii.gz (64, 64, 34, 200)
./ds000009_R2.0.3/sub-02/func/sub-02_task-stopsignal_run-01_bold.nii.gz (64, 64, 34, 184)
./ds000009_R2.0.3/sub-02/func/sub-02_task-stopsignal_run-02_bold.nii.gz (64, 64, 34, 184)
```

Subject 1 and 2 for original version:

```
$ find . -name bold.nii.gz -exec n_vols.py {} \;
./ds009/sub001/BOLD/task001_run001/bold.nii.gz (64, 64, 34, 245)
./ds009/sub001/BOLD/task002_run001/bold.nii.gz (64, 64, 34, 184)
./ds009/sub001/BOLD/task002_run002/bold.nii.gz (64, 64, 34, 184)
./ds009/sub001/BOLD/task003_run001/bold.nii.gz (64, 64, 34, 200)
./ds009/sub001/BOLD/task003_run002/bold.nii.gz (64, 64, 34, 200)
./ds009/sub001/BOLD/task004_run001/bold.nii.gz (64, 64, 34, 293)
./ds009/sub002/BOLD/task001_run001/bold.nii.gz (64, 64, 34, 286)
./ds009/sub002/BOLD/task002_run001/bold.nii.gz (64, 64, 34, 184)
./ds009/sub002/BOLD/task002_run002/bold.nii.gz (64, 64, 34, 184)
./ds009/sub002/BOLD/task003_run001/bold.nii.gz (64, 64, 34, 200)
./ds009/sub002/BOLD/task003_run002/bold.nii.gz (64, 64, 34, 200)
./ds009/sub002/BOLD/task004_run001/bold.nii.gz (64, 64, 34, 293)
```

* Task 1 (old) is BART
* Task 2 is SS
* Task 3 is ER
* Task 4 is TD

Quotes below are from Jessica's thesis

## Stop-signal (SS) task

This is task 2 in the original onsets.

> For the SS task, the model included events for successful go responses,
> successful stop responses, and unsuccessful stop responses.  Incorrect and
> missed go trials were included in a nuisance regressor. All events began at
> fixation onset and lasted through the duration of the stimulus (1.5
> seconds).

This suggests four event-related regressors.

Indeed there are four condition files in the original onsets.

## Balloon analogue risk-taking (BART) task

Task 1 in the original onsets.

> For the BART, the model included events for inflating the balloon (all but
> the last inflation of each trial), the last inflation before an explosion,
> cashing out, and a balloon explosion. The three response-related events
> began at stimulus onset and lasted the duration of the participant's RT. The
> explosion event began at the time of the explosion and lasted the amount of
> time the exploded balloon was on the screen (2 seconds).

> For the temporal discounting task, the model included events for trials
> predefined as hard choices and trials predefined as easy choices. It also
> included parametric regressors weighting each of those trial types by delay.
> All events began at stimulus onset. The duration of all events was the
> participant's RT on that trial. Nuisance regressors included trials with no
> response (duration 4.5 seconds) and the remainder of each trial itself after
> a decision had been made (4.5 seconds - RT).

> For the emotion regulation task, the model included events for viewing the
> attend instructions, viewing the suppress instructions, viewing the three
> different image types (attend neutral, attend negative, and suppress
> negative), viewing the rating screen, and a de-meaned parametric regressor
> weighted by the participant's response.  All events began at stimulus onset
> and lasted either the duration of the stimulus (1 second for instructions, 5
> seconds for images) or the participant's RT (viewing the rating screen and
> the parametric regressor of the participant's rating).  Missed rating trials
> were included in a nuisance regressor with a duration of 3 seconds. For the
> image regressors, only images rated as 1-3 (all neutral images) or 5-7 (all
> negative images) were included. Three participants had less than two
> instances of at least one of the events and were therefore excluded from the
> analysis.
