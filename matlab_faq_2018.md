# FAQ for 2018 Matlab assessment

Feel free to propose edits or new questions for this FAQ.

You can do that by email to <m.brett@bham.ac.uk>, or for cool points,
use the pen icon at the top right of the page to make and propose your
edits.  You'll need a Github account for that, but that's a good thing
to have in any case.

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

## I'm still stuck, what now?

Keep thinking of ways to split the task up into stages.

For example, these stages:

* write `generate_sequence` function
* write `deliver_n_back` function
* write `save_run` function
* write `analyze_n_back` function
* write `analysis` script.

If you get stuck on one stage, work on another.

To help you, here a zip file containing [example_response
files](https://github.com/matthew-brett/msc_imaging/raw/master/example_responses.zip).

The zip has the following files, simulating a set of output files from `deliver_n_back` and `save_run` from a single subject:

* `participant_01_1_back.csv`
* `participant_01_2_back.csv`
* `participant_01_3_back.csv`
* `participant_01_4_back.csv`

You can use these to start work straight away on `analyze_n_back` and the `analysis` script.

Remember, `analyze_n_back`, has the following signature:

```{matlab}
fig = analyze_n_back(filename, N)
```

So, you can start right away on `analyze_n_back`, testing with (e.g.):

```{matlab}
fig = analyze_n_back('participant_01_1_back.csv', 1)
```

You can also get going on `deliver_n_back`, without finishing `generate_sequence`, because the example files have example sequences in them.

For example:

```{matlab}
% Get stimulus, desired response from response file
seq_resps = readtable('participant_01_1_back.csv');
% Convert to seq char array
sequence = cell2mat(seq_resps{:, 1:2});
```

Now you can try building up your `deliver_n_back` function, testing with:

```{matlab}
rts, responses = deliver_n_back(sequence);
```

You can also test your `save_run` function, with something like:

```{matlab}
% Get stimulus, desired response from response file
seq_resps = readtable('participant_01_1_back.csv');
% Split into sequence, rts and responses
sequence = cell2mat(seq_resps{:, 1:2});
rts = seq_resps{:, 3};
responses = cell2mat(seq_resps{:, 4})
```

Then:

```{matlab}
save_run('test.csv', sequence, rts, responses)
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

I have given permission for these two functions, as long as you fulfill the other conditions above:

* [getkey](https://uk.mathworks.com/matlabcentral/fileexchange/7465-getkey)
* [getkeywait](https://uk.mathworks.com/matlabcentral/fileexchange/8297-getkeywait)

Also, any code that you see in this document, you can use and edit freely
without conditions.

## Can you give any hints on how to write out the results file?

You may find that it is more difficult to write the results file, than it was
to write the sequences.

This is because Matlab is a little creaky when saving columns of different
types of data to CSV files.  Specifically, you will find that you can't easily
use `csvwrite`.

If you want to use the old-school Matlab functions to solve this problem, have
a look at the [Matlab help for
fprintf](https://uk.mathworks.com/help/matlab/ref/fprintf.html).

Another option is to use the more modern data
[table](https://uk.mathworks.com/help/matlab/ref/table.html).  If you can
create one of those, you will likely find the
[writetable](https://uk.mathworks.com/help/matlab/ref/writetable.html) function
is useful for your task.
