# FAQ for 2018 Matlab assessment

Feel free to propose edits or new questions for this FAQ.

You can do that by email to <m.brett@bham.ac.uk>, or for cool points, use the
pen icon at the top right of the page to make and propose your edits.  You'll
need a Github account for that, but that's a good thing to have in any case.

## What do you mean "roughly equal chance" of stimulus presentation?

In the assessment document, you will find:

> Each letter in the stimulus set should have a roughly equal chance of being
> presented.

and:

> The order of presentation of the letters should be random, within the
> constraint of 33% targets.

More specifically, the chances of any one stimulus, should be sufficiently
random, that the subject is not aware of any pattern in the stimuli, or that
there are any stimuli that occur more or less often.

You may find yourself running the same subject again, on the same version of
the task.  In that case, a good solution would be to make sure that the
presentation order, for the second presentation, was not the same as the
presentation the first time you present that version of the task.

## Can I use "X" where "X" is a Matlab toolbox

You can use any Matlab toolbox that is installed by default on the machines in
the B24 computer cluster.

You should use the specific version installed on the cluster.

You can't use any toolbox that is not installed on the cluster.

Specifically, you *can* use *Psychtoolbox*, because it is installed on the
cluster.   The installed version of Psychtoolbox is 3.0.12.

If you do use Psychtoolbox, please make sure that your experiment runs as you
expect, without errors, *on the cluster machines*.  It can be difficult to get
Psychtoolbox working the same way on different computers, and particularly, on
different platforms, such as Windows and Mac.   We weakly recommend that you
do not use Psychtoolbox, for that reason.

## What should I display between stimuli?

You can display a blank screen between the stimuli, if you like, or a fixation
cross.   Choose the option that gives the best results in terms of helping the
participants concentrate on the task.

## Isn't the assessment doc wrong about when the first target can happen?

Yes it is.  The assessment doc says:

> You should discard the first N-1 trials from your analysis, because the
> subject will know these cannot be targets.  For example, for the 4-back
> task, the subject will know that presentations 1, 2, and 3 cannot be
> targets.

As Justin Chung pointed out, this is wrong, and you should discard the first
N trials.  The first trial number that a target can appear is N + 1, and
therefore the first N trials cannot be targets.  For example, for a 1-back
task, the first trial cannot be a target, but the second trial can (trial
N + 1)
