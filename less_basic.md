% Somewhat less basic FMRI analysis
% Matthew Brett
% November 14th 2017

# Plan of the talk

* regression and the GLM;
* correction for multiple comparisons;
* random effects;
* slice timing;
* registration within subject;
* registration across subjects.

# To follow along

* [https://www.anaconda.com/distribution](https://www.anaconda.com/distribution)
* [https://github.com/matthew-brett/msc_imaging/archive/master.zip](https://github.com/matthew-brett/msc_imaging/archive/master.zip)

# Regression and the GLM;

* The General Linear Model [http://matthew-brett.github.io/teaching/glm_intro.html](http://matthew-brett.github.io/teaching/glm_intro.html)

# Testing at a single voxel

* 
[https://nbviewer.jupyter.org/github/matthew-brett/msc_imaging/blob/master/all_one_voxel.ipynb](https://nbviewer.jupyter.org/github/matthew-brett/msc_imaging/blob/master/all_one_voxel.ipynb)

# Correction for multiple comparisons.

* Bonferroni [http://matthew-brett.github.io/teaching/bonferroni_correction.html](http://matthew-brett.github.io/teaching/bonferroni_correction.html);
* Random Fields [http://matthew-brett.github.io/teaching/random_fields.html](http://matthew-brett.github.io/teaching/random_fields.html)

# Random effects

See:
[https://nbviewer.jupyter.org/github/matthew-brett/msc_imaging/blob/master/random_effects.ipynb](https://nbviewer.jupyter.org/github/matthew-brett/msc_imaging/blob/master/random_effects.ipynb)

# Within-subject registration

* http://matthew-brett.github.io/teaching/optimizing_space.html

# Across subject registration

AKA "spatial normalization"

# Subject 9 from ds114

\centerline{\includegraphics[height=3in]{sub009_rendered.png}}

# Colin Holmes average

\centerline{\includegraphics[height=2.8in]{colin_rendered.png}}

> http://www.mccauslandcenter.sc.edu/mricro/mricron/

# Cingulate cortex

\centerline{\includegraphics[width=5in]{cingulate_extent.png}}

> Pujol et al (2002) NeuroImage 15:847

#

\centerline{\includegraphics[width=4.5in]{cingulate_config.png}}

# Broca

\centerline{\includegraphics[height=3in]{broca_variable.png}}

> Amunts et al (1999) J Comp Neurol 412:319

# Affine transformations

\centerline{\includegraphics[width=4.5in]{affine_transforms.png}}

# Bad transforms

\centerline{\includegraphics[height=3in]{crazy_warping.png}}

# Volumes and surfaces

\centerline{\includegraphics[height=2.75in]{vol_surf_compare.png}}

> Fischl et al (1999) Hum Brain Mapp 8:272

# The end

That's the end of the talk.
