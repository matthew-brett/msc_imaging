---
output:
  pdf_document: default
  documentclass: report
  papersize: a4
  html_document:
    df_print: paged
---

# Fundamentals in brain imaging methods, assessment B

The assessment for this module has two parts: Part A and Part B. You must
complete both parts. This information is for part B only.

## Introduction

We designed this assessment to give you some experience of:

* replicating a published experiment;
* writing up your analysis in a way that can be easily replicated by others;

These skills are useful to you because a typical imaging experiment involves
replicating an existing experiment to make sure you can find the effect that
you want to study, and then writing up your study so that your reviewers and
readers can check and use your work.

## Introduction to the task

If you log onto the PBIC server, you will find you have a folder:

```
/home/people/xxx/replication
```

where `xxx` is your University of Birmingham ADF username.

Inside that folder you will find a symbolic link:

```
/home/people/xxx/replication/data
```

The link points to a read-only directory, with a copy of the OpenFMRI data.
The data are a slightly expanded version of the DS009 OpenFMRI dataset:

https://openfmri.org/dataset/ds000009

You will also find a near-empty text file:

```
/home/people/xxx/replication/README.txt
```

When you have finished the assignment, you will have filled out that file with
all the instructions necessary for someone else to replicate your analysis.
The specific "Someone else" will be us, your instructors.

We highly recommend that you edit the `README.txt` file, but if you prefer,
you can also record the instructions in a Word file, which should be called:

```
/home/people/xxx/replication/README.docx
```

If you do use a Word file instead of the `README.txt` file, please copy the
current contents of the `README.txt` file to the Word document, and delete the
`README.txt` file.  If we find both, we will assume you meant us to read the
Word document.

## Introduction to the dataset

The version you have here is revision 2.0.3 of the DS009 dataset (see the
dataset web page for details).

The first author of the relevant publication is Jessica Cohen, who is now at
the University of North Carolina: http://cohenlab.web.unc.edu/

The OpenFMRI web page points you to the methods write-up for the study at:

https://openfmri.org/media/ds000009/ds009_methods_0_CchSZHn.pdf

There is a copy of that document in the data folder.

The web page also points you to the canonical write-up of this experiment,
which is Cohen's PhD thesis.  You can get that by following the links on the
page, and logging in through your UoB sign-in, but for your convenience, the
data folder has a copy at `jrcohen_dissertation.pdf`.

The experiment you have here is the one that Cohen describes in chapter 4 of
her thesis. The chapter title is "The neural basis of self-control"; it is on
page 53 as numbered, page 74 in the PDF.  As far as I can see, the methods
document above is a better-quality reproduction of the methods section in
chapter 4 of the thesis. The thesis chapter contains the description of their
FMRI analysis, but we have reproduced that section of the thesis below.

## Overview of the task

Your job is to reproduce the activation maps for two of the four main effects
of the four tasks, as described in figure 4.5 of the thesis chapter, and
tables 4.2 through 4.3.

The two behavioural tasks, and associated "main effects" are:

* Stop-Signal (SS) task / successful stop - go;
* Balloon Analogue Risk Task (BART) / cashing out - inflating the balloon;

You are also welcome to analyze the other two tasks, but they need some
statistical techniques that we have not covered in the lectures or practicals:

* Temporal Discounting (TD) task / difficult trials varying parametrically
  with delay;
* Emotion Regulation (ER) task / activity for "suppress negative" trials
  with positive regression against self-reported regulation.

You can earn *extra marks* by analyzing these last two experiments (see
below).  If you analyze these experiments, you will need to do some extra
reading / ask for extra help - which we are very happy to provide.

In order to replicate the two main effects (SS and BART), you should repeat
their analysis as exactly as you can, with a few exceptions, noted below.

In the following paragraphs, we have reproduced the FMRI analysis section
(4.2.5) from Cohen's thesis.  You will see the exceptions in our annotations
labeled with "FBI annotation:"

