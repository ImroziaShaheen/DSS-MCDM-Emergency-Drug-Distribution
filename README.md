# Dynamic Soft Set-Based MCDM for Adaptive Emergency Drug Distribution

This repository contains Python scripts used to regenerate the figures associated with the research work:

**A Dynamic Soft Set-Based MCDM Framework with Application to Adaptive Emergency Drug Distribution**

## Repository Structure

```text
DSS-MCDM-Emergency-Drug-Distribution/
├── code/
│   ├── figure2_ranking_stability_rank_reversal.py
│   ├── figure3_ablation_ranking_stability.py
│   ├── figure4_decay_sensitivity.py
│   └── figure5_learning_curves.py
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── REPRODUCIBILITY.md
└── requirements.txt
```

## Requirements

The scripts require Python 3 and the following Python packages:

- NumPy
- Matplotlib

Install the required packages with:

```powershell
python -m pip install -r requirements.txt
```

## Running the Figure Scripts

Open PowerShell or Command Prompt in the repository folder and move into the `code` directory:

```powershell
cd code
```

Run the scripts individually:

```powershell
python figure2_ranking_stability_rank_reversal.py
python figure3_ablation_ranking_stability.py
python figure4_decay_sensitivity.py
python figure5_learning_curves.py
```

Each script generates its corresponding figure file(s) in the directory from which it is run.

The generated PNG and PDF figure outputs are excluded from Git tracking through `.gitignore`, so they can be regenerated locally without being added to the repository.

## Reproducibility Scope

The supplied scripts regenerate Figures 2–5 from numerical values stored directly in the Python source files.

They reproduce the plotted figures from those stored values. They should not be described as a complete end-to-end reproduction of the underlying simulation, optimization, or reinforcement-learning experiments unless the full upstream experimental pipeline and source data are also provided.

See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for further details.

## License

The source code in this repository is made available under the Apache License 2.0. See [`LICENSE`](LICENSE).
