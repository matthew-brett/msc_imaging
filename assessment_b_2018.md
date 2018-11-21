---
output:
  pdf_document: default
  documentclass: report
  papersize: a4
  html_document:
    df_print: paged
---

# 2018 fundamentals in brain imaging methods, assessment B

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
The data are a slightly modified version of the DS107 OpenNeuro / OpenFMRI dataset:

https://openneuro.org/datasets/ds000107

You will also find a near-empty text file:

```
/home/people/xxx/replication/README.txt
```

When you have finished the assignment, you will have filled out that file with
all the instructions necessary for someone else to replicate your analysis. The
specific "Someone else" will be us, your instructors.

We highly recommend that you edit the `README.txt` file, but if you prefer, you
can also record the instructions in a Word file, which should be called:

```
/home/people/xxx/replication/README.docx
```

If you do use a Word file instead of the `README.txt` file, please copy the
current contents of the `README.txt` file to the Word document, and delete the
`README.txt` file.  If we find both, we will assume you meant us to read the
Word document.

## Introduction to the dataset

The version you have here is a slightly modified version of revision `v00001`
of the DS107 dataset (see the dataset web page for details).

The first author of the relevant publication is Keith Duncan, who has now left
academia, but the senior author is [Professor Joe
Devlin](https://www.ucl.ac.uk/pals/people/joe-devlin), who is still at UCL,
and, most generously, is still answering our emails about this dataset.

The OpenNeuro web page points you to the paper reporting the results:

Duncan, K.J., Pattamadilok, C., Knierim, I., Devlin, J.T. (2009). Consistency
and variability in functional localisers. Neuroimage, 46(4):1018-26. doi:
10.1016/j.neuroimage.2009.03.014.  Download the full text from
<https://www.sciencedirect.com/science/article/pii/S1053811909002353>.

## Overview of the task

Your job is to reproduce the results from the Duncan *et al* paper, from the original data in the ds107 dataset.

Duncan *et al* did two FMRI runs on each of 49 subjects.  The runs had the same
conditions, but in different order.  The conditions were blocks of stimuli,
presented at one second intervals.  For all conditions, the subject's task was
to press a button if the stimulus just presented was the same as the previous
stimulus (a [1-back](https://en.wikipedia.org/wiki/N-back) task).  There were four conditions, that differed in the type of stimuli presented.  These were:

1. pictures of objects (OBJECTS);
1. scrambled pictures of objects (SCRAMBLED);
1. words (WORDS);
1. consonant strings (STRINGS).

In between some of these blocks there were periods of rest (REST).

Duncan *et al* were interested in the activation for these subtractions:

1. OBJECTS - SCRAMBLED;
1. WORDS - REST.

They expected OBJECTS - SCRAMBED to activate the "lateral occipital complex" in
the lateral Occipital Temporal Cortex (OTC).

They expected WORDS - REST to activate the "visual word form area" in
the ventral OTC, although they disagree with the name "visual word form area".

Their further interest was to look at the variation in the voxels identified as
activated in these regions, across runs.  The point here was that, if there was a lot of variation, then people using tasks like this, to identify these regions, would have to be more careful in their analysis and conclusions.

The results that you need to replicate are:

*   Behavioral data analysis for the 1-back tasks, including d-prime scores and
    reaction times (see table 1 of the paper);
*   Group analysis whole brain activation map for OBJECTS - SCRAMBLED;
*   Group analysis whole brain activation map for WORDS - REST;
*   For each of (OBJECTS \- SCRAMBLED activation in lateral OTC) and (WORDS
    \- REST activation in ventral OTC):
    *   Between-subject variability in coordinates of peak activation (see table 2);
    *   Within subject (across run) variability of:
        *   Peak voxel coordinates (Euclidean distance);
        *   "Ratio of commonly activated voxels" at different Z thresholds
            (1\.64, 2\.3, 3\.09, 4\.0) (figure 3A);
        *   (For extra marks) "Ratio of commonly activated voxels" at
            Z thresholds above, for regions defined by activated voxels within
            9mm of peak (figure 3B).

Duncan *et al* restricted their search for activated voxels to gray matter, by segmenting the subjects' structural images into gray- and white-matter, and masking out the white-matter voxels.  You do not need to do this, but if you do, we will give you extra marks.

If you do the analyses for extra marks, you will need to do some extra reading
/ ask for extra help - which we are very happy to provide.

In order to replicate the two main effects (OBJECTS-SCRAMBLED and WORDS-REST),
you should repeat their analysis as exactly as you can.

In the following paragraphs, we have reproduced sections from the methods
section of the Duncan *et al* paper. You will see the exceptions in our
annotations labeled with "FBI annotation:"

> Data processing was carried out using FSL 4.0 (www.fmrib.ox.ac. uk/fsl).

FBI annotation: you will be using the versions of FSL and FEAT that are
currently on the cluster.

> To allow for T1 equilibrium, the initial two images of each run were
> discarded.

FBI annotation: the experimenters have already dropped the two dummy volumnes
from the image files in the ds107 dataset, so the first volume in each FMRI run, in the data you have, is the first not-dummy scan.

> The data were then realigned to remove small head movements
> (Jenkinson et al., 2002), smoothed with a Gaussian kernel of FWHM 6 mm, and
> pre-whitened to remove temporal auto- correlation (Woolrich et al., 2001).


> The resulting images were entered into a general linear model with four
> conditions of interest corresponding to the four categories of visual
> stimuli. Blocks were convolved with a double gamma “canonical” hemodynamic
> response function (Glover, 1999) to generate the main regressors.

FBI annotation: we have prepared the block onset files for you, with one file
for each of these event types.  You will find these files in the subject `func`
directories (see below).  The files are in "Custom 3 column format" \- see the
[FEAT user guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide) for
more information.

> In addition, the estimated motion parameters were entered as covariates of no
> interest to reduce structured noise due to minor head motion. Linear
> contrasts of [words N fixation] and [objects N scrambled objects] identified
> reading- and object-sensitive areas, respectively. First level results were
> registered to the MNI-152 template using a 12-DOF affine transformation
> (Jenkinson and Smith, 2001) and all subsequent analyses were conducted in the
> MNI standard space. A second level fixed-effects model combined the two first
> level runs into a single, subject-specific analysis which was then entered
> into a third level, mixed effects analysis to draw inferences at the
> population level (Beckmann et al., 2003; Woolrich et al., 2004).

FBI annotation: see the FEAT user manual for details of the options above:
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide

> In order to restrict the analyses to the ventral and lateral OTC, two
> anatomical masks were drawn in standard space. The ventral OTC mask
> encompassed the posterior portion of the left fusiform gyrus,
> occipito-temporal sulcus (OTS), and medial parts of the inferior temporal
> gyrus (ITG) — areas consistently activated by visual word recognition tasks
> (Fiez et al., 1999; Fiez and Petersen, 1998; Herbster et al., 1997; Price et
> al., 1996; Price et al., 1994; Rumsey et al., 1997; Shaywitz et al., 2004).
> The standard space coordinates were: X=−30 to −54, Y=−45 to −70 and Z=−30 to
> −4. This region is sometimes referred to as the “visual word form area”
> (Dehaene et al., 2005; McCandliss et al., 2003), although the term is
> misleading as it suggests a functional specificity which is not present
> (Price and Devlin, 2003, 2004). The lateral OTC mask encompassed lateral
> posterior fusiform gyrus, posterior OTS and lateral parts of posterior ITG
> — areas consistently activated by visual objects and collectively known as
> the “lateral occipital complex” (Grill-Spector et al., 1999; Malach et al.,
> 1995). The standard space coordinates were X=−33 to −56, Y=−67 to −89 and
> Z=−20 to +4. Within each mask, only voxels with at least a 20% chance of
> being grey matter were included based on an automatic tissue segmentation
> algorithm (Zhang et al., 2001).

We have generated these masks files for you.  You will find them in the `data`
directory, with filenames `ventral_otc_cube.nii.gz` and
`lateral_otc_cube.nii.gz` respectively.

## The data format

Your friendly OpenNeuro team has arranged the data in the standard BIDS format:
http://bids.neuroimaging.io

In this particular case this means that each subject has a directory structure
like this:

```
sub-01
├── anat
│   └── sub-01_T1w.nii.gz
└── func
    ├── sub-01_task-onebacktask_run-01_bold.nii.gz
    ├── sub-01_task-onebacktask_run-01_events.tsv
    ├── sub-01_task-onebacktask_run-02_bold.nii.gz
    └── sub-01_task-onebacktask_run-02_events.tsv
```

For each subject, you will need the anatomical T1 file at
`anat/sub-XX_T1w.nii.gz` and the functional files in the `func` directory.
The ``.nii.gz`` files are the 4D EPI FMRI runs, and the `.tsv` files give full
details about all events during the runs.  You will also find event files for
each event named in the corresponding FMRI analysis methods section above (not
shown in the listing).  These files end in `_label-<event_name>.txt`, where
`<condition_name>` is the name of the event.  The labels are `objects,
scrambled, words, consonants`.

## Your report

For your assessment, you should:

1.  Fill in the README.txt / README.docx file with a detailed guide to
    repeating all the steps in your analysis.  Reference or quote the methods
    section from the paper, as we have above, for example:

    "I ran the FEAT analysis tool, and chose the option to coregister the EPI
    functional scan `sub-XX/func/sub-XX_task-onebacktask_run-01_bold.nii.gz`
    to the anatomical T1 scan `sub-XX/sub-01_T1w.nii.gz`. This was in order to
    replicate the following from the thesis method section "A 3-step
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
