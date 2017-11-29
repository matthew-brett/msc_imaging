---
output:
  pdf_document: default
  documentclass: report
  papersize: a4
---
# Fundamentals in Brain Imaging Methods: Assessment B

Updated 12/11/2017

The assessment for this module has two parts: Part A and Part B. You must
complete both parts. This information is for part B only.

## Introduction

We designed this assessment to give you some experience of:

* replicating a published experiment;
* writing up your analysis in a way that can be easily replicated by others
* reviewing and improving another person's analysis.

These skills are useful to you because a typical imaging experiment involves
replicating an existing experiment to make sure you can find the effect that
you want to study, collaborating with others so they can improve and extend
your findings, and then writing up your study so that your reviewers and
readers can check and use your work.

## Parts

Assessment B has three parts:

1. *Initial replication*: You will need to make a reproducible replication of
   a published analysis on a dataset we will allocate to you. Your task is to
   write a report detailing the steps you perform to achieve this. The dataset
   will be randomly selected from one of three possible datasets ($\alpha$,
   $\beta$ or $\gamma$). The deadline to complete this step is December 15th
   2017\.

2. *Replication review*: We will allocate a report from a fellow student to
   review. You will be the *replication reviewer* for this student. It is
   likely that this student will have chosen you as a possible replication
   reviewer (see below). You will need to write a report on their replication.
   As part of the report, find and fix any problems you find. The deadline for
   the replication review is 8 January 2017. This process will not be
   anonymised; you are free to interact with the student whose work you are
   reviewing.  Indeed, you need to let your fellow student know about any
   problems as you find them as they will need this information to improve
   their analysis for Part 3, the replication update. Your task here is to do
   the best you can to find mistakes, so that your fellow student can recover
   the most marks in the replication update. If you miss a problem, and we
   (your instructors) find it, this will mean your fellow student will not
   have a chance to fix the problem and recover the marks. They will lose
   marks but so will you. As the reviewer here, you need to be identifying
   mistakes and possible problems.

3. *Replication update*: using the feedback from your own replication
   reviewer, you will need to fix any errors and explain any points that are
   not clear. Your changes should be complete by 8 January 2017. We will mark
   this replication update using the same criteria as the initial replication,
   and will give you 75% of the marks that you recover (full marking details
   below).

## Part 1: Study Replication

You will each get instructions pointing to a particular dataset from the
[OpenFMRI project](https://www.openfmri.org). In these instructions, we give
you the particular analysis that we want you to replicate ($\alpha$, $\beta$
or $\gamma$), and the form it should take.

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
you more specific instructions on what you should replicate, and which data we
have given you.

You will also find a near-empty text file:

```
/home/people/xxx/replication/REPLICATION.txt
```

When you have finished the first past of the assignment, you will have filled
out the `REPLICATION.txt` file with all the instructions necessary for someone
else to replicate your analysis. Specifically this will need to be for one of
your fellow students who will be your reviewer, and for us, your instructors.
We highly recommend that you edit the `REPLICATION.txt` file, but if you
prefer, you can also record the instructions in a Word file, which should be
called:

```
/home/people/xxx/replication/REPLICATION.docx
```

If you do use a `REPLICATION.docx` Word file instead of the `REPLICATION.txt`
file, please delete the `REPLICATION.txt` file.

You will need to:

* Read the file `/home/people/xxx/replication/data/INSTRUCTIONS.txt`. It has
  instructions specific to the dataset that you are analyzing, and links to
  the matching OpenFMRI dataset.
* Read the additional information about the dataset available at the
  OpenFMRIweb page.
* Read the cited paper for your dataset, to understand the analysis that the
  original authors used.
* Replicate the analysis, as described in the paper, as closely as you can.
* For each analysis step, say why you chose the settings that you have chosen
  (for example, quote the original paper, or say why you chose the option you
  did given the information that you had).
* Record **all** your analysis steps in the `REPLICATION.txt` (or
  `REPLICATION.docx`) file, along with your reasoning for choosing the steps;
* You will quickly find that it is much easier to check and replicate your own
  work if you use scripting for your analyses (Workshop 6). This will also
  make it much easier for your replication reviewer.
* Be careful to record all of your steps explicitly: some steps that might
  seem obvious to you may not be obvious to your reviewer or to us, your
  instructors.  You might find that you can describe the steps to your
  reviewer when they ask, but if we, your instructors, cannot follow the
  steps, you will lose marks.

### Meanwhile, you can nominate potential reviewers

When you start your assignment, we will send out a list of the datasets
allocated to each student for analysis($\alpha$, $\beta$ or $\gamma$). If you
like, you can choose up to 3 students on the this list as potential reviewers
to review your work in Part 2. You may already know that it is common for
authors submitting articles to suggest reviewers to journal Editors. Note that
the student you nominate cannot be replicating the same analysis that you are
working on. 

Submit your nominations by midnight on December 14th, by emailing Matthew at
m.brett@bham.ac.uk.

For the Part 2, starting on December 15th, we will allocate you a reviewer. We
will try to give you one of your nominees, but we reserve the right to give
you another student, if we are unable to match you with one of your nominees.
If you don't nominate anyone, we will give you a reviewer at random (given the
constraints of the people who have nominated).

### Submission

**Submission is automatic at midnight December 15th**

At midnight of December 15th, we will make a read-only copy of your directory
`/home/people/xxx/replication` to `/home/data/FBI_assessment/xxx/replication`.
Only you and your replication reviewer will be able to read this directory.
So, *before 24:00 of December 15th* make sure that:

* The `REPLICATION.txt` / `REPLICATION.docx` files are up to date.
* All the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the REPLICATION file are
  available for your replication partner to look at.

### Marking for Part 1

We will mark you out of 70 on the following basis:

* Is the description of what you did clear?
* Have you justified all the steps of your analysis?
* Did you make any analysis errors?
* How easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along with
  any script files or library code in your directory.  You will lose marks if
  we cannot follow what you did *from your description alone*.
* Did you successfully replicate the original findings? Or successfully show
  that the original findings are unlikely to be correct?

As you will soon see, if you do lose marks here, you will have a chance to
recover most of these marks in Part 3 (replication update) below.

## Part 2: Replication Review

We will tell you whose project you are reviewing on December 18th.

Say the colleague you are reviewing for has PBIC username is `yyy`. Your
username is `xxx`. You will now have read-only access to their
`/home/data/FBI_assessment/yyy/replication` copy.  You will also find you have
a read-write personal copy of the analysis at
`/home/people/xxx/replication_review`. Inside you will find a file called
`REPLICATION_REVIEW.txt`. This is where you will fill out your replication
review.  As with the original `REPLICATION.txt` file, you can instead make a
file `REPLICATION_REVIEW.docx` in Word format. Your colleague will also be
able to read this directory.

You will need to:

* Replicate your partner's analysis in your new folder
  `/home/people/xxx/replication_review`.
* Write a replication review, in which you describe any problems that came up,
  and how you fixed them. This is most usefully done by negotiation with the
  student whose work you are reviewing.

The replication report `REPLICATION_REVIEW.txt`should follow the same general
scheme as for the Part 1 marking section above.  Here is a copy of the
instructions from that section:

* Is the description of what you did clear?
* Have you justified all the steps of your analysis?
* Did you make any analysis errors?
* How easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along with
  any script files or library code in your directory.  You will lose marks if
  we cannot follow what you did *from your description alone*.
* Did you successfully replicate the original findings? Or successfully show
  that the original findings are unlikely to be correct?

We encourage you to negotiate with the student whose work you are reviewing
and to work together to fix any problems that you find. For each problem you
find:

* Make sure that you agree with your fellow that this is an error. If you do
  not agree, please contact Matthew Brett <m.brett@bham.ac.uk> for a decision.
* Note that you agree with the student whose work you are reviewing (or that
  Matthew agreed).
* Write a diagnosis of the problem.
* Write a description of the fix.

Your aim here is to describe how the student whose work you are reviewing
could best recover all the marks you think they will lose for their original
replication.

If the student whose work you are reviewing has written a particularly good
initial report, without significant errors, please note this and then suggest
possible extensions to their replication.

Remember that, if **you** miss problems in your review of the other student's
replication, **you** will lose marks for your report (because you missed a
problem), and **they** will also lose marks for their final replication,
because they may well not have found the problem, and therefore won't be able
to fix it.

### Submission

**Submission is automatic at 12 noon on January 8th**

At 12 noon of January 8th, we will make a read-only copy of your directory
`/home/people/xxx/replication_review`. Make sure that:

* The `REPLICATION_REVIEW.txt` / `REPLICATION_REVIEW.docx` files are up to date.
* All the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the `REPLICATION_REVIEW` are
  available for us to look at.

### Marking for Part 2

The marks are out of 30, for:

* Your progress in replicating the initial replication. We will take into
  account how difficult your replication was, given the the initial
  replication.
* The quality and accuracy of the the suggestions you make for improvement.
* If there wasn't much room for improvement (the initial replication was well-
  done and well-described), then we will look at your suggestions for
  extensions to the replication. We will be particularly impressed if you
  carry out the extensions you suggest.

## Part 3: Replication Update

Meanwhile, in parallel to your work on Part 2, your own replication reviewer
should be giving you feedback about your own replication.

You can continue to work in your original `/home/people/xxx/replication`
folder. Remember, if you need to refer to it, there is a read-only snapshot of
your original replication at `/home/data/FBI_assessment/xxx/replication`.

You should update your `REPLICATION.txt / REPLICATION.docx` file to reflect
any changes you had to make.

For each problem found, you should also append the information above, repeated
here:

* Make sure that you agree with the student reviewing your work that this is
  an error. If you do not agree, please contact Matthew Brett
  <m.brett@bham.ac.uk> for a decision.
* Note that you agree with the student reviewing your work (or that Matthew agreed).
* Write a diagnosis of the problem;
* Write a description of the fix.

### Submission

**Submission is automatic at 12 noon on January 8th**

We will take another snapshot of your directory `/home/people/xxx/replication`
folder at 12 noon on January 8th.  Make sure that:

* The `REPLICATION.txt` / `REPLICATION.docx` files are up to date.
* All the analyses comprising the update replication have been run inside that
  folder, and the results files referred to in the REPLICATION file are available
  for your replication partner to look at.

### Marking for Part 3

We will mark your replication update according to the same rubric as your original replication.

If your mark increases, we will take the increase, and add 75% of it to your original replication mark, to give your *final replication mark*.

Call your original replication mark `R`.  Call your updated replication mark `U`.
Your *recovered marks* are `U - R`. Your final replication mark is then: `R + (U - R) * 0.75`.

To give a specific example: if your original replication mark was 35 out of 70, and your updated replication mark was 60, then your final replication mark is 35 + (60 - 35) * 0.75 = 53.75 out of 70.

## Part B Assessment mark

Your part B assessment mark is out of 100 and comprises your *final
replication mark* (out of 70), plus the mark for your *replication review*
(out of 30).