> Imaging data were processed and analyzed using FSL 4.1 (FMRIB's Software
> Library, www.fmrib.ox.ac.uk/fsl). Steps included BET to extract the brain
> from the skull and McFLIRT for motion correction. Statistical analysis was
> conducted using FEAT 5.98.

FBI annotation: you will be using the versions of FSL and FEAT that are
currently on the cluster.

> The statistical models varied depending on the task. For the SS task, the
> model included events for successful go responses, successful stop
> responses, and unsuccessful stop responses.  Incorrect and missed go trials
> were included in a nuisance regressor. All events began at fixation onset
> and lasted through the duration of the stimulus (1.5 seconds). For the BART,
> the model included events for inflating the balloon (all but the last
> inflation of each trial), the last inflation before an explosion, cashing
> out, and a balloon explosion. The three response-related events began at
> stimulus onset and lasted the duration of the participant's RT. The
> explosion event began at the time of the explosion and lasted the amount of
> time the exploded balloon was on the screen (2 seconds).

FBI annotation: we have prepared the event onset files for you, with one file
for each of these event types.  You will find these files in the subject
`func` directories (see below).  The files are in "Custom 3 column format" \-
see the [FEAT user
guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide) for more
information.

FBI annotation: the following description is for tasks you do not need to
analyze for this assessment (but you can analyze for extra marks):

> For the temporal discounting task, the model included events for trials
> predefined as hard choices and trials predefined as easy choices. It also
> included parametric regressors weighting each of those trial types by delay.
> All events began at stimulus onset. The duration of all events was the
> participant's RT on that trial. Nuisance regressors included trials with no
> response (duration 4.5 seconds) and the remainder of each trial itself after
> a decision had been made (4.5 seconds - RT). For the emotion regulation
> task, the model included events for viewing the attend instructions, viewing
> the suppress instructions, viewing the three different image types (attend
> neutral, attend negative, and suppress negative), viewing the rating screen,
> and a de-meaned parametric regressor weighted by the participant's response.
> All events began at stimulus onset and lasted either the duration of the
> stimulus (1 second for instructions, 5 seconds for images) or the
> participant's RT (viewing the rating screen and the parametric regressor of
> the participant's rating).  Missed rating trials were included in a nuisance
> regressor with a duration of 3 seconds. For the image regressors, only
> images rated as 1-3 (all neutral images) or 5-7 (all negative images) were
> included. Three participants had less than two instances of at least one of
> the events and were therefore excluded from the analysis.

FBI annotation: the following applies to all four tasks, and therefore to the two
tasks in this assessment.

> For the first level analysis, images were spatially smoothed using a
> Gaussian kernel of FWHM 5 mm. Time-series statistical analysis was carried
> out using FILM (FMRIBs Improved Linear Model) with local autocorrelation
> correction after highpass temporal filtering (Gaussian-weighted
> least-squares straight line fitting with sigma = 33.0s). Regressors of
> interest were created by convolving a delta function representing each event
> of interest with a canonical (double- gamma) hemodynamic response function
> (Woolrich et al., 2001).

FBI annotation: the next sentence applies only to the TD experiment, which is
not part of your assessment:

> Parametric regressors were created by modulating the amplitude of a delta
> function using a demeaned version of the parameter of interest.

FBI annotation: the following sentence does apply to all experiments:

> In addition to regressors of interest, estimated motion parameters and their
> temporal derivatives (i.e., displacement) were included as nuisance
> regressors.  Linear contrasts were performed for comparisons of interest.

FBI annotation: the 3-step registration method below is somewhat complicated.
We will give you 5 *extra marks* if you implement it (see below), but you can
also get full ordinary marks (see below) by doing the standard registration of
the EPI functional images to the matching structural images, as you have been
taught in the workshops.

