import matplotlib.pyplot as plt
import numpy as np

# Exact data and error bars from the manuscript's TikZ/pgfplots code (unchanged)
categories = ['No-EW', 'No-PE', 'No-TW', 'Full DSS']
RS = [90.2, 84.3, 88.1, 93.6]
err = [2.1, 2.9, 2.5, 1.9]

# Exact color match to LaTeX xcolor "teal!50" (teal mixed 50% with white)
teal_50 = (0.50, 0.7509803921568627, 0.7509803921568627)

x = np.arange(len(categories))
bar_width = 0.5  # proportionally matches "bar width=22pt" look in an 11cm-wide axis

fig, ax = plt.subplots(figsize=(11 / 2.54, 6.5 / 2.54), dpi=300)  # 11cm x 6.5cm, matching \width, \height

bars = ax.bar(x, RS, width=bar_width, color=teal_50, edgecolor='black', linewidth=0.6,
              yerr=err, capsize=4, error_kw={'elinewidth': 0.8, 'capthick': 0.8})

# nodes near coords (value labels above each bar)
for xi, val in zip(x, RS):
    ax.annotate(f'{val:.1f}', xy=(xi, val), xytext=(0, 6),
                textcoords="offset points", ha='center', va='bottom', fontsize=7)

ax.set_ylabel('Ranking Stability (%)', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(78, 100)

ax.grid(axis='y', which='major', linestyle='--', color='gray', alpha=0.4)
ax.set_axisbelow(True)

# Remove top/right spines for a cleaner pgfplots-like look (optional, does not alter data/colors)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save as both PNG (quick preview) and PDF (vector, ready for LaTeX/Overleaf inclusion)
plt.savefig('figure3_ablation_RS.png', dpi=300, bbox_inches='tight')
plt.savefig('figure3_ablation_RS.pdf', bbox_inches='tight')
plt.show()

print("Figure 3 saved as figure3_ablation_RS.png and figure3_ablation_RS.pdf")
