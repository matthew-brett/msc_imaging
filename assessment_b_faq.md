# Frequently asked questions for Assessment B

Feel free to proposed edits or new questions for this FAQ.

You can do that by email to m.brett@bham.ac.uk, or for cool points, use the
pen icon at the top right of the page to make and propose your edits.  You'll
need a Github account for that, but that's a good thing to do in any case.

## Do I have to copy the data? or Why am I getting permission errors?

You have a folder called `replication` in your home directory, and that has a
link named `data`, which points to `/home/data/FBI/assessment`.  That
directory is read-only - so you cannot save anything into the
`/home/data/FBI/assessment` directory, and therefore, you can't save anything
in your `replication/data` directory.

This might be annoying, because when you run tools like BET or FEAT, the
default output image or directory matches the input data.  For example, if you
try to run BET on the image
`/home/data/FBI/assessment/ds000009_R2.0.3/sub-01/anat/sub-01_T1w` - then the
default output image will be
`/home/data/FBI/assessment/ds000009_R2.0.3/sub-01/anat/sub-01_T1w_brain`.
Another pointer to the same place is
`/home/people/xxx/replication/data/ds000009_R2.0.3/sub-01/anat/sub-01_T1w_brain`
where `xxx` is your username.   You have two options:

1.  Copy the entire data folder to another directory in your home directory
    space.  We don't recommend this, because it will take up a lot of space,
    and you may run out of space when doing your analysis.
2.  Set the output files and directories to point into your home space.  For
    example, for the BET output above, you could make an output directory like
    this:

        # Make a directory to put files for this subject
        mkdir -p ~/replication/analysis/sub-01/anat

    and then use an output filename like
    `/home/people/xxx/replication/analysis/sub-01/anat/sub-01_T1w_brain`

## Do I need to reorient the structural images?

Have a look at the structural files with fsleyes - are they in the correct
orientation?  Or they they sagittal images like you had in the workshop?  You
need to reorient if they are not already in the correct orientation.

## What's this about using FLIRT for registration?

The very observant among you may have noticed that chapter 2 of Cohen's thesis
gives more detail on the two-step registration procedure that she used again
in chapter 4 (where chapter 4 refers to the experiment you are analyzing).
That chapter has the following text (section 2.2.5):

> A 3-step registration process was applied using FSL’s FLIRT module for
> linear registration for the UCLA data. EPI functional images were first
> registered to an inplane T2-weighted structural image (matched bandwidth; 7
> DOF). The inplane structural image was registered to the high-resolution
> structural image (MPRage; 7 DOF), and the high-resolution image was
> registered to standard MNI152 space using FLIRT linear registration with 12
> degrees of freedom.

The steps that she described there are a little advanced, and involve using
the FSL command line tools, of which FLIRT is one - see
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT . Cohen is using FLIRT to
register the images and record the transformation needed to match one image to
the other.  She is then using more of the FSL tools to combine these
transformations and finally reslice the images with the resulting
transformation.  See http://nipy.org/nibabel/coordinate_systems.html for
background on recording the transformations.

## What is spatial smoothing?

See: https://matthew-brett.github.io/teaching/smoothing_intro.html

## What's this about "number of pumps" for the BART?

You'll find this in the assessment document, quoting from Cohen's thesis:

> The model for each task included a regressor modeling mean activity and
> demeaned regressors for SSRT (SS), number of pumps (BART), k (TD), and
> amount of reported regulation (ER). Outlier deweighting was performed using
> a mixture modeling approach (Woolrich, 2008).

These are the specifications for the model at the group level.  At the group
level, the rows in the model correspond to COPE scans, one per run.  The
regressors in the section above therefore have one value per run.

In the case of the BART, there is only one run per subject, and therefore one
value per subject.

The value is the number of times the subject inflated the balloon over the
course of the run.  You'll see my algorithm for that calculation at:

https://github.com/matthew-brett/msc_imaging/blob/master/bart_pumps.py

The result of running that algorithm is the file at:

https://github.com/matthew-brett/msc_imaging/blob/master/bart_pumps.txt

## How about the SSRT? I think I need this for my group model

Indeed you do need the SSRT for your group model (see below).

Cohen describes the SSRT calculation in section 4.4.2 of her thesis:

