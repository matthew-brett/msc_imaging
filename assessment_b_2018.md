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
10.1016/j.neuroimage.2009.03.014.

Download the full text from
<https://www.sciencedirect.com/science/article/pii/S1053811909002353>.

## Overview of the task

Your job is to reproduce the results from the Duncan *et al* paper, from the original data in the ds107 dataset.

Duncan *et al* did two FMRI runs on each of 49 subjects.  The runs had the same
conditions, but in different order.  The subject observed a succession of
stimuli presented at one second intervals; the subject's task was to press
a button if the stimulus just presented was the same as the previous stimulus
\- a [1-back](https://en.wikipedia.org/wiki/N-back) task.  The conditions
consisted of blocks of stimuli from specific categories. These were:

1. pictures of objects (OBJECTS);
1. scrambled pictures of objects (SCRAMBLED);
1. words (WORDS);
1. consonant strings (STRINGS).

In between some of these blocks there were periods of rest (REST).

Duncan *et al* were interested in the activation for these subtractions:

1. OBJECTS - SCRAMBLED;
1. WORDS - REST.

They expected OBJECTS - SCRAMBLED to activate the "lateral occipital complex"
in the lateral Occipital Temporal Cortex (OTC).

They expected WORDS - REST to activate the "visual word form area" in
the ventral OTC, although they disagree with the name "visual word form area".

Their further interest was to look at the variation in the voxels identified as
activated in these regions, across runs.  The point here was that, if there was a lot of variation, then people using tasks like this, to identify these regions, would have to be more careful in their analysis and conclusions.

The results that you need to replicate are:

*   (For extra marks) Behavioral data analysis for the 1-back tasks, including
    d-prime scores and reaction times (table 1 of the paper);
*   Group analysis whole brain activation map for OBJECTS - SCRAMBLED;
*   Group analysis whole brain activation map for WORDS - REST;
*   For each of (OBJECTS \- SCRAMBLED activation in lateral OTC) and (WORDS
    \- REST activation in ventral OTC):
    *   Between-subject variability in coordinates of peak activation (table 2);
    *   Within subject (across run) variability of:
        *   Peak voxel coordinates (Euclidean distance);
        *   "Ratio of commonly activated voxels" at different Z thresholds
            (1\.64, 2\.3, 3\.09, 4\.0) (figure 3A);
        *   (For extra marks) "Ratio of commonly activated voxels" at
            Z thresholds above, for regions defined by activated voxels within
            9mm of peak (figure 3B).

Duncan *et al* restricted their search for activated voxels to gray matter, by segmenting the subjects' structural images into gray- and white-matter, and masking out the white-matter voxels.  You do not need to do this, but if you do, we will give you extra marks (see below).

If you do the analyses for extra marks, you will need to do some extra reading
/ ask for extra help - which we are very happy to provide.

## The task in detail

In the following paragraphs, we have reproduced sections from the methods and
results sections of Duncan *et al*. You will see discussion of your task and
other notes in our annotations labeled with "FBI:"

> Data processing was carried out using FSL 4.0 (www.fmrib.ox.ac. uk/fsl).

FBI: you will be using the versions of FSL and FEAT that are
currently on the cluster.

> To allow for T1 equilibrium, the initial two images of each run were
> discarded.

FBI: the experimenters have already dropped the two dummy volumes
from the image files in the ds107 dataset, so the first volume in each FMRI run, in the data you have, is the first not-dummy scan.

> The data were then realigned to remove small head movements (Jenkinson et
> al., 2002), smoothed with a Gaussian kernel of FWHM 6 mm, and pre-whitened to
> remove temporal auto-correlation (Woolrich et al., 2001).
>
> The resulting images were entered into a general linear model with four
> conditions of interest corresponding to the four categories of visual
> stimuli. Blocks were convolved with a double gamma "canonical" hemodynamic
> response function (Glover, 1999) to generate the main regressors.

FBI: we have prepared the block onset files for you, with one file for each of
these event types.  You will find these files in the subject `func` directories
(see below).  The files are in "Custom 3 column format" \- see the [FEAT user
guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide) for more
information.  Subject 41, run 2 in the original data appears to have
a truncated event onset file, and we suggest you exclude that subject from your
analyses.

> In addition, the estimated motion parameters were entered as covariates of no
> interest to reduce structured noise due to minor head motion. Linear
> contrasts of [words > fixation] and [objects > scrambled objects] identified
> reading- and object-sensitive areas, respectively. First level results were
> registered to the MNI-152 template using a 12-DOF affine transformation
> (Jenkinson and Smith, 2001) and all subsequent analyses were conducted in the
> MNI standard space. A second level fixed-effects model combined the two first
> level runs into a single, subject-specific analysis which was then entered
> into a third level, mixed effects analysis to draw inferences at the
> population level (Beckmann et al., 2003; Woolrich et al., 2004).

FBI: see the FEAT user manual for details of the options above:
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide

> In order to restrict the analyses to the ventral and lateral OTC, two
> anatomical masks were drawn in standard space. The ventral OTC mask
> encompassed the posterior portion of the left fusiform gyrus,
> occipito-temporal sulcus (OTS), and medial parts of the inferior temporal
> gyrus (ITG) - areas consistently activated by visual word recognition tasks
> (Fiez et al., 1999; Fiez and Petersen, 1998; Herbster et al., 1997; Price et
> al., 1996; Price et al., 1994; Rumsey et al., 1997; Shaywitz et al., 2004).
> The standard space coordinates were: X=-30 to -54, Y=-45 to -70 and Z=-30 to
> -4. This region is sometimes referred to as the "visual word form area"
> (Dehaene et al., 2005; McCandliss et al., 2003), although the term is
> misleading as it suggests a functional specificity which is not present
> (Price and Devlin, 2003, 2004). The lateral OTC mask encompassed lateral
> posterior fusiform gyrus, posterior OTS and lateral parts of posterior ITG
> - areas consistently activated by visual objects and collectively known as
> the "lateral occipital complex" (Grill-Spector et al., 1999; Malach et al.,
> 1995). The standard space coordinates were X=-33 to -56, Y=-67 to -89 and
> Z=-20 to +4.

FBI: We have generated these mask files for you.  You will find them
in the `data` directory, with filenames `ventral_otc_cube.nii.gz` and
`lateral_otc_cube.nii.gz` respectively.

FBI: You can implement the following paragraph for 5 extra marks.

> Within each mask, only voxels with at least a 20% chance of
> being grey matter were included based on an automatic tissue segmentation
> algorithm (Zhang et al., 2001).

FBI: Implementing this step will involve segmenting the individual structural
images into gray- and white-matter.  The image you segment should be registered
to MNI space.  You would then apply the gray-matter mask to the mask files
above to make a new mask, that is specific to each subject, containing the
ventral and lateral OFC voxels that are also in gray-matter.  Do this for
5 extra marks.  If you do that, use these masks in the analyses of regions of
activation that follow.

FBI: the first step involves some behavioural analysis.  It is optional, for
5 extra marks.

> Behavioural data from six subjects were lost due to a problem recording
> button press responses while in the scanner. The data from the remaining
> subjects (n=39) were analysed using signal detection theory as hits and false
> alarms. The mean hit rate was 0.791 and the false alarm rate was 0.011,
> indicating that participants performed the task adequately (see Table 1). In
> addition, d-prime (d') scores were calculated to measure sensitivity for
> detecting repeated items (Table 1).

FBI: If you want to do this step, you should replicate the data in table 1 as
closely as you can, showing your working.  Results count for 5 extra marks (see
*Your report* below).  Please see the note in the "Data format" section for
a confusing error in the event files.

FBI: Do the two ANOVA analyses in the next section for a total of 4 extra
marks.

> These were then entered into 4 x 2 repeated measures ANOVA examining the
> effects of Category (words, consonant strings, objects, scrambled objects)
> and Run (first, second). A main effect of Category (F(3,114)=77.9,
> p b 0.0001) indicated that detecting repetitions of scrambled objects was
> most difficult, but there was no difference between words or objects (t(38)
> = 0.05, p = 0.961). Importantly, neither the main effect of Run (F(1,38)
> = 0.494, p = 0.486) nor the Category x Run interaction (F(3,114) = 1.665,
> p = 0.179) was significant, indicating that participants' performance did not
> significantly change from the first to the second run. The same pattern was
> present in the reaction times to correct detections (i.e. "hits"). Again,
> there was a main effect of Category (F(3,114) = 5.4, p = 0.002) but no main
> effect of Run (F(1,38) = 0.09, p = 0.765) and no Category x Run interaction
> (F(3,114) = 1.169, p = 0.325). In other words, there was no behavioural
> evidence for task learning that might confound the activation patterns across
> runs.

FBI: Extra marks: 2.5 marks for ANOVA of d-prime scores, 2.5 marks for ANOVA of
reaction time for correct detections.

> Consistent with previous research, the peak activation in ventral OTC for
> words relative to fixation was located in the occipito-temporal sulcus (-42,
> -50, -20; Z = 7.7), extending both medially onto the convexity of the
> posterior fusiform gyrus and laterally onto the inferior temporal gyrus.

FBI: Show the group-level activation map, on the MNI standard brain, for
OBJECTS-SCRAMBLED and WORDS-REST: 5 marks each = 10 total. Show the table of
activated clusters: 3 marks each = 6 total.  Give the file-system location of
the t-statistic map that you generated for this comparison: 2 marks each
= 4 total.  Total for this item = 20.

> To visualize this activation, the group results were projected onto an inflated
> surface of an "average" brain (i.e. Freesurfer's fsaverage subject) to
> illustrate that activation was not limited to the ventral surface but also
> present inside the occipito-temporal sulcus (Fig. 2B).

FBI: There is no need to display the results on the inflated surface.  If you
want to do it, please go ahead, and we will be impressed, but we will not give
you extra marks.

From the legend in figure 2:

> D) Effect sizes for words, consonant strings, objects and scrambled objects
> relative to fixation in ventral and lateral OTC. Error bars represent
> standard error of the mean. * indicates a significant difference at
> p < 0.001.

FBI: Replicate panel D of figure 2, by taking the average of all voxels within
the lateral and ventral OTC mask, for the contrast images of WORDS, CONSONANTS,
OBJECTS, and SCRAMBLED OBJECTS.  Hint: investigate the `fslstats` command to do
things like apply a masking image, and calculate an average across the
remaining voxels.  This is worth 5 marks.

From the legend of table 2:

> Summary of inter-subject variability in peaks coordinates for words and
> objects. Coordinates are in the MNI152 space and the Z-score is for the peak
> voxel.

FBI: Record the coordinate of the peak voxel in ventral OFC for the WORDS \-
REST comparison.  Do the same for the lateral OFC and the OBJECTS \- SCRAMBLED
comparison.  Use these values to replicate the results in table 2.  9 marks.

FBI: Hint.  The [Euclidean
distance](https://en.wikipedia.org/wiki/Euclidean_distance) $d$ between two
points with coordinates $x_1, y_1, z_1$ and $x_2, y_2, z_2$ is given by the 3D
extension of Pythagoras' theorem - $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2
+ (z_1 - z_2)^2}$.  In Matlab, if the two points are in two 1 x 3 matrices
`point1` and `point2`, this becomes `d = sqrt(sum((point1 - point2).^2))`.

> Because studies often define functional ROIs using a sphere with a fixed
> radius centred on the peak voxel (Blankenburg et al., 2006; Jiang et al.,
> 2007; Miller and D'Esposito, 2005; Pulvermüller et al., 2006), the first
> measure examined the spatial reliability of the peak voxel since this
> determines the fROI. The coordinates of peak voxels were extracted for each
> participant from both runs and the distance between peaks was calculated
> using the standard Euclidean distance measurement. On average, peaks for
> words were separated by 7.4 mm while peaks for objects were 8.3 mm apart.

FBI: replicate this calculation, and show the histogram of the distances
between the run1 / run2 peak coordinates, across subjects. 10 marks.

> ... the second measure assessed consistency in terms of the volume of
> commonly activated cortex between runs in both ventral and lateral OTC. This
> was computed as the ratio ($R_{ij}$) of commonly activated voxels to the
> total number of activated voxels in two runs, $i$ and $j$:
>
> $R_{ij} =2 V_{ij} / (V_i + V_j)$
>
> where $V_{ij}$ is the number of voxels within the ROI which were active in
> both runs $i$ and $j$; and $V_i$ and $V_j$ are the number of voxels within
> the ROI that were active in runs $i$ and $j$, respectively  [...]
>
> To avoid conditioning the results by an arbitrary choice, five thresholds
> were used spanning a typical range: i) Z>1.64 (p < 0.05 uncorrected), ii)
> Z>2.3 (p<0.01 uncorrected) iii) Z>3.09 (p>0.001 uncorrected), and iv) Z>4.0,
> (roughly p<$10^{-4}$, which is fairly conservative) and v) Z>5.0 (roughly
> p<$10^{-6}$, which would conservatively correct for multiple comparisons
> across the whole brain with a family-wise $\alpha < 0.05$).