> A 3-step registration process was applied using FSL's FNIRT module for
> nonlinear registration. EPI functional images were first registered linearly
> to an inplane T2-weighted structural image (matched bandwidth; 7 DOF). The
> inplane structural image was registered linearly to the high-resolution
> structural image (MPRage; 7 DOF), and the high-resolution image was
> registered to standard MNI152 space using nonlinear registration with 12
> degrees of freedom (warp resolution 10 mm). These transformation matrices
> were combined to provide the transform from EPI to MNI space, and this
> transform was applied to the results from the first-level analysis.

> For the two tasks that had more than one run (SS and ER), data were combined
> across the two runs using a fixed effects model, and then modeled using
> mixed effects at the group level with FSL's FLAME model (Stage 1 only). The
> model for each task included a regressor modeling mean activity and demeaned
> regressors for SSRT (SS), number of pumps (BART), k (TD), and amount of
> reported regulation (ER). Outlier deweighting was performed using a mixture
> modeling approach (Woolrich, 2008).

FBI annotation: see the FEAT user manual for details of the options above:
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide

> Results were thresholded at a whole-brain level using cluster-based Gaussian
> random field theory, with a cluster-forming threshold of z > 2.3 and a
> whole-brain corrected cluster significance level of p < .05 unless otherwise
> noted in the text.

FBI annotation: the following paragraph completes the FMRI analysis methods
description, but does not apply to your task in this assessment.