> To calculate SSRT, first all correct RTs were arranged in an assumption-free
> distribution in ascending order. Then the proportion of failed inhibition
> (i.e., the proportion of stop trials on which the participant responded) was
> determined. The RT corresponding to that proportion was computed (i.e., if
> failed inhibition was .55, the RT corresponding to 55% of the area under the
> RT distribution curve): the quantileRT. SSRT was calculated as the
> difference between the quantileRT and the average SSD.

I assume that she did this calculation from the behavioural data recorded for
the FMRI runs, and that she pooled the data across the two SS task runs, to
give an SSRT for each subject.

You'll see my implementation of the SSRT algorithm in:

https://github.com/matthew-brett/msc_imaging/blob/master/write_ssrts.py

The result of running that algorithm on the FMRI event files is here:

https://github.com/matthew-brett/msc_imaging/blob/master/ssrts.tsv

That file contains the regressor you need for your higher-level analysis (see
below).

You might also be interested in my exploration of the SSRT value in:

https://github.com/matthew-brett/msc_imaging/blob/master/read_ssrt.ipynb

## Should I add a coordinate results table?

Cohen gives a table of coordinates, estimated brain areas, maximum z score and
cluster extent for each contrast.  If you want to check your results, you may
also want to generate a matching table.  We would love to see that in your
report, as confirmation, but we won't mark you down if you don't include it.

To get a results table for a particular contrast map, open the corresponding
`report_poststats.html` file in your FEAT results directory, and click on the
contrast image display.  You should get a statistics result table.  In fact
this calls up the matching `cluster_zstatN.html` file where N is your contrast
number.  See the [FEAT User
Guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide) for more detail.

## Slice timing

You may want to do slice timing on your first-level analyses.

Cohen does not refer to slice timing in her write-up, but you may prefer to
put it into your pipeline.

Slice timing adjusts the functional scans for the fact that the scanner
collects the slices one by one, so the last slice that the scanner collects
is nearly one TR in time after the first slice in the volume.

One way of adjusting for this, is by interpolating the scan data in time, to
get an estimate of what the voxel values would have been, if they had all been
collected at the same time.

