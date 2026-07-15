from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

np.random.seed(1)

categories = []
for i in range(1,21):
    categories.append(f"Item {i}")
values = np.random.randint(10, 100, size = 20)
data = pd.DataFrame({
    'Category' : categories,
    'Value'    : values
    })
top_data = data.sort_values(by = 'Value', ascending = False).head(10)

new_data = pd.DataFrame(
    np.random.randn(100,5),
    columns = ['Column A', 'Column B', 'Column C', 'Column D', 'Column E']
    )
corr_new_data = new_data.corr()\

fig, axes = plt.subplots(1, 2, figsize = (15,6))

sns.barplot(
    data = top_data,
    x = "Value",
    y = "Category",
    ax = axes[0],
    palette = "viridis"
)
axes[0].set_title("Top 10 Items By Values.")
axes[0].set_xlabel("Values")
axes[0].set_ylabel("Category")

sns.heatmap(
    data = corr_new_data,
    annot = True,
    cmap = 'coolwarm',
    fmt = '.2f',
    ax = axes[1],
    cbar_kws = {'label' : 'Correlation Coefficient'}
)
axes[1].set_title("Feature Correlation Matrix")

plt.tight_layout()
plt.savefig("two_panel_visualization.png", dpi = 300)
print("File Saved Sucessfully!")
plt.show()