FBI: replicate this calculation to generate your own version of figure 3A.
Hint: to do this task, consider looking at the `fslmaths` command to combine
mask images, and the `fslstats` command to give volumes within a mask.  15
marks.

FBI: You do not need to do the analysis in the next section, but if you do, you
have the potential to earn 10 extra marks.

> Finally, it is possible to combine peak and volume measures to define an fROI
> as the set of active voxels that are contiguous with the peak activation
> (Downing et al., 2006). This approach will help to reduce variability between
> runs as long as the two peaks fall within overlapping clusters. To assess the
> consistency of this method, we defined fROIs as the set of contiguous active
> voxels (using the same set of five thresholds as above) that included the
> peak voxel and were within a 9 mm radius of the peak voxel following Downing
> et al.(2006). The results are shown in Fig. 3B. Again, the highest
> consistency values were for the lowest statistical threshold. For the
> contrast [words > fixation] in ventral OTC, the mean consistency ratio
> ($R_{ij}$) was 0.50 (SEM = 0.05) and for the contrast [objects > scrambled],
> the mean $R_{ij}$ was 0.45 (SEM = 0.05). Increasing the threshold to
> Z > 5 reduced the overlap to 0.27 $\pm$ 0.05 for words and 0.21 $\pm$ 0.06
> for objects and precluded identifying an fROI in 8 and 18 of the
> participants.

