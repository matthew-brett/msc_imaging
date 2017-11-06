# Fundamentals in brain imaging methods, assessment B

The assessment for this module has two parts: Part A and Part B. You must
complete both parts. This information is for part B only.

## Introduction

We designed this assessment to give you some experience of:

* replicating a published experiment;
* writing up your analysis in a way that can be easily replicated by others;
* reviewing and improving another person's analysis.

These skills are useful to you because a typical imaging experiment involves
replicating an existing experiment to make sure you can find the effect that
you want to study, collaborating with others so they can improve and extend
your findings, and then writing up your study so that your reviewers and
readers can check and use your work.

## Parts

This assessment (assessment B), has three parts. The three parts are:

1. *study replication*: make a reproducible replication a published analysis
   using publicly available data.  The deadline to complete this step is
   December 15th;
1. *replicate and extend*: write a report on a replicaton by an (allocated)
   fellow student.  We'll call this fellow student your *replication partner*.
   Fix any problems you find.  When you've finished fixing problems, you may
   be able to move on to extending the replication.  The deadline for the
   replication report is 4 January 2017.
1. *replication update*: your replication partner will be also be attempting
   to replicate your study.  As as result, you may well be editing your own
   analysis, to fix mistakes or make the instructions clearer.  These changes
   should be complete by 4 January 2017.

## Marking outline

You will find the details of how marking works below, but, in outline, the
procedure is:

* We will mark the study replication out of 100 for: how easy is your analysis
  to replicate?; how well did you explain and justify your analysis steps?; is
  your replication correct?  Call this initial mark your *replication mark*.
* In the replicate and extend phase, your job will depend on how well your
  replication partner has done.  You should first replicate their result, and
  fix any problems that you found, letting your partner know as you find
  problems, so they can fix them (see below).  When your partner's replication
  is fully fixed, you can move on to the extension phase, in which we ask you
  to some new (and replicable) analyses based on the your partner's dataset.
  Your mark will depend on how many problems you correctly found and fixed,
  and, if you had time, whether you succeeded in extending the analysis.
* For the replication update, you will have been receiving feedback from your
  replication partner.  With that feedback, you can modify your original
  analysis.  We will mark this modified analysis, and give you 75% of the
  marks that you recovered in the new analysis.  For example, if your original
  replication mark was 50 out of 100, and your replication update mark was 90
  out of 100, your final replication mark would be 50 + (40 * 0.75) = 80 out
  of 100.  Therefore part 3 allows you to recover a large proportion of the
  marks lost in part 1.

## Part 1: study replication

