# Reproducibility Notes

## Purpose

This document describes exactly what the supplied repository code reproduces and what it does not.

## Supplied Figure Scripts

| Script | Intended output |
|---|---|
| `code/figure2_ranking_stability_rank_reversal.py` | Figure 2: ranking stability (RS) and rank reversal rate (RR) |
| `code/figure3_ablation_ranking_stability.py` | Figure 3: ablation-study ranking stability |
| `code/figure4_decay_sensitivity.py` | Figure 4: sensitivity to the temporal decay parameter |
| `code/figure5_learning_curves.py` | Figure 5: HDSRL/PPO and standard DQN learning curves |

## What the Scripts Reproduce

The supplied Python files contain the numerical values used in the corresponding plots directly in the source code.

Running the scripts regenerates the visualizations from those stored values using NumPy and Matplotlib.

This is useful for:

- verifying plotted values;
- recreating the manuscript-style figures;
- inspecting the plotting logic;
- modifying labels, dimensions, or export settings.

## What the Scripts Do Not Currently Reproduce

Based on the supplied files, the repository does not currently contain the full upstream experimental pipeline that generated every plotted numerical value.

For example, the Figure 5 script contains the learning-curve values directly rather than training the reinforcement-learning models from scratch.

Therefore, unless additional experimental code and inputs are added, describe this repository as containing **figure-generation/reproduction code** rather than claiming complete computational reproducibility of all underlying experiments.

## Dependencies

The scripts import:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Install them with:

```bash
python -m pip install -r requirements.txt
```

## Output Files and PDF Restriction

Several scripts save both PNG and PDF outputs locally.

The public repository is configured through `.gitignore` to ignore `*.pdf` files. This means locally generated PDF figures and restricted manuscript PDFs should not appear as Git changes in normal Git/GitHub Desktop workflows.

The PNG outputs can be included only if their public distribution is permitted.

## Reproducibility Versions

For stronger long-term reproducibility, record the Python, NumPy, and Matplotlib versions actually used for the publication release.

On Windows, after activating the environment used to generate the final figures, you can record the full environment with:

```powershell
python --version
python -m pip freeze > requirements-lock.txt
```

Only add `requirements-lock.txt` if it reflects the environment actually used for the final reproducible release; do not create an arbitrary lock file from an unrelated computer environment.

## Publication Release

When the code corresponding to the final article is stable:

1. Commit the final verified repository state.
2. Create a Git tag/release such as `v1.0.0`.
3. Record the article DOI in the README and citation metadata once it exists.
4. Optionally archive the public release in a research-software repository that issues a persistent DOI.
