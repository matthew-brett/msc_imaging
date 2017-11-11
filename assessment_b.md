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

Assessment B has three parts:

1. *initial replication*: make a reproducible replication of a published analysis
   on a dataset we will allocate to you.  The deadline to complete this step
   is December 15th. Each member of your group will get a different analysis
   to work on.  We will mark you on this replication, using the criteria below;
1. *replication review*: write a report on a replication by an fellow student
   in your group.  You will be the *replication reviewer* for your fellow. Fix
   any problems you find.  The deadline for the replication review is 4
   January 2017.  You should let your fellow student know about any problems
   as you find them, they will need the information to improve their analysis
   for the third part;
1. *replication update*: using the feedback from your own replication
   reporter, fix any errors and explain any points that are not clear.  Your
   changes should be complete by 4 January 2017. We will mark this replication
   update using the same criteria as the initial replication, and give you 75%
   of the marks that you recover (see below).

Your job in the replication review is to do the best job you can in finding
mistakes, so that your fellow student can recover the most marks in the
replication update.  Remember, if you miss a problem, and we (your
instructors) find it, this will mean your fellow will not have a chance to fix
the problem and recover the marks.

## Part 1: study replication

You will each get instructions pointing to a dataset from
the [OpenFMRI project](https://www.openfmri.org).  In these instructions, we
give you the particular analysis that we want you to replicate, and the form
it should take.

If you log onto the PBIC server, you will find you have a folder:

```
/home/people/xxx/replication
```

where `xxx` is your University of Birmingham ADF username.

Inside that folder you will find a symbolic link:

```
/home/people/xxx/replication/data
```

The link points to a read-only directory, with a copy of the OpenFMRI data
that you will be analyzing, along with a file called `INSTRUCTIONS.txt` giving
you more instructions on what you should replicate, and which data we have
given you.

You will also find a near-empty text file:

```
/home/people/xxx/replication/README.txt
```

When you have finished the first past of the assignment, you will have filled
out that file with all the instructions necessary for someone else to
replicate your analysis.  The specific "Someone else"s are your future fellow
student reviewer, and us, your instructors.

We highly recommend that you edit the `README.txt` file, but if you prefer,
you can also record the instructions in a Word file, which should be called:

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
  easier for your replication reviewer;
* be careful to record your steps explicitly: steps that might seem obvious to
  you and to the rest of your group, may not be as obvious to us, your
  instructors.

### Meanwhile, you can nominate potential reviewers

When you start your assignment, we will send out a list of the projects
allocated to each student.

If you like, you can choose up to 3 students on the this list as potential
reviewers for your replication, in the second phase.  The people you nominate
cannot be replicating the same analysis that you are working on.  You may
already know that it is not uncommon for authors submitting articles to nominate reviewers.

Submit your nominations by midnight on December 14th, by emailing Matthew at
m.brett@bham.ac.uk.

For the second phase, starting on December 15th, we will allocate you a
reviewer.  We will try to give you one of your nominees, but we reserve the
right to give you another student, if we can't match you with one of your
nominees.

If you don't nominate anyone, we will give you a reviewer at random (given the
constraints of the people who have nominated).

### Submission

**Submission is automatic at midnight December 15th**

At midnight of December 15th, we will make a read-only copy of your directory
`/home/people/xxx/replication` to `/home/FBI_assessment/xxx/replication`.
Only you and your replication reviewer will be able to read this directory.
So, *before 24:00 of December 15th* make sure that:

* the `README.txt` / `README.docx` files are up to date;
* all the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the README file are available
  for your replication partner to look at.

### Marking

We will mark you out of 70 on the following basis:

* is the description of what you did clear?
* have you justified all the steps of your analysis?
* did you make any analysis errors?
* how easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along
  with any script files or library code in your directory.
* did you successfully replicate the original findings?  Or successfully show
  that the original findings are unlikely to be correct?

As you'll soon see, if you lose marks here, you'll have a chance to get most
of them back in the replication update below.

## Part 2: replication review

We will tell you whose project you are reviewing on December 18th.

Say the colleague you are reviewing for has PBIC username is `yyy`.  Your
username is `xxx`.  You will also now have read access to their
`/home/people/yyy/replication` directory and its read-only snapshot at
`/home/FBI_assessment/yyy/replication`.  You will also find you have a
read-write personal copy of the analysis at
`/home/people/xxx/replication_review`.  Inside you will find a file called
`REPLICATION_REVIEW.txt`.  This is where you will fill out your replication
review.  As for the README file, you can instead make a file
`REPLICATION_REVIEW.docx` in Word format.  Your colleague will also be able to
read this directory.

Your job is to:

* replicate your partner's analysis in your new folder
  `/home/people/xxx/replication_review`;
1. write a replication review, in which you describe any problems that came
   up, and how you fixed them. This is most usefully done by negotiation with
   your partner.

The replication report `REPLICATION_REVIEW.txt` should follow the same scheme
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

However, we encourage you to negotiate with your fellow, and work together to
fix any problems that you find.  For each problem you find:

* make sure that you agree with your fellow that this is an error.  If you
  don't agree, contact Matthew Brett <m.brett@bham.ac.uk> for a decision.
  Note that you agree with your replication partner (or that Matthew agreed).
* write a diagnosis of the problem;
* write a description of the fix.

Your aim is to describe how your replication partner could best recover all
the marks you think they will lose for their original replication.

If your fellow has written a particularly good initial report, without
significant errors, please suggest extensions to their replication.

Remember that, if you miss problems in your fellow's replication, you will
lose marks for your report (because you missed a problem), and they will lose
marks for their final replication, because they may well not have found the
problem, and therefore won't be able to fix it.

### Submission

**Submission is automatic at midnight January 4th**

At midnight of January 4th, we will make a read-only copy of your directory
`/home/people/xxx/replication_review`. Make sure that:

* the `REPLICATION_REVIEW.txt` / `REPLICATION_REVIEW.docx` files are up to date;
* all the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the `REPLICATION_REVIEW` are
  available for us to look at.

### Marking

The marks are out of 30, for:

* your progress in replicating the initial replication. We will take into
  account how difficult this replication was, given the the initial
  replication;
* the quality and accuracy of the the suggestions you make for improvement;
* if there wasn't much room for improvement (the initial replication was well-
  done and well-described), then we will look at your suggestions for
  extensions to the replication.  We will be particularly impressed if you
  carry out the extensions you suggest.

# Part 3: replication update

Meanwhile, your replication reviewer will be feeding back to you about your
own replication.

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
  for your instructors to look at.

### Marking

We will mark your replication update according to the same rubric as your
original replication.

If your mark increases, we will take the increase, and add 75% of it to your
original replication mark, to give your final replication mark.

Call your original replication mark `R`.  Call your updated replication mark
`U`.  Your *recovered marks* are `U - R`. Your final replication mark is `R +
(U - R) * 0.75`.

To give a specific example: if your original replication mark was 35 out of
70, and your updated replication mark was 60, then your final replication mark
is 35 + (60 - 35) * 0.75 = 53.75 out of 70.

## Marking overall

Your overall mark is out of 100 and is your *final replication mark* (out of
70), plus the mark for your replication review (out of 30).
