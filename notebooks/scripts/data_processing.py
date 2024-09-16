import pandas as pd

def load_data(file_path):
    """Function to load data from a CSV file."""
    try:
        df = pd.read_csv(file_path, delimiter='|')  # Ensure delimiter matches the data format
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean the data by removing rows with missing or zero values in critical columns
    such as TotalPremium and TotalClaims.
    """
    # Remove rows with missing or zero values for key metrics
    df_clean = df.dropna(subset=['TotalPremium', 'TotalClaims'])
    df_clean = df_clean[df_clean['TotalPremium'] != 0]
    df_clean = df_clean[df_clean['TotalClaims'] != 0]
    
    return df_clean
def load_data2(file_path):
    """Function to load data from a CSV file."""
    try:
        # Load the data with appropriate data types
        df = pd.read_csv(file_path, delimiter='|', low_memory=False,
                         dtype={'TotalClaims': 'float64', 'TotalPremium': 'float64'},
                         na_values=['', ' ', 'NaN'])  # Handle missing values
        
        # Handle non-numeric or mixed-type columns by forcing them to numeric
        df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
        df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
        
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