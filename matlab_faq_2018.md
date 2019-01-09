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

## What can I do if I get stuck?

Getting stuck is one of the most common and fundamental problems in
programming.   All programmers struggle with getting stuck.

The trick is to keep moving, somehow.  Do smaller parts of the task.  Try
things any way you can, on paper, with scripts at the interactive prompt, until you understand the problem better, then step back, and see if you can solve the problem, as posed.

For example, if you have having trouble with the `generate_sequence` function,
then try something else to generate the output data, `sequence`.

That is, try anything you like, paper and pencil, Excel, or working from the
Matlab prompt, to generate a 1-back version of `sequence`.  Remember, this is
a two-dimensional matrix (or table, or whatever you want to call it), where
there are 48 (or 24) rows, and each row has a letter to be presented, and
a letter 'T' to say whether this is a target or 'N' to say it is a non-target.

The letters should be at least plausibly random (that is - the subject can't
tell they are not random).

Maybe generate this as a text file, `my_first_sequence.csv`.

Here I make a quick fake `sequence`, with 20 random letters from `abcdef` in
the first column, and random `p` or `q` in the last column.

```{matlab}
% A shape (20, 1) array of letters, starting with spaces
sequence = char(ones(20, 2));
letters = 'abcdef';
indices = randi(length(letters), 20, 1);
sequence(:, 1) = letters(indices);
resps = 'TN';
indices = randi(length(resps), 20, 1);
sequence(:, 2) = resps(indices)
```

Then I save it as a comma-separated value (CSV) file:

```{matlab}
csvwrite('my_first_sequence.csv', sequence)
```

You wouldn't want to use this file exactly, because it doesn't use the right
letters, and the responses don't correspond to real N-back checks.

I could also have made this file in Notepad, or by doing something in Excel.

Now when you want to work on `deliver_n_back`, you can load the sequence file,
and run it with your `deliver_n_back` function.  Here I load the CSV file, ready to use with `deliver_n_back(sequence)`.

```{matlab}
% Generates a Matlab "table" - but you don't need to know about these.
seq_table = readtable('my_first_sequence.csv');
% Convert to cell array
seq_cells = table2array(seq_table);
% Convert to char array
sequence_back = cell2mat(seq_cells)
```

## But what if I'm still stuck?

Keep moving.  Another way to do this, is to start writing your function in
comments.  For example, let's imagine I'm stuck on my `generate_sequence`
function.

I start by making a new file `generate_sequence.m`, like this, that just copies the template from the instructions.

```{matlab}
function [sequence] = generate_sequence(N, n_presentations)
% The arguments to this function are:
%
% * `N` as in the N of N-back.  This should be one of 1, 2, 3, or 4.
% * `n_presentations` should be the number of presentations in the
%   sequence.  In your case this will be 48 or 24, but your function
%   should allow for different lengths of sequences.
%
% The function returns a 2D matrix `sequence`, with `n_presentations` rows (48
% for the full sequences, 24 for the practice sequences), and two columns,
% where the first column is the letter to present (one of
% `BCDFGHJKLMNPQRSTVWXYZ`) and the second is one of `T` or `N` where `T` means
% target and `N` means non-target.

end
```

Then I start to fill out the function with comments listing the things I will
need to do, inside the function.

```{matlab}
function [sequence] = generate_sequence(N, n_presentations)
% The arguments to this function are:
%
% * `N` as in the N of N-back.  This should be one of 1, 2, 3, or 4.
% * `n_presentations` should be the number of presentations in the
%   sequence.  In your case this will be 48 or 24, but your function
%   should allow for different lengths of sequences.
%
% The function returns a 2D matrix `sequence`, with `n_presentations` rows (48
% for the full sequences, 24 for the practice sequences), and two columns,
% where the first column is the letter to present (one of
% `BCDFGHJKLMNPQRSTVWXYZ`) and the second is one of `T` or `N` where `T` means
% target and `N` means non-target.

% Create a char array "sequence" size n_presentations by 2

% Fill the first column with n_presentations random letters from
% `BCDFGHJKLMNPQRSTVWXYZ`.

% Fill the second column with 'T' or 'N', where each value has a
% 33.3% chance of being 'T'

% Remember the first N values can't be targets.

% Go through the letters in the first column, and change them to target
% letters, if the second column has a 'T'

% Think about what do with letters that are targets just due to the initial
% random selection of the letters, but that have 'N' in the second column.

end
```

## I've found a function online that I want to use, can I?

The assessment document says your submission should only use code that you
wrote yourself, or code that is installed by default on the cluster machines.

This is true for the main parts of the task, such as the logic for generating
the stimulus sequence, and delivering the stimuli.  For example, you can't use
anyone else's code to generate the sequence of N-back characters, in
`generate_sequence.m`.

For more peripheral tasks, such as improving stimulus display, you can use
other people's code, as long as you have our explicit prior permission.  We
will generally give you permission if:

* The task you are using the code for is not central to the logic of the
  assessment.
* You point us to the code that you want to use, you use exactly the code you
  point us to, and you give credit to the author and a link to the code, in
  your submitted materials.
* You submit a copy of the code with your assessment materials.

Remember, if you want to use someone else's code in your assessment work, you
have to ask us for permission *before you submit*.  Otherwise, we go back to
the plagiarism rules that you'll see in the assessment document.

## What should my analysis figures have on them?

The assessment document is a bit confused about the analysis outputs, so here is a clarification.

We are expecting that you will generate a single figure, for each combination
of participant and N-back number.

That is, if you have three participants, you will have 3 * 4 = 12 figures.  If
P is the participant, and N is the N-back number, you will have one figure for each of:

* P=1, N=1
* P=1, N=2
* P=1, N=3
* P=1, N=4
* P=2, N=1
...
* P=4, N=4

Each figure will have:

* The reaction time distribution for correct responses for this participant,
  version of the task.
* A display of the mean reaction time for correct responses to targets, for
  this participant, version of the task.
* A display of the mean reaction time for correct responses to non-targets, for
  this participant, version of the task.
* A display of percent correct, for this participant, version of the task.

The display of mean reaction time for correct responses to targets,
non-targets, might be in the form of a bar chart, or box plot.

Your `analysis.m` script will generate all these figures; that is, it will
generate all the figures for participant 1 1-back, participant 1 2-back ...
participant 3 4-back.

The assessment document is confusing (otherwise put, confused) in suggesting
a separate bar chart for the mean reaction times for targets, non-targets, and
percent correct.  Please use the summary above as a correct description of your
task.
