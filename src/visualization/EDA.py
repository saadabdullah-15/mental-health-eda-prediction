import seaborn as sns
import matplotlib.pyplot as plt


def plot_distribution(df, column):
    """Plots a distribution for a given column."""
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


# Use this script to generate and save plots into reports/figures/.
