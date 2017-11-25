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

## Study replication

You will each get instructions pointing to a dataset from the [OpenFMRI
project](https://www.openfmri.org).  In these instructions, we give you the
particular analysis that we want you to replicate, and the form it should take.

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

When you have finished the assignment, you will have filled out that file with
all the instructions necessary for someone else to replicate your analysis.
The specific "Someone else"s will be us, your instructors.

We highly recommend that you edit the `README.txt` file, but if you prefer,
you can also record the instructions in a Word file, which should be called:

```
/home/people/xxx/replication/README.docx
```

If you do use a Word file instead of the `README.txt` file, please copy the
current contents of the `README.txt` file to the Word document, and delete the
`README.txt` file.  If we find both, we will assume you meant us to read the
Word document.

Your job is to:

* read the file `/home/people/xxx/replication/data/INSTRUCTIONS.txt`.  It has
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
  easier for us, your replication reviewers;
* be careful to record your steps explicitly: steps that might seem obvious to
  you, may not be as obvious to us, your instructors.

## Submission

**Submission is automatic at noon January 8th**

At noon on January 8th, we will make a read-only copy of your directory
`/home/people/xxx/replication`. So, *before 12:00 of January 8th* make sure
that:

* the `README.txt` / `README.docx` files are up to date;
* all the analyses comprising the replication have been run inside that
  folder, and the results files referred to in the README file are available
  for your instructors to look at.

### Marking

We will mark you out of 100 on the following basis:

* Is the description of what you did clear?
* Have you justified all the steps of your analysis?
* Did you make any analysis errors?
* How easy is it to exactly replicate your analysis? You will get maximum
  marks if we can run a script to replicate the analysis given only the raw
  data that you have linked at `/home/people/xxx/replication/data` along
  with any script files or library code in your directory.
* Did you successfully replicate the original findings?  Or successfully show
  that the original findings are unlikely to be correct?
