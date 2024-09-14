import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(data):
    """
    Plot a heatmap for the correlation matrix of the data.
    
    :param data: pd.DataFrame, dataset for plotting
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

def plot_feature_distribution(data, feature):
    """
    Plot the distribution of a feature in the dataset.
    
    :param data: pd.DataFrame
    :param feature: str, column name of the feature to plot
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data[feature], kde=True)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()
