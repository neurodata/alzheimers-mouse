from pathlib import Path

from nilearn import plotting
import nibabel as nib
import numpy as np


def get_masked_image(roi_idx):
    p = Path("../data/parcellation/")
    t2 = nib.load(p / "chass_symmetric3_T2.nii.gz")
    parc = nib.load(p / "chass_symmetric3_labels.nii.gz")

    img = parc.get_fdata()
    mask = np.isin(img, roi_idx) * img

    out = nib.Nifti1Image(mask, parc.affine)

    return out