By separate post, you will each get instructions pointing to a dataset from
the [OpenFMRI project](https://www.openfmri.org).  In these specific
instructions, we give you the particular analysis that we want you to
replicate, and the form it should take.

If you log onto the PBIC server, you will find you have a folder:

```
/home/people/xxx/replication
```

where `xxx` is your University of Birmingham ADF username.

Inside that folder you will find a symbolic link:

```
/home/people/xxx/replication/data
```

that points to a read-only directory, with a copy of the OpenFMRI data that
you will be analyzing.

You will also find a near-empty text file:

```
/home/people/xxx/replication/README.txt
```

When you have finished the first past of the assignment, you will have filled
out that file with all the instructions necessary for one of your colleages to
replicate your analysis.

We highly recommend that you edit this file, but if you prefer, you can also
record the instructions in a Word file, which should be called:

```
/home/people/xxx/replication/README.docx
```

If you do use a Word file instead of the `README.txt` file, please delete the
`README.txt` file.

Your job is to:

* read the file `/home/people/xxx/replication/data/README.txt`.  It has
  instructions specific to the dataset that you are analyzing, and links to
  the matching OpenFMRI dataset;
* read the additional information about the dataset available at the OpenFMRI
  web page;
* read the cited paper for your dataset, to understand the analysis that the
  original authors used;
* replicate the analysis, as described in the paper, as closely as you can;
  for each analysis step, say why you chose the settings that you have chosen
  (for example, quote the original paper, or say why you chose the option you
  did given the information that you had).  Record this inform
* record all your analysis steps in the `README.txt` (or `README.docx`) file,
  along with your reasoning for choosing the steps;
* you will quickly find that it is much easier to check and replicate your own
  work, if you use scripting for your analyses.  This will also make it much
  easier for your replication partner.

Note that, until December 16th:

* your `replication` directory can only be read by you, and by the system
  administrators for the system; it cannot be read by your fellow students,
  unless you give them specific permission to do that;
* you will not know who your replication partner is.

### Submission

**Submission is automatic at midnight December 15th**

At midnight of December 15th, we will make a read-only copy of your directory
`/home/people/xxx/replication` to `/home/FBI_assessment/xxx/replication`.
Only you and your replication partner will be able to read this directory.
So, *before 24:00 of December 15th* make sure that:

* the `README.txt` / `README.docx` files are up to date;
* all the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the README file are available
  for your replication partner to look at.

### Marking

We will give you final marks for your initial submission along with the marks
for the other stages (see below).  The marks will be on this basis:

* is the description of what you did clear?
* have you justified all the steps of your analysis?
* did you make any analysis errors?
* how easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along
  with any script files or library code in your directory.
* did you successfully replicate the original findings?  Or successfully show
  that the original findings are unlikely to be correct?

## Part 2: replicate and extend.

On December 16th, we will allocate you as a *replication partner* for another
student.  The allocation will be random, except that your replication partner
will have analyzed a different dataset.

Say your partner's PBIC username is `yyy`.  You will also now have read access
to your replication partner's `/home/people/yyy/replication` directory and its
read-only snapshot at `/home/FBI_assessment/yyy/replication`.  You will also
find you have a read-write personal copy of the analysis at
`/home/people/yyy/replication_partner`.  Inside you will find a file called
`REPLICATE_REPORT.txt`.  This is where you will fill out your replication
report.  As for the README file, you can instead make a file
`REPLICATION_REPORT.docx` in Word format.  Your partner will also be able to
read this directory.

Your job is two-fold (depending on the time you have available):

1. replicate your partner's analysis in your new folder
   `/home/people/xxx/replication_partner`;
1. write a replication report, in which you describe any problems that came
   up, and how you fixed them, probably by negotiation with your partner;
2. if you have time, extend your partner's analysis according to the new
   instructions, that you will find in the file
   `/home/people/xxx/replication_partner/EXTEND_INSTRUCTIONS.txt`.  These
   instructions will give you five extensions you can carry out, each worth 10
   points.  Run the extensions you have time for, and fill out the procedure
   to replicate your extensions in the file
   `/home/people/xxx/replication_partner/EXTEND_README.txt`.  You may also use
   a Word format file
   `/home/people/xxx/replication_partner/EXTEND_README.docx`.

The replication report `REPLICATION_REPORT.txt` should follow the same scheme
as the marking section above.  Repeating here:

* is the description of what you did clear?
* have you justified all the steps of your analysis?
* did you make any analysis errors?
* how easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along
  with any script files or library code in your directory.
* did you successfully replicate the original findings?  Or successfully show
  that the original findings are unlikely to be correct?

However, we encourage you to negotiate with your replication partner, and work
together to fix any problems that you find.  For each problem you find:

* make sure that you agree with your replication partner that this is an
  error.  If you don't agree, contact Matthew Brett <m.brett@bham.ac.uk> for a
  decision.  Note that you agree with your replication partner (or that
  Matthew agreed).
* write a diagnosis of the problem;
* write a description of the fix.

Your aim is to describe how your replication partner could best recover all
the marks you think they will lose for their original replication.

When you have finished doing this, you can move on to extending the analysis,
according to the `EXTEND_INSTRUCTIONS.txt` file.  Fill out the
`EXTEND_README.txt` (or `.docx`) file.

Don't go on to extending the analysis, until you have finished fixing the
original replication.

### Submission

**Submission is automatic at midnight January 4th**

At midnight of January 4th, we will make a read-only copy of your directory
`/home/people/xxx/replication_partner`. Make sure that:

* the `REPLICATION_REPORT.txt` / `REPLICATION_REPORT.docx` files are up to date;
* if applicable, the `EXTEND_README.txt` (or `.docx`) file are up to date.
* all the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the `REPLICATION_REPORT` and
  `EXTEND_README` files are available for us to look at.

### Marking

The marks are out of 50.

The marking will depend on how may problems there are to fix in your partner's
replication.  Remember, you will not know the score we will give to your
partner's replication, so you will have to decide for yourself, where your
partner would likely lose points.

* If your partner's replication would score 50 or less, then all 50 of your
  points from this part must come from fixes to your partner's replication.
* If your partner's replication scores 100, then all 50 of your points must
  come from doing all 5 of the 10 point extensions;
* When your partner's replication would score between 50 and 100, then your
  mark comes from a mixture of your fixes to their work, and the extensions
  that you finished.

To give an example, say you estimate that your partner would get 70 / 100. If
that is true, then you have 30 marks to gain from fixing your partner's
replication, and 20 marks to gain from extending their work.  So you would
spend 60% of your time on fixing their work, and 40% of the time on doing 2 of
the 10 point extensions.

But, let's say you had missed a mistake in their analysis, and in fact they
will get 60 / 100.  First, their mistake may make any of your extensions
incorrect.  Second, this will mean that you can in fact only get a total of 10
points for your extensions; any effort on extensions after 10 points will be
wasted (at least in terms of marks).

# Part 3: replication update

Meanwhile, your replication partner will be feeding back to you about your own
replication.

Continue working in your original `/home/people/xxx/replication` folder.
Remember, you have a read-only snapshot of your replication at
`/home/FBI_assessment/xxx/replication`.

You should update your `README.txt / README.docx` file to reflect any changes
you had to make.

For each problem found, you should also append the information above, repeated
here:

* make sure that you agree with your replication partner that this is an
  error.  If you don't agree, contact Matthew Brett <m.brett@bham.ac.uk> for a
  decision.  Note that you agree with your replication partner (or that
  Matthew agreed).
* write a diagnosis of the problem;
* write a description of the fix.

### Submission

**Submission is automatic at midnight January 4th**

We will take a snapshot of your directory `/home/people/xxx/replication`
folder at midnight on January 4th.  Make sure that:

* the `README.txt` / `README.docx` files are up to date;
* all the analyses comprising the update replication have been run inside that
  folder, and the results files referred to in the README file are available
  for your replication partner to look at.

### Marking

We will mark your replication update according to the same rubric as your
original replication.

If your mark increases, we will take the increase, and add 75% of it to your
original replication mark, to give your final replication mark.

Call your original replication mark `R`.  Call your updated replication mark
`U`.  Your final replication mark is `R + (U - R) * 0.75`.

To repeat the example above: if your original replication mark was 50, and
your updated replication mark was 90, then your final replication mark is 50 +
(90 - 50) * 0.75 = 80.

## Marking overall

Your overall mark is out of 150 and is your final replication mark (out of
100), plus your final replicate and extend mark (out of 50).
