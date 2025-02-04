## Exploratory Analyses and Data Post-Processing

This folder contains two files:

- [Figure2.ipynb](./Figure2.ipynb): conducts exploratory analyses of the difference matrices for volume and FA of the mouse connectomes.
- [embedding.ipynb](./embedding.ipynb): computes the pairwise difference matrices region-wise for each mouse over volume and FA, and then embeds the resulting difference matrices using the omnibus embedding separately for the mouse volume and FA difference matrices. This creates the derivatives [fa_embed.npy](https://github.com/neurodata/alzheimers-mouse/blob/main/data/embeddings/fa_embed.npy) and [vol_embed.npy](https://github.com/neurodata/alzheimers-mouse/blob/main/data/embeddings/vol_embed.npy), which are subsequently used for statistical inference.
