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

This supports:

- verification of the plotted values;
- regeneration of Figures 2–5;
- inspection of the plotting logic; and
- modification of plotting or export settings.

## Scope Limitation

The supplied files do not constitute a complete upstream experimental pipeline for generating every plotted numerical value from raw inputs.

For example, the learning-curve script contains the plotted learning-curve values directly rather than training the reinforcement-learning models from scratch.

Accordingly, this repository should be described as containing **figure-generation/reproduction code**, not as a complete computational reproduction of every underlying experiment.

## Dependencies

The scripts use:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Install the dependencies with:

```powershell
python -m pip install -r requirements.txt
```

## Generated Outputs

The scripts save their generated figure outputs locally.

The repository's `.gitignore` excludes the generated PNG filenames and all PDF files so that regenerated outputs are not accidentally committed through Git or GitHub Desktop.

## Environment Recording

For stronger long-term reproducibility, record the Python, NumPy, and Matplotlib versions used for the final publication release.

From the environment actually used for the final figures, you can record the installed packages with:

```powershell
python --version
python -m pip freeze > requirements-lock.txt
```

Only add a lock file if it represents the environment actually used for the research release.
