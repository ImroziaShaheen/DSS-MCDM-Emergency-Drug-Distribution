import matplotlib.pyplot as plt
import numpy as np

# Exact data from the manuscript's TikZ/pgfplots code (unchanged)
episodes = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]

HDSRL = [-30, -10, 20, 55, 90, 120, 145, 165, 182, 196, 207, 216, 223, 228, 233, 236, 239, 241, 243, 245, 246]
DQN = [-40, -20, 5, 30, 58, 80, 98, 112, 123, 132, 140, 147, 153, 157, 161, 164, 167, 169, 171, 172, 173]

HDSRL_upper_SD = [-50, -25, 5, 40, 75, 105, 130, 150, 167, 181, 192, 201, 208, 213, 218, 221, 224, 226, 228, 230, 231]
HDSRL_lower_SD = [-10, 5, 35, 70, 105, 135, 160, 180, 197, 211, 222, 231, 238, 243, 248, 251, 254, 256, 258, 260, 261]

DQN_upper_SD = [-60, -40, -15, 10, 38, 60, 78, 92, 103, 112, 120, 127, 133, 137, 141, 144, 147, 149, 151, 152, 153]
DQN_lower_SD = [-20, 0, 25, 50, 78, 100, 118, 132, 143, 152, 160, 167, 173, 177, 181, 184, 187, 189, 191, 192, 193]

# Exact color match to LaTeX xcolor tints/mixes
green_60_black = (0.0, 0.6, 0.0)  # color=green!60!black
blue_70 = (0.3, 0.3, 1.0)          # color=blue!70
green_50 = (0.5, 1.0, 0.5)         # green!50 (SD bounds for HDSRL)
blue_40 = (0.6, 0.6, 1.0)          # blue!40 (SD bounds for DQN)

fig, ax = plt.subplots(figsize=(12 / 2.54, 6.5 / 2.54), dpi=300)  # 12cm x 6.5cm, matching \width, \height

# Main curves: thick (pgfplots "thick" ~ 0.8pt -> using linewidth=1.8 for main lines)
ax.plot(episodes, HDSRL, color=green_60_black, linewidth=1.8, linestyle='-',
         marker='None', label='HDSRL (PPO)')

ax.plot(episodes, DQN, color=blue_70, linewidth=1.8, linestyle='-',
         marker='None', label='Std. DQN')

# SD bound curves: dashed, no explicit "thick" in TikZ -> default thin linewidth
ax.plot(episodes, HDSRL_upper_SD, color=green_50, linewidth=1.0, linestyle='--', marker='None')
ax.plot(episodes, HDSRL_lower_SD, color=green_50, linewidth=1.0, linestyle='--', marker='None')

ax.plot(episodes, DQN_upper_SD, color=blue_40, linewidth=1.0, linestyle='--', marker='None')
ax.plot(episodes, DQN_lower_SD, color=blue_40, linewidth=1.0, linestyle='--', marker='None')

ax.set_xlabel('Training episode', fontsize=10)
ax.set_ylabel('Cumulative reward (smoothed)', fontsize=10)
ax.set_xlim(0, 500)
ax.set_ylim(-50, 300)

ax.grid(True, which='major', linestyle='--', color='gray', alpha=0.4)
ax.set_axisbelow(True)

# legend positioned above the plot, 2 columns (matches legend style={at={(0.5,1.02)}...})
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, fontsize=9, frameon=False)

# Remove top/right spines for a cleaner pgfplots-like look (does not alter data/colors)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save as both PNG (quick preview) and PDF (vector, ready for LaTeX/Overleaf inclusion)
plt.savefig('figure5_learning_curves.png', dpi=300, bbox_inches='tight')
plt.savefig('figure5_learning_curves.pdf', bbox_inches='tight')
plt.show()

print("Figure 5 saved as figure5_learning_curves.png and figure5_learning_curves.pdf")
