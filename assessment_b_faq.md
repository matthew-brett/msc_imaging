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

These are the specifications for the model at the second level.  At the second
level, the rows in the model correspond to COPE scans, one per run.  The
regressors in the section above therefore have one value per run.

In the case of the BART, there is only one run per subject, and therefore one
value per subject.

The value is the number of times the subject inflated the balloon over the
course of the run.  You'll see my algorithm for that calculation at:

https://github.com/matthew-brett/msc_imaging/blob/master/bart_pumps.py

The result of running that algorithm is the file at:

https://github.com/matthew-brett/msc_imaging/blob/master/bart_pumps.txt

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
