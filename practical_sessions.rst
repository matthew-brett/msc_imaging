##################
Practical sessions
##################

##################
First - workshop 4
##################

FSL single subject analysis

* PAR / REC to nifti conversion (dcm2mii);
* Reorienting the data (fslswapdim);
* BET, robustfov;

FEAT First-level analysis / Full analysis

Preprocessing:

* high-pass filter;
* alternative reference;
* Motion correction;
* B0 unwarping OFF;
* slice timing;
* spatial smoothing;
* perfusion subtraction OFF; highpass checkbox ON
* Melodic OFF

Stats:

* FILM prewhitening: ON
* Motion parameters: Standard
* Voxelwise confound: empty
* External script: empty
* 1 EV, shape "square" convolution Gamma 0, 3, 6
* Contrasts.

Post stats:

* Thresholding: Uncorrected

Registration:

* Brain extracted structural;
* Search BBR (Boundary-Based Registration);
* Normal search 12 DOF;

###################
Second - workshop 5
###################

FSL Higher Level Analysis

Fixed effects, cross sessions, within participant.

FEAT First-level analysis / Higher-level analysis

Schematic of your design.

Mixed effects, cross subjects, cross session designs as input.

FEAT First-level analysis / Higher-level analysis

Registration Summary - not aligned between participants.

Mixed effects, cross subjects, all subject / session fixed effects as input.

##################
Third - workshop 6
##################

Mixed effects: OLS (instead of FLAME 1)

Voxel correction for post-stats.

Cluster correction for post-stats.

t-test vs F-test.

Region of interest / % signal change.

Extraction of time-series from regions.

Scripts

In bash
Bash loops
Perl -pie for changing model files.

