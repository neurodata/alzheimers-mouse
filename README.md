# Network Biomarkers of Alzheimer’s Disease Risk

This repository corresponds to the a project for identifying network biomarkers predictive of Alzheimer's disease risk in mice. Our work takes the unique approach of performing a joint analysis of volume and texture covariance models. Our unique multivariate approach allows us to identify coordinated changes in both volume and texture that influence disease risk, whereas typical approaches tend to analyze biomarkers in isolation. 

## Contents

- [Abstract](#abstract)
- [Repo Contents](#repo-contents)
- [System and Software Requirements](#system-and-software-requirements)
- [Installation Guide](#installation-guide)
- [Results and figure reproduction](#results-and-figure-reproduction)
- [Issues](https://github.com/neurodata/alzheimers-mouse/issues)
- [Citation](#citation)

# Abstract

There are no effective cures for Alzheimer’s disease (AD), which is usually detected too late to allow for interventions to revert pathological changes and their effects. It is thus important to advance our ability for early detection, to understand what confers risk for AD and what are the downstream effects of such risk factors. Animal models provide excellent tools to study prodromal stages. We use mice modeling on various levels of genetic risk for AD, by expressing the three major human APOE alleles, instead of the mouse APOE. Our neuroimaging strategy employed high resolution magnetic resonance diffusion imaging, due to its ability to provide multiple parameters that can be analysed jointly. We have examined how the association between APOE genotype, age, sex, diet and immunity interact to alter the interaction between different regional brain volumes and regional fractional anistropy, as a sensitive metric for modeling changes in water diffusion within the brain. Our approach uses joint network modeling to reveal system changes in multiple regions. Our results reveal genotype has a strong impact on the caudate putamen, pons, cingulate cortex, and cerebellum, while sex impacted the amygdala and piriform cortex bilaterally. Immunity impacted a large number of regions, including the parietal association cortices, thalamus, auditory cortex, V1, and the dentate cerebellar nuclei bilaterally. The interaction of risk factors had a strong impact on the amygdala, thalamus and pons.  Mice on a regular diet with the APOE2 genotype showed the least changes over time, denoting resilience. On the other hand, a high fat diet affected APOE3 genotype mice the least. HFD accentuated the effect of aging, affecting a large number of regions. The interaction of AD risk factors including diet revealed a role for the periaqueductal gray, pons, amygdala, inferior colliculus, M1 and the ventral orbital cortex. Our approach allows the detection of simultaneous variations in brain volume and texture, e.g. fractional anisotropy. Further studies should explore the mechanisms behind these coordinated changes in volume and texture, perhaps through examining network similarity in gene expression, metabolism, and relating those to structural pathways that allow for neurodegenerative disease propagation.

# Repo Contents
- [data](./data): Pre- and post-processed data from the mice.
- [docs](./docs): Functions used to process and analyze the data.
- [figures](./figures): Figures and summary tables used during exploratory analysis phases of the work.
- [pkg](./pkg): A mini python package comprising useful helper functions for plotting.
- [results](./results): Figures and summary tables produced via statistical inference of mouse data.

# System and Software Requirements

The analyses for this work require only a standard computer with enough RAM to store and analyze the mouse volume and texture covariance matrices in memory. Our analysis was performed with a computer with the following specs:

- RAM: 32 GB
- CPU: 8 hyper-threaded cores (16 threads), 3.0 GHz/thread

Analyses were performed on a MAC laptop (Ventura 13.1), with python version `3.11.2`. 


# Installation Guide

We recommend first cloning this repository locally via `ssh`:

```
$ git clone git@github.com:neurodata/alzheimers-mouse.git
```

Then, we recommend isolating a virtual environment with an appropriate python version. With this environment activated, you can install the dependencies of the project with:

```
$ cd alzheimers-mouse
$ pip install poetry  # install poetry if necessary
$ pip install .
```

This will set up the project within your virtual environment using the [pyproject.toml](./pyproject.toml) file. 

# Results and Figure Reproduction

See [the docs](https://github.com/neurodata/alzheimers-mouse/main/docs) for instructions to reproduce figures from Bridgeford et al. (2025). 

# Citation

We encourage the repurposing of our code and insights for subsequent works. Please cite according to the enclosed [citation.bib](./citation.bib).
