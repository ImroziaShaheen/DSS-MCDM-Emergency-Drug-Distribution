import matplotlib.pyplot as plt
import numpy as np

# Exact data from the manuscript's TikZ/pgfplots code (unchanged)
rho = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

RS = [89.1, 90.4, 91.8, 93.1, 93.6, 88.1]
RR = [10.9, 9.6, 8.2, 6.9, 6.4, 11.9]
RS_upper_SD = [91.2, 92.5, 93.9, 95.0, 95.5, 90.6]
RS_lower_SD = [87.0, 88.3, 89.7, 91.2, 91.7, 85.6]

# Exact color match to LaTeX xcolor tints
blue_70 = (0.3, 0.3, 1.0)   # color=blue!70
red_70 = (1.0, 0.3, 0.3)    # color=red!70
blue_40 = (0.6, 0.6, 1.0)   # color=blue!40 (dashed SD bounds)

fig, ax = plt.subplots(figsize=(12 / 2.54, 6.5 / 2.54), dpi=300)  # 12cm x 6.5cm, matching \width, \height

# RS main line: mark=*, thick
ax.plot(rho, RS, color=blue_70, marker='o', markersize=6, markerfacecolor=blue_70,
         markeredgecolor=blue_70, linewidth=1.8, linestyle='-', label='RS (%)')

# RR main line: mark=square*, thick
ax.plot(rho, RR, color=red_70, marker='s', markersize=6, markerfacecolor=red_70,
         markeredgecolor=red_70, linewidth=1.8, linestyle='-', label='RR (%)')

# RS upper SD: dashed, mark=none
ax.plot(rho, RS_upper_SD, color=blue_40, linewidth=1.2, linestyle='--',
         marker='None', label='RS upper SD')

# RS lower SD: dashed, mark=none
ax.plot(rho, RS_lower_SD, color=blue_40, linewidth=1.2, linestyle='--',
         marker='None', label='RS lower SD')

ax.set_xlabel(r'Decay parameter $\rho$', fontsize=10)
ax.set_ylabel('Value (%)', fontsize=10)
ax.set_xticks(rho)
ax.tick_params(axis='x', labelsize=9)
ax.set_ylim(0, 100)

ax.grid(True, which='major', linestyle='--', color='gray', alpha=0.4)
ax.set_axisbelow(True)

# legend positioned above the plot, 2 columns (matches legend style={at={(0.5,1.02)}...})
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, fontsize=9, frameon=False)

# Remove top/right spines for a cleaner pgfplots-like look (does not alter data/colors)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save as both PNG (quick preview) and PDF (vector, ready for LaTeX/Overleaf inclusion)
plt.savefig('figure4_sensitivity_decay.png', dpi=300, bbox_inches='tight')
plt.savefig('figure4_sensitivity_decay.pdf', bbox_inches='tight')
plt.show()

print("Figure 4 saved as figure4_sensitivity_decay.png and figure4_sensitivity_decay.pdf")
