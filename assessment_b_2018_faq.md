# Frequently asked questions for 2018 Assessment B

Feel free to propose edits or new questions for this FAQ.

You can do that by email to <m.brett@bham.ac.uk>, or for cool points,
use the pen icon at the top right of the page to make and propose
your edits.  You'll need a Github account for that, but that's a good
thing to have in any case.

## Do I have to copy the data? or Why am I getting permission errors?

You have a folder called `replication` in your home directory, and
that has a link named `data`, which points to
`/home/data/FBI/assessment`.  That directory is read-only - so you
cannot save anything into the `/home/data/FBI/assessment` directory,
and therefore, you can't save anything in your `replication/data`
directory.

This might be annoying, because when you run tools like BET or FEAT,
the default output image or directory matches the input data.  For
example, if you try to run BET on the image
`/home/data/FBI/assessment/ds107/sub-01/anat/sub-01_T1w` - then the
default output image will be
`/home/data/FBI/assessment/ds107/sub-01/anat/sub-01_T1w_brain`.
Another pointer to the same place is
`/home/people/xxx/replication/data/ds107/sub-01/anat/sub-01_T1w_brain`
where `xxx` is your username.   You have two options:

1.  Copy the entire data folder to another directory in your home
    directory space.  We don't recommend this, because it will take
    up a lot of space, and you may run out of space when doing your
    analysis.
2.  Set the output files and directories to point into your home
    space.  For example, for the BET output above, you could make an
    output directory like this:

        # Make a directory to put files for this subject
        mkdir -p ~/replication/analysis/sub-01/anat

    and then use an output filename like
    `/home/people/xxx/replication/analysis/sub-01/anat/sub-01_T1w_brain`

## Do I need to reorient the structural images?

Have a look at the structural files with `fsleyes` - are they in the
correct orientation?  Or they they sagittal images like you had in
the workshop?  You need to reorient if they are not already in the
correct orientation.

## What is spatial smoothing?

See: https://matthew-brett.github.io/teaching/smoothing_intro.html

## Slice timing

You may want to do slice timing on your first-level analyses.

Duncan *et al* do not refer to slice timing in their write-up, but
you may prefer to put it into your pipeline.

Slice timing adjusts the functional scans for the fact that the
scanner collects the slices one by one, so the last slice that the
scanner collects is nearly one TR in time after the first slice in
the volume.

One way of adjusting for this, is by interpolating the scan data in
time, to get an estimate of what the voxel values would have been, if
they had all been collected at the same time.