> Results of the ROI analysis were thresholded within that ROI using a
> threshold-free cluster enhancement method (TFCE; S. M. Smith & Nichols,
> 2009) and a corrected significance level of p <.05 unless otherwise noted.
> The conjunction analysis found areas that were significantly active within
> that ROI for at least two of the tasks. Cortical surface renderings were
> performed using CARET software (http://brainmap.wustl.edu). Group
> statistical maps were mapped to the Population Average Landmark and
> Surface-based (PALS) atlas using the multifiducial mapping technique
> described by Van Essen (Van Essen, 2005).  For the purposes of presentation,
> data are overlaid on the average atlas surface.

## The data format

Your friendly OpenFMRI team has arranged the data in the standard BIDS format:
http://bids.neuroimaging.io

In this particular case this means that each subject has a directory structure
like this:

```
sub-01
|-- anat
|   |-- sub-01_inplaneT2.json
|   |-- sub-01_inplaneT2.nii.gz
|   |-- sub-01_T1w.json
|   `-- sub-01_T1w.nii.gz
|-- dwi
|   |-- sub-01_dwi.bval
|   |-- sub-01_dwi.bvec
|   |-- sub-01_dwi.json
|   `-- sub-01_dwi.nii.gz
|-- func
|   |-- sub-01_task-balloonanalogrisktask_bold.json
|   |-- sub-01_task-balloonanalogrisktask_bold.nii.gz
|   |-- sub-01_task-balloonanalogrisktask_events.tsv
|   |-- sub-01_task-discounting_bold.json
|   |-- sub-01_task-discounting_bold.nii.gz
|   |-- sub-01_task-discounting_events.tsv
|   |-- sub-01_task-emotionalregulation_run-01_bold.json
|   |-- sub-01_task-emotionalregulation_run-01_bold.nii.gz
|   |-- sub-01_task-emotionalregulation_run-01_events.tsv
|   |-- sub-01_task-emotionalregulation_run-02_bold.json
|   |-- sub-01_task-emotionalregulation_run-02_bold.nii.gz
|   |-- sub-01_task-emotionalregulation_run-02_events.tsv
|   |-- sub-01_task-stopsignal_run-01_bold.json
|   |-- sub-01_task-stopsignal_run-01_bold.nii.gz
|   |-- sub-01_task-stopsignal_run-01_events.tsv
|   |-- sub-01_task-stopsignal_run-02_bold.json
|   |-- sub-01_task-stopsignal_run-02_bold.nii.gz
|   `-- sub-01_task-stopsignal_run-02_events.tsv
`-- sub-01_scans.tsv
```

For each subject, you will need the anatomical T1 file at
`anat/sub-XX_T1w.nii.gz` and the functional files in the `func` directory.
The ``.nii.gz`` files are the 4D EPI FMRI runs, and the `.tsv` files give full
details about all events during the runs.  You will also find event files for
each event named in the corresponding FMRI analysis methods section above (not
shown in the listing).

You'll find the scanning parameters, such as the Time to Repeat (TR) in the
files ending in `_bold.json`.

## Your report

For your assessment, you should:

1.  Fill in the README.txt / README.docx file with a detailed guide to
    repeating all the steps in your analysis.  Reference or quote the thesis
    methods section, as we have above, for example:

    "I ran the FEAT analysis tool, and chose the option to coregister the EPI
    functional scan `sub-XX/func/sub-XX_task-balloonanalogrisktask_bold.nii.gz`
    to the anatomical T1 scan `sub-XX/sub-01_T1w.nii.gz`. This was in order to
    replicate (in part) the following from the thesis method section "A 3-step
    registration process was applied using FSL's FNIRT module for nonlinear
    registration. EPI functional images were first registered linearly to an
    inplane T2-weighted structural image (matched bandwidth; 7 DOF). The
    inplane structural image was registered linearly to the high-resolution
    structural image (MPRage; 7 DOF) ... "

    At each step, point to the output result folders in your
    `/home/people/xxx/replication` folder.

    We will grade this report out of 60 on the following criteria:

    *   Is the description of what you did clear? 15 marks.
    *   Have you justified all the steps of your analysis?  10 marks.
    *   Did you make any analysis errors? 20 marks.
    *   How easy is it to exactly replicate your analysis (whether right or
        wrong)? You will get maximum marks if we can run a script to replicate
        the analysis given only the raw data that you have linked at
        `/home/people/xxx/replication/data` along with any script files or
        library code in your directory. 15 marks.

2.  In your report you should give the location of these specific files:

     1. The activation (t-statistic) map for the "main effect" contrast for the
        SS task (as defined above, and in the thesis FMRI methods). 10 marks,
        see below.
     1. The thresholded z-statistic map for the "main effect" contrast for the
        SS task (with 0 in voxels in areas below threshold and valid z scores
        in voxels in areas above threshold). 5 marks, see below.
     1. The activation (t-statistic) map for the "main effect" contrast for the
        BART task (as defined above, and in the thesis FMRI methods). 10 marks.
     1. The thresholded z-statistic map for the "main effect" contrast for the
        BART task (with 0 in voxels in areas below threshold and valid z scores
        in voxels in areas above threshold). 5 marks.

    We will mark each image for approximate correspondence to the correct map,
    as generated from our own analysis of the same data.

3.  Can you identify voxels that have a statistically convincing effect (as
    defined by the thresholding described above) for *both* of the SS and BART
    tasks.  For this, we would like to see an image where there are zeros in
    voxels which are activated by only one or neither task, and non-zeros in
    voxels activated by both tasks.  Hint: you may want to investigate the
    `fslmaths` tool.  Point us to this image in your report. 10 marks.

## Extra marks

There are 100 ordinary marks available (marks above not labeled as "extra"),
and 25 extra marks available.  Your final score will be your ordinary marks
plus your extra marks, with a maximum total of 100. For example, if you earn
85 ordinary marks, and 25 extra marks you will get 100. If you earn 60
ordinary marks and 15 extra marks you will get 75.

## Submission

**Submission is automatic at noon January 8th**

At noon on January 8th, we will make a read-only copy of your directory
`/home/people/xxx/replication`. So, *before 12:00 of January 8th* make sure
that:

*   the `README.txt` / `README.docx` files are up to date;
*   all the analyses comprising the replication have been run inside that
    folder, and the results files referred to in the README file are available
    for your instructors to look at.
