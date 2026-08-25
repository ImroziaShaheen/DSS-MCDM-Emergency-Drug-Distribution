# Dynamic Soft Set-Based MCDM for Adaptive Emergency Drug Distribution

This repository contains Python figure-generation code and permitted supporting materials associated with the research article:

**A Dynamic Soft Set-Based MCDM Framework with Application to Adaptive Emergency Drug Distribution**

> **Manuscript availability:** The manuscript PDF is intentionally **not distributed in this repository** because public sharing of the PDF is not permitted. After publication, readers should access the article through its official publisher page or DOI.

## Repository Contents

```text
DSS-MCDM-Emergency-Drug-Distribution/
├── code/
│   ├── figure2_ranking_stability_rank_reversal.py
│   ├── figure3_ablation_ranking_stability.py
│   ├── figure4_decay_sensitivity.py
│   └── figure5_learning_curves.py
├── figures/                         # Include only figures you are permitted to share
│   ├── graphical_abstract.png
│   ├── figure2_ranking_stability_rank_reversal.png
│   ├── figure3_ablation_ranking_stability.png
│   ├── figure4_decay_sensitivity.png
│   └── figure5_learning_curves.png
├── .gitattributes
├── .gitignore
├── README.md
├── REPRODUCIBILITY.md
└── requirements.txt
```

A completed `CITATION.cff` should be added once the author/citation metadata has been verified. A template is provided separately as `CITATION.cff.example`.

## Requirements

The supplied figure-generation scripts require:

- Python 3
- NumPy
- Matplotlib

Install the Python dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Running the Figure Scripts

From the repository root, run the scripts individually:

```bash
python code/figure2_ranking_stability_rank_reversal.py
python code/figure3_ablation_ranking_stability.py
python code/figure4_decay_sensitivity.py
python code/figure5_learning_curves.py
```

The scripts create figure files in the current working directory.

Some supplied scripts also create PDF versions of figures locally. The repository's `.gitignore` deliberately ignores all `*.pdf` files so that PDFs are not accidentally committed through Git/GitHub Desktop.

## Reproducibility Scope

The figure scripts use numerical values embedded directly in the source code to regenerate Figures 2–5. They therefore reproduce the plotted figures from those stored values.

They should **not** be described as a complete end-to-end reproduction of the underlying simulation, optimization, or reinforcement-learning experiments unless the full experimental pipeline and source data are also made available.

See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for details.

## Figures

The `figures/` directory should contain only image files that you have permission to distribute publicly.

If reuse or redistribution of article figures is restricted, omit the restricted images from the public repository. The code can still be shared independently if you have permission to share the code.

## Manuscript and Submission Documents

The following materials are intentionally excluded from this repository:

- Manuscript PDFs
- Cover letters
- Declaration/submission forms
- ORCID-detail documents
- Reviewer or editorial correspondence
- Other confidential or publisher-restricted files

## Citation

A `CITATION.cff` file should be added after the repository authorship and publication metadata have been verified.

Until the article is formally published, do not invent a DOI, journal citation, volume, issue, page range, or publication date.

After publication, update this section with the official article citation and DOI.

## License

No open-source license should be added until the authors have confirmed that they have the right to license the source code and any included figures.

If no license is present, normal copyright restrictions apply. Public visibility on GitHub by itself does not grant permission for others to reuse the material.

## Repository Versioning

For the version of the code corresponding to the published article, create a tagged GitHub Release such as:

```text
v1.0.0
```

If a persistent software DOI is desired, the public release can later be archived with a research-software archive such as Zenodo.

## Suggested Repository Topics

Useful GitHub topics may include:

- `mcdm`
- `multi-criteria-decision-making`
- `soft-sets`
- `emergency-logistics`
- `drug-distribution`
- `decision-support`
- `python`
- `reproducible-research`
