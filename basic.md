% Basic FMRI analysis
% Matthew Brett
% October 31st 2017

# Plan of the talk

* imaging, analysis, reproducibility;
* what is an image?
* 3D and 4D images.
* the simplest possible analysis;
* correlation;
* convolution;
* regression and the GLM;
* correction for multiple comparisons.

# Risks for error

Increased risk of false findings for:

1. small sample size (low power);
2. small effect size (low power);
3. large number of tests (analysis bias);
4. greater flexibility in analysis (analysis bias);
5. greater financial interests (analysis bias);
6. larger numbers of groups studying same effects (publication bias);

John P. A. Ioannidis (2005). “Why most published research findings are false.”
PLoS medicine 2 (8): e124.  See also [exposition on Ioannidis 2005](https://matthew-brett.github.com/teaching/ioannidis_2005.html).

# Error in neuroimaging

> I have occasionally asked respected colleagues what percent of published
> neuroimaging findings they think would replicate, and the answer is
> generally very depressing. My own guess is **way** less than 50%.

Nancy Kanwisher (2013) commenting on [Daniel Bor's blog
post](http://www.danielbor.com/dilemma-weak-neuroimaging).

# My straw poll

> Let us say you took a random sample of papers using functional MRI over the
> last five years. For each study in the sample, you repeated the same
> experiment.  What proportion of your repeat experiments would substantially
> replicate the main findings of the original paper?

Answers from people running neuroimaging labs vary from 5% to 50%.

# Images, arrays

See:
https://github.com/matthew-brett/talks/fmri-processing/arrays_and_images.ipynb



# The end

That's the end of the talk.

# A lack of concern

> Computing results are now being presented in a very loose, “breezy” way—in
> journal articles, in conferences, and in books. All too often one simply
> takes computations at face value. This is spectacularly against the evidence
> of my own experience. I would much rather that at talks and in referee
> reports, the possibility of such error were seriously examined.

David L. Donoho (2010). "An invitation to reproducible computational research"
Biostatistics 11(3) p385-8

# Opening the black box

"What I cannot create, I do not understand"

Found on Richard Feynman's blackboard after his death.
