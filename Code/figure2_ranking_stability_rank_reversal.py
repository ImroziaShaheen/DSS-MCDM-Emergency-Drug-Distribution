import matplotlib.pyplot as plt
import numpy as np

# Exact data and error bars from the manuscript's TikZ/pgfplots code (unchanged)
categories = ['Static Soft', 'STA', 'DSS-TTPA', 'DSS-MTTE']

RS = [78.4, 84.7, 93.6, 91.8]
RS_err = [3.1, 2.8, 1.9, 2.2]

RR = [21.6, 15.3, 6.4, 8.2]
RR_err = [3.1, 2.8, 1.9, 2.2]

# Exact color match to LaTeX xcolor "blue!40" and "red!40" (40% color + 60% white)
blue_40 = (0.6, 0.6, 1.0)
red_40 = (1.0, 0.6, 0.6)

x = np.arange(len(categories))
bar_width = 0.35  # proportionally matches "bar width=18pt" on a 13cm-wide axis

fig, ax = plt.subplots(figsize=(13 / 2.54, 7 / 2.54), dpi=300)  # 13cm x 7cm, matching \width, \height

bars1 = ax.bar(x - bar_width/2, RS, width=bar_width, color=blue_40, edgecolor='black', linewidth=0.6,
                yerr=RS_err, capsize=4, error_kw={'elinewidth': 0.8, 'capthick': 0.8},
                label='Ranking Stability (%)')

bars2 = ax.bar(x + bar_width/2, RR, width=bar_width, color=red_40, edgecolor='black', linewidth=0.6,
                yerr=RR_err, capsize=4, error_kw={'elinewidth': 0.8, 'capthick': 0.8},
                label='Rank Reversal Rate (%)')

# nodes near coords (value labels above each bar) — horizontal, matching
# the default pgfplots "nodes near coords" orientation used in the manuscript
for xi, val, e in zip(x - bar_width/2, RS, RS_err):
    ax.annotate(f'{val:.1f}', xy=(xi, val + e), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom',
                fontsize=6, rotation=0)

for xi, val, e in zip(x + bar_width/2, RR, RR_err):
    ax.annotate(f'{val:.1f}', xy=(xi, val + e), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom',
                fontsize=6, rotation=0)

ax.set_ylabel('Value (%)', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 105)

ax.grid(axis='y', which='major', linestyle='--', color='gray', alpha=0.4)
ax.set_axisbelow(True)

# legend positioned above the plot, 2 columns (matches legend style={at={(0.5,1.02)}...})
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, fontsize=9, frameon=False)

# Remove top/right spines for a cleaner pgfplots-like look (does not alter data/colors)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save as both PNG (quick preview) and PDF (vector, ready for LaTeX/Overleaf inclusion)
plt.savefig('figure2_RS_RR_tikz_match.png', dpi=300, bbox_inches='tight')
plt.savefig('figure2_RS_RR_tikz_match.pdf', bbox_inches='tight')
plt.show()

print("Figure 2 saved as figure2_RS_RR_tikz_match.png and figure2_RS_RR_tikz_match.pdf")