See my [slice timing
tutorial](http://matthew-brett.github.io/teaching/slice_timing.html) for an
introduction.

First you will need to know what order the scanner collected the slices in
your data.   To help you with this, I have written a tiny script, available
at:

https://raw.githubusercontent.com/matthew-brett/msc_imaging/master/show_slice_order.py

Use it by downloading the file as `show_slice_order.py` to your PBIC account
somewhere, then run with:

```
python show_slice_order.py data/ds000009_R2.0.3/sub-01/func/sub-01_task-*.json
```

It will print out the slice order of each functional run, as recorded in the
[JSON](https://en.wikipedia.org/wiki/JSON) file for that run.

To do the slice-timing correction in FSL, see the [FEAT User
Guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide).

Note that I haven't done all the work for you in my script.  You need to work out how the output of my script relates the slice timing inputs that FSL accepts, and then either adapt the script to write the file you need, or take the output and put it into a file by hand.

## What are the files in the `dwi` directory?

Each subject has a `dwi` directory, alongside the `anat` and `func`
directories.  Here's a listing for `sub-01`.

```
sub-01/dwi
|-- sub-01_dwi.bval
|-- sub-01_dwi.bvec
|-- sub-01_dwi.json
`-- sub-01_dwi.nii.gz
```

These are Diffusion Weighted Images (DWI).  They are very interesting images,
but outside the scope of Cohen's analysis, and your assessment.  In your
future careers, you will probably find papers trying to relate the anatomical
connectivity information from these DWI images to the functional information
from the BOLD contrast images, but that's not your task here.

## What's the "sigma" in high-pass filtering?

Thanks to Mairi Houlgreave for this question.

In Cohen's description, you will see:

> Time-series statistical analysis was carried out using FILM (FMRIBs Improved
> Linear Model) with local autocorrelation correction after highpass temporal
> filtering (Gaussian-weighted least-squares straight line fitting with sigma
> = 33.0s).

That is confusing, because the parameter you will see in the FEAT GUI is the
the high-pass frequency cut-off in seconds, where the default is 100.
However, if you run an analysis with high-pass filtering enabled, and a
cut-off of 100, you will something like this in the `report_prestats.html`
file:

> highpass temporal filtering (Gaussian-weighted least-squares straight line
> fitting, with sigma=50.0s).

As usual, see the [FEAT User
Guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide) for some more
detail on the implementation of high-pass filtering with regression line
fitting.  It appears that the "sigma" setting in the FEAT report corresponds
to the cut-off value divided by 2.  I don't know of a solid reference for
this, but see [this wiki entry][1].

  [1]: https://www.spinozacentre.nl/wiki/index.php/NeuroWiki:Processing_fMRI_(FSL)#Temporal_filtering

## Any hints for the group models?

Here's the relevant part of Cohen's descriptions for the group models.

> For the two tasks that had more than one run (SS and ER), data were combined
> across the two runs using a fixed effects model, and then modeled using
> mixed effects at the group level with FSL's FLAME model (Stage 1 only). The
> model for each task included a regressor modeling mean activity and demeaned
> regressors for SSRT (SS), number of pumps (BART), k (TD), and amount of
> reported regulation (ER).

To recap what you have done already in the workshops, we return to the distant
days of workshop 5.

You did two types of higher-level analysis in that workshop.

*   Higher-level analysis 1:

    * first level analysis of each FMRI run;
    * one second level analysis for each subject with more than one run, to
      average across runs within subject;
    * third level analysis comparing a mixture of first level analysis (for
      subjects with only one run) with second level analyses (for subjects
      with more than one run).

*    Higher-level analysis 2:

    * first level analysis of each FMRI run (you re-used these);
    * one big second level analysis in which you use all the first level
      analysis directories, and make contrasts that write out the average
      across runs within subject;
    * third level analysis using the contrast images from the second level
      analysis, one per subject (one per contrast at the second level).

The FEAT user guide uses the term "mid-level" for the "second level" analyses
above.  The second level / mid-level analyses are to combine data across runs
within subject.

If you only have one run per subject, then you don't need a mid-level
analysis, and you can go straight to the third level.  We can also call this
the group level.

If you do have more than one run per subject, then you will need to do a
mid-level analysis.   Read Cohen's description above, and try and work out
which of higher-level analysis 1 or 2 she has used.

All the above is about the machinery to use for the group modeling.  The next
set of questions is about the actual group model Cohen is describing in her
section above.

For the SS task, the group model is one column of all ones to model the mean,
and one column giving the SSRT value for each subject.  The second column has
had the mean subtracted.  See above for the SSRT values.  That's the model -
but you need to work out which contrast she has used for her main effect.

I think you can work this out, but you will probably get some help from the
desciptions of the cluster tables later on in Cohen's chapter 4.

Here's the caption for Table 4.2:

> Clusters associated with successful stopping - going on the SS task.

If you apply a contrast of "1 0" to the design with the group mean and the
demeaned regressor, you will select the group mean column, and the output will
show you voxels where the first-level contrast is high or low across subjects.

If you apply a contrast of "0 1" to that design, you will get voxels where the
first level contrast value has a linear relationship to the SSRT.

What do you think from Cohen's descriptions - has she used her contrast to
selet the group mean column for the BART, or to select the SSRT regressor?

For the BART task, the group model is one column of all ones to model the
mean, and one column giving the number of pumps. This second column has had
the mean subtracted (and so has a mean of 0).  See above for the values of
that regressor.  As above, you need to work out which contrast she has used
for her main effect.

For your convenience, here's the caption for Table 4.3:

> Table 4.3: Clusters associated with cashing out - inflating the balloon on
> the BART.

Do you think Cohen has applied her contrast to the group mean regressor (1, 0)
or to the number of pumps regressor (0, 1)?

If you are among the brave, you may be analyzing the ER and TD tasks.  Because
you are brave, I know you will not want much help, but, try reading the
cluster table descriptions for these contrasts.  See whether you can work out
what contrasts Cohen has applied to her group model.

Have a look at the `ds009_participants.tsv` file in this repository for some
values you could use for the ER and TD higher-level regressors:

https://github.com/matthew-brett/msc_imaging/blob/master/ds009_participants.tsv

## Why do I get an error when doing non-linear registration

Some of you have found that you get an error when you try to do non-linear
registration.   The error starts with something like:

> Warning: nonlinear registration is turned on but FEAT cannot automatically
> find the whole-head image related to the selected brain-extracted structural
> image /home/people/xxx/replication/my_data/sub-01/sub-01_T1_brain (this
> needs to end in "_brain").

When FSL does non-linear registration, it likes to have access to the
whole-brain image - the image before skull stripping.  To get this, it looks
for an image with the same name as the skull-stripped image, but without the
`_brain` suffix.  So, in the case above, FSL is looking for an image called
`/home/people/xxx/replication/my_data/sub-01/sub-01_T1.nii.gz`.  You can
provide this by linking the original T1w anatomical image for that subject
into your directory with the correct name.  For example:

```
cd ~/replication
ln -s data/ds000009_R2.0.3/sub-01/anat/sub-01_T1w.nii.gz my-data/sub-01/sub-01_T1.nii.gz
```

## How did you create the event .txt files for SS and BART?

There's a hint about this in the assessment document on Canvas.  The OpenFMRI
data does not not come with the ``.txt` files giving the onset, duration and
amplitude information for each event type.  I created these files from the
overall event definition files for each task.

For example, here are a listing of the first few ``.txt`` files for subject
01:

```
sub-01/func/sub-01_task-balloonanalogrisktask_label-inflate.txt
sub-01/func/sub-01_task-balloonanalogrisktask_label-beforeexplode.txt
sub-01/func/sub-01_task-balloonanalogrisktask_label-cashout.txt
sub-01/func/sub-01_task-balloonanalogrisktask_label-explode.txt
```

I used a Python script to generate these files from the source file:

```
sub-01/func/sub-01_task-balloonanalogrisktask_events.tsv
```

The script that I used to do this was:

https://github.com/matthew-brett/msc_imaging/blob/master/ds009_onsets.py

As you can see from that script, I had to write small algorithms to analyze
the events, and select the ones corresponding to the individual trial types. I
have defined this algorithm for the SS and BART tasks, but I haven't done this
for the ER and TD tasks.

## Where do I get the event files for the ER and TD tasks?

The short answer is (for now):

  * the ER files are here:

    https://github.com/matthew-brett/msc_imaging/blob/master/er_files.zip

  * the TD files will soon be here:

    https://github.com/matthew-brett/msc_imaging/blob/master/td_files.zip

<!-- make er-files -->
<!-- make td-files -->

The long answer is about how I made those files, and how you might make or
modify those files yourself.

The trick is to work out, from Cohen's thesis, how the events in (for example)
the following files, correspond to the regressors Cohen describes in her
thesis:

```
sub-01/func/sub-01_task-emotionalregulation_run-02_events.tsv
sub-01/func/sub-01_task-discounting_events.tsv
```

You can do this any way you like.  For example, you can download these files
to your laptop, and open them in Excel.  They are just text files containing a
spreadsheet, where the values are separated by tabs (Tab Separated Values =
tsv).

Excel would be horribly inefficient for the task of processing these values,
so here's me exploring what the ER .tsv file fields mean, and how to get the
regressors:

https://github.com/matthew-brett/msc_imaging/blob/master/on_er.ipynb

Then you need to fill in or modify an algorithm for the ER and TD tasks,
corresponding to the algorithm for - say - the SS task here:

https://github.com/matthew-brett/msc_imaging/blob/master/ds009_onsets.py#L39

Finally, you need to fill or modify the `preprocessor` and `conditions` fields
in the `TASK_DEFS` definition in that file, set the `ok` field to `True`, and
run the `write_all_tasks` function in that file with something like:

```
python ds009_onsets.py replication/data/ds000009_R2.0.3 out_dir
```

where `replication/data/ds000009_R2.0.3` is the path to the data, and
`out_dir` is the directory into which the script will write the new `.txt`
files.

## Running the Python scripts to generate the .txt files

You only need to do this if you want to modify or understand what I have done
to generate the .txt files.

Be careful, the scripts I have written do not work on the PBIC cluster.  The
PBIC cluster has a very old version of Python.  What I do, and what I
recommend you do, is run these scripts on your laptop.  I recommend:

* Make sure you have Anaconda installed : https://www.anaconda.com/download
* (re-) Download the msc_imaging archive from
  https://github.com/matthew-brett/msc_imaging/archive/master.zip and unzip
  the files somewhere, say your desktop;
* Open the Terminal (Windows: start Powershell; Mac: open Terminal.app);
* Change directory to the directory containing the unzipped files;
* Run the script as above to make sure it works.

    ```
    python ds009_onsets.py replication/data/ds000009_R2.0.3 out_dir
    ```

You might also consider opening up the notebook files, maybe by opening the
Anaconcda Navigator, opening the Jupyter Notebook, nagivating to the folder
containing the unzipped files, and opening (e.g.) `on_er.ipynb`.