FBI: This is a harder task for extra marks.  You will need some machinery to
identify voxels above threshold that are within 9mm of the peak voxel.   We
will leave this to your ingenuity, but we are happy to give advice, if you want
to try this.  You should end up by replicating something like figure 3B.

## The data format

Your friendly OpenNeuro team has arranged the data in the standard BIDS format:
http://bids.neuroimaging.io

In this particular case this means that each subject has a directory structure
like this:

```
sub-01
|-- anat
|   `-- sub-01_T1w.nii.gz
`-- func
    |-- sub-01_task-onebacktask_run-01_bold.nii.gz
    |-- sub-01_task-onebacktask_run-01_events.tsv
    |-- sub-01_task-onebacktask_run-02_bold.nii.gz
    `-- sub-01_task-onebacktask_run-02_events.tsv
```

For each subject, you will need the anatomical T1 file at
`anat/sub-XX_T1w.nii.gz` and the functional files in the `func` directory.
The ``.nii.gz`` files are the 4D EPI FMRI runs, and the `.tsv` files give full
details about all events during the runs.  You will also find event files for
each event named in the corresponding FMRI analysis methods section above (not
shown in the listing).  These files end in `_label-<event_name>.txt`, where
`<condition_name>` is the name of the event.  The labels are `objects,
scrambled, words, consonants`.

Be careful of the data in the `_events.tsv` files.  These files have a column
for "trial_type" that has wrong data; the column labeled "0" has the event
identifiers that are correct.  From these identifiers, you can see that
"trial_type" == "Words" are indeed for WORDS, but "trial_type" == "Objects" in
fact correspond to STRINGS, "trial_type" == "Scrambled objects" refer to
OBJECTS and "trial_type" == "Consonant strings" in refer to SCRAMBLED.  We did
fixed this coding for your `_label-<event_name>.txt` files above, but you need
to correct this error when using the `_events.tsv` files for the behavioural
analysis.

## Your report

For your assessment, you should:

1.  Fill in the README.txt / README.docx file with a detailed guide to
    repeating all the steps in your analysis.  Reference or quote the methods
    section from the paper, as we have above, for example:

    "I ran the FEAT analysis tool, and chose the option to coregister the EPI
    functional scan `sub-XX/func/sub-XX_task-onebacktask_run-01_bold.nii.gz`
    to the anatomical T1 scan `sub-XX/sub-01_T1w.nii.gz`. This was in order to
    replicate the following from the method section "First level results were
    registered to the MNI-152 template using a 12-DOF affine transformation
    (Jenkinson and Smith, 2001)".

    At each step, point to the output result folders in your
    `/home/people/xxx/replication` folder.

    Include the image and statistics output in your report.

    We will grade this report out of 40 on the following *general* criteria:

    *   Is the description of what you did clear? 15 marks.
    *   Have you justified all the steps of your analysis?  10 marks.
    *   How easy is it to exactly replicate your analysis (whether right or
        wrong)? You will get maximum marks if we can run a script to replicate
        the analysis given only the raw data that you have linked at
        `/home/people/xxx/replication/data` along with any script files or
        library code in your directory. 15 marks.

2.  As we have noted in the sections above, we will also grade you on the
    quality of your replication and replication report for the following
    features of the paper:

    1.   Replication of group activation map and cluster table for OBJECTS \-
         SCRAMBLED: 10 marks and WORDS \- REST: 10 marks.  See above for detail
         of mark allocation.
    1.   Replication of average effects within regions of interest, from panel
         D of figure 2: 5 marks.
    1.   Replication of inter-subject variability in peak activation
         coordinates for the two comparisons of interest and their matching OFC
         locations (table 2): 10 marks.
    1.   Replicate calculation of peak to peak variability across runs, for
         each comparison of interest and their matching OFC locations.  Show
         a histogram for each. Total is 10 marks.
    1.   Replicate consistency of activation ratio across runs for the
         5 Z-score thresholds: 15 marks.


## Extra marks

There are 100 ordinary marks available (marks above not labeled as "extra"),
and 25 extra marks available.

1.   Replication of data from table 1, including hits, false alarms, d-prime
     and reaction times:  5 marks.
1.   Apply per-subject gray-matter mask to region of interest: 5 marks;
1.   ANOVA for d-prime scores: 2.5 marks;
1.   ANOVA for reaction time of correct detections: 2.5 marks;
1.   Replicate consistency of activation metric for activation contiguous with
     peak: 10 marks.

Your final score will be your ordinary marks plus your extra marks, with
a maximum total of 100. For example, if you earn 85 ordinary marks, and 20
extra marks you will get 100. If you earn 60 ordinary marks and 15 extra marks
you will get 75.

## Submission

**Submission is automatic at noon January 7th**

At noon on January 7th, we will make a read-only copy of your directory
`/home/people/xxx/replication`. So, *before 12:00 of January 7th* make sure
that:

*   the `README.txt` / `README.docx` files are up to date;
*   all the analyses comprising the replication have been run inside that
    folder, and the results files referred to in the README file are available
    for your instructors to look at.
