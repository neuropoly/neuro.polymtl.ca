# MSc \| PhD \| PostDoc Positions

NeuroPoly Lab (Polytechnique, University of Montreal) is located in Montreal, best student-city in the world! \([https://www.topuniversities.com/city-rankings/2017](https://www.topuniversities.com/city-rankings/2017)\). We develop advanced MRI image analysis techniques using deep learning and distribute them as open-source software. In collaboration with neuroradiologists and world experts in deep learning (Mila), we apply these tools in patients with traumatic injury and neurodegenative diseases (multiple sclerosis, ALS, etc.).

We are recruiting Master/PhD students and Postdoc fellows to work on various projects:

## Machine learning projects ⚙️

These projects are done in partnership with [Mila](https://mila.quebec/), with possible co-supervision from Mila profs.

`data science` | `deep learning` | `computer vision` | `segmentation` | `medical applications`

### Generalization of deep learning models

![lifelong_learning](../_media/project_geneneralization.png)

* **Description:** Most deep learning segmentation methods work for a specific data domain (eg: hospital, acquisition parameters, patient demographics). This strongly limits the dissemination of advanced solutions across various clinical and research centers. Some solutions, such as transfer learning, require the user to train a model, which is not realistic in a "real world" clinical scenario, where clinicians neither have the time nor the expertise to train models that work for their datasets. The goal of this project is to find solutions to make deep learning segmentation models work for a *large* variety of datasets. Few avenues include:
  * Incorporation of prior constraints from MRI physics during training;
  * Synthesizing images during data augmentation;
  * Careful selection of heterogeneous dataset;
* **Skills**: `deep learning` | `computer vision` | `python` | `git/GitHub`
* **Related projects**: [ivadomed](https://ivadomed.org)
* **Relevant publications**: [Lemay et al. MIDL 2021](https://arxiv.org/pdf/2102.09582.pdf)
* **Contact**: [Julien Cohen-Adad](mailto:jcohen@polymtl.ca)


### Uncertainty estimation and applications

  * Incorporating uncertainty measures to deal with inter-rater variability
  * Using uncertainty in active learning framework for histology and medical data segmentation
  * Use [DeepSeg method](https://arxiv.org/abs/2011.09041) to encode uncertainty.

### Lifelong learning of multiple sclerosis lesion segmentation

![lifelong_learning](../.gitbook/assets/continual_learning_ms_segmentation.png)

* **Description**: The goal of this project is to implement a comprehensive and sustainable analysis framework for the segmentation of multiple sclerosis (MS) lesions in the brain and spinal cord. Deep learning models will be continuously updated with new data being prospectively acquired across several clinics in Canada. We will validate the clinical relevance of these models as a sensitive biomarker of disease severity and prognosis. The project focuses on three aims (the potential candidate student can pick the aim they are most interested in): 
  * Create a general model for brain and spinal cord MS lesion segmentation, robust to hospitals, MRI vendor and acquisition parameters; 
  * Implement a continuous learning framework and assess stability of model performance over time  using a retrospective database; 
  * Demonstrate the clinical relevance of automatic segmentation-based biomarkers.
* **Skills**: Python programming | git/GitHub | deep learning | data science | (computer vision)
* **Related projects**: [ivadomed](https://ivadomed.org), [SCT](https://spinalcordtoolbox.com/)
* **Contact**: [Julien Cohen-Adad](mailto:jcohen@polymtl.ca)

### Software Development for `ivadomed`

### Other projects

* **Segmentation of axons and myelin from histology**
  * Description: Segment axons and myelin sheath \(two different labels\) from large-scale histology data, in order to create microstructure atlas of the human central nervous system \(example: see BigBrain project: [https://bigbrain.loris.ca](https://bigbrain.loris.ca/)\). Dataset: Electron microscopy and optical imaging, with about 15,000 axons and myelin sheath manually segmented.
  * Skills: Deep learning \| Image analysis \| Python \| git/GitHub
  * Related to: [AxonDeepSeg](https://axondeepseg.readthedocs.io/) \| [ivadomed](https://ivadomed.org/)
* **Implementing open-source AI solutions**
  * Bringing AI methods into clinical radiology routine via user-friendly software solutions;
  * Contribution to medical AI framework [ivadomed](https://ivadomed.org/)


## Neuroimaging projects 🧠

`analysis pipeline` | `biomarker` | `reproducibility` | `data science` | `computer vision` | `medical application` | `multiple sclerosis` | `spinal cord injury`

### Analysis of MRI data from multiple sclerosis patients

![ms_lesion_pipeline](../_media/project_ms_lesion_quantification.png)

* **Description**: Better understanding of multiple sclerosis (MS) and its diagnosis is key for the development of personalized therapy. MRI is an important diagnosis tool, but the use of advanced biomarkers is complex and requires further methodological development for it to be used by clinicians. The goal of this project is to develop and apply an pipeline for the analysis of MRI data from MS patients. The dataset consists of >1,000 patients coming from >12 international hospitals, with MS lesions labeled by neuroradiologists. Potential candidates can work on either of these sub-projects:
  * Set up an analysis pipeline to automatically process MRI scans, perform quality control of the analysed datasets (eg: identify failed automatic processes and find solutions);
  * Interpret the results with the help of neurologists, perform statistics to find best biomarkers from MRI data (eg: spinal cord cross-sectional area, MS lesion load).
* **Skills**: `image analysis` | `python` | `git/GitHub` | `analysis pipeline` | `computer vision` | `statistics`
* **Related projects**: [ivadomed](https://ivadomed.org), [SCT](https://spinalcordtoolbox.com/)
* **Relevant publications**: [Kerbrat et al. Brain 2020](https://pubmed.ncbi.nlm.nih.gov/32572488/), [Eden et al. Brain 2019](https://pubmed.ncbi.nlm.nih.gov/30715195/)
* **Contact**: [Julien Cohen-Adad](mailto:jcohen@polymtl.ca)

### Software Development for SCT


### Diffusion Tensor Imaging (DTI) for Radiotherapy Treatment Planning of Glioma
  * **Description**: We are recruiting an MSc student to work on DTI-based tractography for predicting paths of tumor spread during radiotherapy treatment planning of gliomas. Research will be conducted at the NeuroPoly (Polytechnique, University of Montreal, [www.neuro.polymtl.ca](http://www.neuro.polymtl.ca/)\), and in collaboration with the Radiation Oncology department of the McGill University Health Center (MUHC).
  * **Skills**: MRI (acquisition and analysis) \| Radiotherapy \| Cancer
  * **Contact**: [Eva Alonso-Ortiz](mailto:eva.alonso-ortiz@polymtl.ca)



## MRI Physics projects 🧲

`mri` | `physics` | `rf coils` | `shimming` | `biophysical modeling`

### Realtime shimming with MRI
 
* **Description**: Building on our recent progress on integrated shim coils and real time shimming technology, we are recruiting Master/PhD/Postdoc fellows to work on real time shimming projects applied to the spinal cord at 7T. Research will be conducted at the NeuroPoly lab \(Polytechnique, University of Montreal, [www.neuro.polymtl.ca](http://www.neuro.polymtl.ca/)\), and at the Montreal Neurological Institute \(MNI, McGill University\).
* **Skills**: Ultra-high field MRI | MRI acquisition | Image analysis
* **Related projects**: [Shimming Toolbox](https://shimming-toolbox.org/)
* **More** details [here](https://www.dropbox.com/s/exfteqe66sado2y/20190511_PositionRealTimeShimming.pdf?dl=0)
* **Contact**: [Julien Cohen-Adad](mailto:jcohen@polymtl.ca)

### Vendor-agnostic realtime shimming

* **Description**: Shimming is a procedure that aims at homogeneizing the static (B0) magnetic field in an MRI scanner. When subjects breathe, the B0 fields varies in time and space. Our group has developed methods to mitigate these variations, using external coils. However, it would be nice to be able to do it using the internal gradient and shim coils from the MRI system itself. One difficulty is that a lot of code and access to the hardware on these proprietary systems are restricted. A solution would be to use an RTHawk system, which offers full modularity when driving the MRI system.
* **Skills**: Physics | Familiar with MRI | Computer programming | System integration | Experimentation | Image analysis
* **Related projects**: [Shimming Toolbox](https://shimming-toolbox.org/), [RTHawk environment](https://zenodo.org/record/3675442#.YakntPHMLkE)
* **Contact**: [Julien Cohen-Adad](mailto:jcohen@polymtl.ca)

### B0 Magnetic Field Mapping

* **Description**: We are recruiting MSc/PhD students to work on B0 magnetic field mapping at 3 T and 7 T. Many MRI techniques, such fMRI, DTI, and T2* mapping are highly sensitive to B0 inhomogeneities. B0-related artifacts can be minimized or eliminated if the B0 field distribution is known. Different approaches to measuring the B0 field have been proposed over the years. This project would aim to evaluate different B0 mapping techniques and propose B0 mapping procedures for 3 T and 7 T imaging. Research will be conducted at the NeuroPoly lab (Polytechnique, University of Montreal, [www.neuro.polymtl.ca](http://www.neuro.polymtl.ca/)\), and at the Montreal Neurological Institute (MNI, McGill University).
* **Skills**: Physics | MRI (acquisition and analysis) | Ultra-high field MRI
* **Contact**: [Eva Alonso-Ortiz](mailto:eva.alonso-ortiz@polymtl.ca)


## What profile are we looking for? 👀

* For projects on image analysis \| deep learning:
  * Strong coding skills in Python, use of git/GitHub
  * Passion for open-source software, data science and knowledge sharing ❤️
  * Experience in data science, computer vision and medical imaging is an asset
* For projects on MRI physics:
  * Strong theoretical background in physics
  * Experience in MRI
  * Coding skills in Python/Matlab, use of git/GitHub

## Why you should join us? 

* Join an environment that fosters autonomy, passion and creativity;
* Get the opportunity to take leadership in open-source projects with strong impact in the medical field;
* You will gain **highly** relevant expertise on bleeding edge technologies \(MRI physics, computer vision, A.I., deep learning, etc.\)
* You will be using a state-of-the-art 7T Siemens Terra system
* You will interact with radiologists and neurosurgeons who will apply these techniques
* You will collaborate with top institutions \(Univ. Montreal, McGill, MGH/Harvard, UCL, Oxford, etc.\)

## How to apply? ✍️

* Send requests to the contact person listed under each project. Please include CV, GitHub link, blogs, grades, references. No need to send reminders, we always receive and see your emails.
