# Template of the Spinal Cord

![](../../.gitbook/assets/spinalcord_template.png)



This template was created from T2-weighted images of 16 subjects using the methods described in Aim 2. Then, an existing probabilistic template of the white and gray matter \[95\] was warped to the T2- weighted template using non-rigid deformation implemented in ANTS \[101\]. This probabilistic template was made available to us from our collaboration with the group of Dr. Callot \(CRMBM, Aix- Marseille University, France\). Using the probabilistic white matter template and an existing atlas of spinal pathways \[100\], we created an atlas of spinal pathways that is merged with the template. This atlas consists of 30 different tracts and can be used to extract quantitative MRI metrics within specific pathways. Moreover, this atlas takes into account partial volume effect and hence offers higher accuracy that the current methods, which are based on the gross delineation of white matter tract using a binary regions of interest. The same procedures will be used in this project to create a second version of the template that \(i\) is made from 40 individuals, \(ii\) includes the whole spinal cord and brainstem and \(iii\) includes both T1- and T2-weighted contrasts.

> Fonov V, Le Troter A, Taso M, Leveque G, Benhamou M, Sdika M, Collins DL, Callot V, Cohen-Adad J. MNI-Poly-AMU average anatomical template for automatic spinal cord measurements. Proceedings of the 22th Annual Meeting of ISMRM, Milan, Italy 2014:5358.

> Benhamou M, Fonov V, Taso M, Le Troter A, Sdika M, Collins DL, Callot V, Cohen-Adad J. Atlas of white-matter tracts in the human spinal cord. Proceedings of the 22th Annual Meeting of ISMRM, Milan, Italy 2014:5132

![](../../.gitbook/assets/template_london.png)

Application of template-based analysis in a multi-centre DTI study. This study was initiated by our group and involved three different sites \(Montreal, London, Vanderbilt\) and two manufacturers \(Siemens, Philips\). Five healthy subjects were scanned at each site. The left figure shows the result of the within site-averaged b=0 and fractional anisotropy \(FA\) in a slice centred at the C3 vertebral body. Data from all sites were adequately registered to the template. The right panel shows the white matter tracts selected for quantification from the white matter atlas \(red: left CST, green: right CST, blue: left gracilis, yellow: right gracilis\). Average FA is plotted on the bottom right figure \(L=London, V=Vanderbilt, M=Montreal\). Results of ANOVA on the CST using FA show no effect for site, subject and laterality. Similar results were obtained on other tracts and other metrics. These results suggest a good reproducibility of the template-based method for quantifying metrics in the spinal cord. This preliminary study demonstrates for the first time the feasibility and usefulness of template-based methods for processing spinal cord images across sites and vendors.

> Cohen-Adad J, Samson RS, Schneider T, Smith AK, Benhamou M, Leveque G, Smith SA, Wheeler-Kingshott CAM. Multisite DTI of the spinal cord with integrated template and white matter atlas processing pipeline. Proceedings of the 22th Annual Meeting of ISMRM, Milan, Italy 2014:5004.

