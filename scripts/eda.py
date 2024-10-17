import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # Ensure pandas is imported

def eda_univariate(df, columns):
    """
    Performs univariate analysis on specified columns.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    columns (list): List of columns to analyze
    
    Returns:
    None (Displays plots)
    """
    for col in columns:
        plt.figure(figsize=(8, 6))
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col], kde=True)
            plt.title(f"Distribution of {col}")
        else:
            sns.countplot(data=df, x=col)
            plt.title(f"Countplot of {col}")
        plt.show()

def eda_bivariate(df, col1, col2):
    """
    Performs bivariate analysis between two columns.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    col1 (str): First column
    col2 (str): Second column
    
    Returns:
    None (Displays plots)
    """
    plt.figure(figsize=(8, 6))
    if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        sns.scatterplot(data=df, x=col1, y=col2)
        plt.title(f"Scatterplot between {col1} and {col2}")
    else:
        sns.countplot(data=df, x=col1, hue=col2)
        plt.title(f"Countplot between {col1} and {col2}")
    plt.show()
