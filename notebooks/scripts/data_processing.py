import pandas as pd

def load_data(file_path):
    """Function to load data from a CSV file."""
    try:
        df = pd.read_csv(file_path, delimiter='|')  # Ensure delimiter matches the data format
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def summarize_data(df):
    """Function to summarize the dataframe."""
    return df.describe(include='all')

def check_missing_values(df):
    """Function to check for missing values."""
    return df.isnull().sum()

def check_data_types(df):
    """Function to check data types of each column."""
    return df.dtypes

def detect_outliers(df, column):
    """Function to detect outliers using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]