# Automatic Spinal Cord Segmentation

Spinal cord segmentation has a tremendous importance for various applications, from surgical planning to neurodegenerative diseases diagnosis/prognosis. However, only a few methods exist that segment the spinal cord automatically and on different types of MR contrasts. The objective of this project is to develop an fully automatic segmentation method for the spinal cord in MR images \(T1-, T2-, T2\*-weighted, dMRI, MTR, etc.\). This method has to manage the variable curvature of the spinal cord as well as contrast variation and artefacts. We have developed this algorithm based on the multi-resolution propagation of deformable models, coupled with local contrast adaptive mechanisms. The automation is provided by an independent spinal cord detection module, giving an approximation of spinal cord position and orientation in the volume. Coupled with an automatic vertebral level identification algorithm, this method provides quantitative metrics of the spinal as cross-sectional areas and volumes in a generic vertebral coordinate system, allowing easy inter- and intra-patient comparisons for large-cohort studies. This method is part of the Spinal Cord Toolbox and is freely available on [http://sourceforge.net/projects/spinalcordtoolbox/](http://sourceforge.net/projects/spinalcordtoolbox/).

![](../../.gitbook/assets/segmentation.png)

## References

> De Leener B, Cohen-Adad J, Kadoury S. Automatic segmentation of the spinal cord and spinal canal coupled with vertebral labeling. IEEE Trans Med Imaging 2015;\(in press\):10.1109/TMI.2015.2437192.

> De Leener B, Kadoury S, Cohen-Adad J. \(2014\) _“Robust, accurate and fast automatic segmentation of the spinal cord”_, Neuroimage, 98, 528-536. doi: [10.1016/j.neuroimage.2014.04.051](http://dx.doi.org/10.1016/j.neuroimage.2014.04.051)

> De Leener B. ; Cohen-Adad J. and Kadoury S., _“Automatic 3D segmentation of spinal cord MRI using propagated deformable models”_, Proc. SPIE 9034, Medical Imaging 2014: Image Processing, 90343R \(March 21, 2014\); doi: [10.1117/12.2043183](http://dx.doi.org/10.1117/12.2043183)