See my [slice timing
tutorial](http://matthew-brett.github.io/teaching/slice_timing.html)
for an introduction.

First you will need to know what order the scanner collected the
slices in your data.   The original functional images, from which the
experimenters made the OpenNeuro copies, had this information in
their [NIfTI header](https://nifti.nimh.nih.gov/nifti-1).  They all
had the header field named `slice_code` set to 3, which signifies
"alternating increasing".  This means that the scanner collected the
bottom slice first (call that slice 1), then the third-from-bottom
(slice 3), all the way up to slice 35, and then returned to collect
slice 2, 4 and so on.

To do the slice-timing correction in FSL, see the [FEAT User
Guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide).

## How do compare an event against fixation?

The methods of the paper used (among other
contrasts):

> contrasts of [words > fixation] and [objects
> scrambled objects]

WORDS, OBJECTS and SCRAMBLED are all event types.  If it is not clear
how to do contrasts of events, please read the contrast sections of
the [introduction to the General Linear
Model](https://matthew-brett.github.io/fbi2018/chapters/04/glm_intro)

Fixation is not an event \- at least, it is not an event for which
you have event onset files.  So, how do you compare WORDS to
fixation?

The trick is, that you can consider fixation to be everything that is
not modeled by the other events.

Another way to think of it, is that fixation is an *implicit
baseline*.

Consider [this analysis for a single
voxel](https://matthew-brett.github.io/fbi2018/chapters/04/glm_one_voxel).

Here we have only one event, and one haemodynamic predictor \- as
well as the intercept column of all ones.

The analysis estimates a slope relating the haemodynamic predictor
(x) to the voxel signal (y).

The slope is in the following situation: the signal is low, when the
predictor is low (or negative), and high when the predictor is high.
Notice that the predictor is low during the rest blocks (the stuff we
have not modeled).

This is generally true; the event regressors are high when the events
have just happened, and low during periods when the events are not
happening.

When there is more than one event, you can think of each event
regressor separately picking up signal that relates to the
haemodynamic prediction for the corresponding event.

Each slope we estimate, for the event, is a slope *relative to the
not-modeled signal*, and so, relative to rest, or fixation, if we
have not modeled rest or fixation.

Therefore, the slope for WORDS will be positive when the signal
during the WORDS events is greater than signal during fixation
/ rest, and the same is true for the other events.  Therefore the
slope for OBJECTS is positive when signal after OBJECTS events is
greater than activity during rest, and so on.

There is a somewhat technical discussion of implicit baselines in
this paper:

Pernet, Cyril R. "Misconceptions in the use of the General Linear
Model applied to functional MRI: a tutorial for junior
neuro-imagers." Frontiers in neuroscience 8 (2014): 1.
[link](https://www.frontiersin.org/articles/10.3389/fnins.2014.00001/full).

## How did you create the event .txt files?

The OpenNeuro data does not not come with the `.txt` files giving the
onset, duration and amplitude information for each event type.
I created these files from the overall event definition files for
each task.

For example, here is a listing of the `.txt` files for subject 01:

```
sub-01/func/sub-01_task-onebacktask_run-01_label-objects.txt
sub-01/func/sub-01_task-onebacktask_run-01_label-scrambled.txt
sub-01/func/sub-01_task-onebacktask_run-01_label-strings.txt
sub-01/func/sub-01_task-onebacktask_run-01_label-words.txt
sub-01/func/sub-01_task-onebacktask_run-02_label-objects.txt
sub-01/func/sub-01_task-onebacktask_run-02_label-scrambled.txt
sub-01/func/sub-01_task-onebacktask_run-02_label-strings.txt
sub-01/func/sub-01_task-onebacktask_run-02_label-words.txt
```

I used a Python script to generate these files from the overall event
definition files:

```
sub-01/func/sub-01_task-onebacktask_run-01_events.tsv
sub-01/func/sub-01_task-onebacktask_run-02_events.tsv
```

The script that I used was:

<https://github.com/matthew-brett/ds107-fixes/blob/master/ds107_onsets.py>

As you might be able to see from that script, I had to write small
algorithms to analyze the events, and select the ones corresponding
to the individual trial types.

## Why do I get errors using the mask files with fslmaths?

I'm afraid the masking problem is rather more difficult than I meant
it to be.

### Native and standard space

To understand what's going on, we need to distinguish between:

* native (subject) space;
* standard (template) space.

See this [introduction to coordinate
systems](http://nipy.org/nibabel/coordinate_systems.html) for the
meaning of *space*.  In what follows, I will use the term
*orientation* to refer to the *affine* in the page above.  Read the
page to see what that means.

An image in *native space* has image dimensions, voxel sizes, and
orientation from the images acquired in the scanner.  You can see
this information with the `fslhd` command, that displays the NIfTI
image header.  For example, here's an excerpt from the output of
running `fslhd
/home/data/FBI/assessment/ds107/sub-01/func/sub-01_task-onebacktask_run-01_bold.nii.gz`:

```
sizeof_hdr     348
data_type      INT16
dim0           4
dim1           64
dim2           64
dim3           35
dim4           164
...
pixdim0        0.000000
pixdim1        3.000000
pixdim2        3.000000
pixdim3        3.000000
pixdim4        3.000000
...
sform_name     Scanner Anat
sform_code     1
sto_xyz:1      3.000000  0.000000  0.000000  -93.000000
sto_xyz:2      0.000000  3.000000  0.000000  -103.556091
sto_xyz:3      0.000000  0.000000  3.000000  -51.734001
sto_xyz:4      0.000000  0.000000  0.000000  1.000000
```

The `dim` fields give the image dimensions, in this case 64 by 64 by
35 by 164.  These correspond to the image `shape` in the Python code from the lectures.

The `pixdim` fields give the voxel sizes, in millimetres.  In this
case the voxels are 3 by 3 by 3mm. The TR is also 3, confusingly, so
we see 4 `3.000000` values.

The `sform` fields give the orientation (affine). The orientation
gives the relationship between voxel positions in the image to
millimetre positions in terms of the scanner. See the page above for
more explanation.

Contrast this with an image in *standard* or *template* space. An
image in *standard space* has image dimensions, voxel sizes, and
orientation from a standard template image.  Here are some excerpts
from the output of `fslhd
/usr/local/fsl/data/standard/avg152T1.nii.gz`:

```
sizeof_hdr     348
data_type      INT16
dim0           3
dim1           91
dim2           109
dim3           91
dim4           1
...
pixdim0        0.000000
pixdim1        2.000000
pixdim2        2.000000
pixdim3        2.000000
pixdim4        1.000000
...
sform_name     MNI_152
sform_code     4
sto_xyz:1      -2.000000  0.000000  0.000000  90.000000
sto_xyz:2      0.000000  2.000000  0.000000  -126.000000
sto_xyz:3      0.000000  0.000000  2.000000  -72.000000
sto_xyz:4      0.000000  0.000000  0.000000  1.000000
```

This is a three-dimensional image, with image shape 91 by 109 by 91
and voxel sizes of 2 by 2 by 2mm.  The orientation (affine) gives the
relationship between voxel positions in the template and millimetres
in the standard template space.

As you may have gathered from [the
lectures](https://matthew-brett.github.io/fbi2018/chapters/03/normalization),
*registration* or *spatial normalization* is the process we use to
work out the correspondence between *native space* for a particular
subject, and *template space*.

### Native and template space in FEAT analysis directories

Now let us look at the space of statistics images in your analyses.
If you try a few `fslhd` commands, you will find that:

* first-level statistics images are in native space, even if you have
  specified template registration in FEAT;
* higher-level statistics images are template space.

In fact, if you look closely at the output log of your second-level
analyses, you will see they include execution of the command
`featregapply`, that uses the calculated registration to generate new
copies of some analysis images, transformed to template space.  This
is the command that puts the higher-level analysis images into
template space.

### Using the masks with statistics images

With the background above, we can check the *space* of the mask
images, with e.g. `fslhd
/home/data/FBI/assessment/ds107/lateral_otc_cube.nii`.  You will see
that the mask has the same information as the template image above.
It is in template space.   That makes sense, because the paper
defines the mask coordinates in template space.  Using template space
is the only reasonable thing to do, because we want the mask to apply
to all the subjects, and this will only make sense when we have
transformed the subject data to the same position, shape and size \-
the position, shape and size of the template.

Now consider what should happen if we try to use the mask in an `fslstats` command on a native space image.  After a little reflection, we try it, and find:

```
$ fslstats sub-01_run-01.feat/stats/zstat1.nii.gz -k data/lateral_otc_cube.nii -M
Mask and image must be the same size
```

That is what should happen.  `fslstats` sees that the mask is in a different space to the data, and stops, with an error, because it cannot work out the correspondence of the voxels in the mask to the voxels in the native space data.

There are two basic ways of solving this problem:

1.   Transform the first-level statistics images to standard space,
     using the registration information you already calculated in the
     FEAT run.  Use `fslstats` to apply the original mask to the
     transformed statistics image.
2.   Transform the mask to the subject's native space. using the
     registration information you already calculated in the FEAT run.
     Use `fslstats` to apply the transformed mask to the original
     statistics image.

### Option 2, standard to native, using Featquery

Thanks to Kara Farrar for pointing me to this method.

If you run the Featquery GUI, you will see the option to specify a mask.  Here you can select, for example, the original `lateral_otc_cub.nii` mask.

If you select a first-level FEAT directory as input, you may have
noticed that the output has a sentence at the top, saying something like:

> Mask /home/data/FBI/assessment/ds107/lateral_otc_cube.nii is in
> space of standard.
>
> Image of mask in native space:

As this implies, Featquery found the registration parameters in the FEAT directory, and transformed the mask from standard to native space.  See below for the steps it will have used.

The output image is `mask.nii.gz` in Featquery's output directory,
typically called `featquery`, in the FEAT directory.

### Option 1, native to standard, using Renderhighres

Another GUI option is to use the [Renderhighres](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide#FEAT_Programs) utility.

Try running `Renderhighres` from the terminal.

Notice the capital R.   Select the feat directory, and run.  In your
feat directory, you now have a new sub-directory called `hr` (for
High Res).  This has, among other things, the transformed
`thresh_zstat` images.  Assuming you did uncorrected 0.05
thresholding in your original FEAT run, the `thresh_zstat` images
should be thresholded low enough for you to be able to generate all
the images you need, by applying the mask, and thresholding at
different z values.

### Option 2, standard to native, using flirt

This involves getting down and dirty with the commands that FSL uses for registration.

See [this FAQ entry](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT/FAQ#How_do_I_transform_a_mask_with_FLIRT_from_one_space_to_another.3F) for more background.

Example 1 in the page above shows the command for converting a mask
from native to standard space.  Our option 2 involves going the
opposite way round, transforming from standard to native space.  For
example, here is me doing the transformation for one of my subjects:

```
$ cd ~/replication/sub-01_run-01.feat
$ flirt -in ~/replication/data/lateral_otc_cube -ref example_func
-applyxfm -init reg/standard2example_func.mat -out sub-01_lateral_otc
```

In more detail:

* `flirt` is the FSL registration command.
* `-in ~/replication/data/lateral_otc_cube` tells `flirt` to work on
  the original template space image.
* `-ref example_func` tells flirt the image that has the space that
  it should transform to - our *native* space for this subject.
* `-applyxfm` tells `flirt` to apply a transform it has already
  calculated.
* `-init reg/standard2example_func.mat` points `flirt` at the
  parameters it has already calculated in the FEAT step for
  transforming the template to native space.
* `-out sub-01_lateral_otc` gives the output name for the new
  resampled mask image.

As the page above explains, the resampling process involves taking various averages across voxels in the mask, when these averages involve voxels with 0 and 1, the values will not be 0 or 1, but some value in between.

For that reason, to make the image into a proper mask, with only 0 or 1, you should binarize, using `fslmaths`, e.g.:

```
fslmaths sub-01_lateral_otc  -thr 0.5 -bin sub-01_lateral_otc_bin
```

This mask is in this subject's native space, and will work with
`fslstats` commands.

If you go this route (option 2), remember that each subject has
a different native space.  Therefore, you will have to run these
commands separately for each subject.  If you want to make your
analysis replicable, you should record the commands you used

## Which images should I refer to in my report?

In your output directory for each task, you will likely have image
maps with names like `thresh_zstat1.nii.gz` and
`rendered_thresh_zstat1.nii.gz`.  The `rendered` image is a special
image optimized for display with FslEyes. Prefer the `thresh_zstat`
image when you are choosing images to point to for your report.

## Do I need to get exactly the same answers as the paper?

You will all but certainly find that, if you do your analysis
correctly, you will not get exactly the same answers as the paper.
Just for example, you are using a different version of FSL.  In some
cases, we are really guessing what the authors did, and this is
particularly so for the replication of figure 2, panel D, where it
isn't clear (to me) what voxels the authors were averaging to get
their effect sizes.  I guessed it was all the voxels in the lateral
and ventral cortex regions, but that may be wrong.  You may not have
exactly the same set of subjects as the authors used here.

So, all the marks for the replication are for the correct procedure,
giving a valid answer for the data you have.

## I've run out of disk space on the cluster.  What should I do?

1. Try cleaning up any temporary files.
2. If that doesn't work, you can email Charnjit Sidhu at
   pbic-computing@contacts.bham.ac.uk to ask for a bigger quota.  You
   should explain what you have done in step 1 above, to clean out
   old files.

## How do I copy my Word / other files from my laptop to the cluster?

### On Windows

  * Go to: https://winscp.net/eng/download.php
  * Download and install the "Installation package".  Choose all the
    default options.
  * Start WinSCP and enter your details to log into the cluster, like
    this:

    ![](images/winscp_login.png)

    Obviously you'll need your own username, instead of mine, which
    is `brettmz`.

  * A new window with two panes will open.  The left hand pane refers
    to your laptop, the right to the filesystem on the cluster.  Use
    the left pane to navigate to the directory containing the file
    you want to upload, then drag it to the `replication` directory
    in the right pane.

### On Mac

  * Open Terminal.app.  You now have a terminal running on your Mac.
    Make sure that you haven't accidentally picked up a Terminal.app
    session that is already logged into the cluster, by typing
    `hostname`.  It should show the name of your Mac, and not
    `pbic.bham.ac.uk`.
  * Use `cd` to navigate to the directory containing the file you
    want to upload.  For example, if you document was in the
    `Documents` folder in your home directory, you could type `cd
    ~/Documents`.  If you're stuck working out how to get to that
    directory, try opening a Finder window, then navigate to the
    directory containing the file you want to transfer, and drag the
    file to the Terminal window.  Its path (position on the file
    system) should appear in the Terminal window.
  * Use `scp` to copy the file to the cluster - e.g.

    ```
    scp README.docx xxx@pbic.bham.ac.uk:replication
    ```

    where `xxx` is your username.

    This will start a copy of the `README.docx` file to the
    `replication` directory on the server.  The server will ask for
    your password to finish the copy.
