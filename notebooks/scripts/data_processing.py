import pandas as pd

def load_data(file_path):
    """
    Load data from a file path into a pandas DataFrame.
    
    :param file_path: str, path to the data file
    :return: pd.DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(data):
    """
    Clean the dataset by handling missing values, duplicates, and other preprocessing steps.
    
    :param data: pd.DataFrame
    :return: pd.DataFrame, cleaned data
    """
    # Example cleaning process
    data.dropna(inplace=True)  # Removing missing values
    data.drop_duplicates(inplace=True)  # Removing duplicates
    return data

def prepare_features(data):
    """
    Prepare features for analysis and modeling. This can include encoding categorical variables, scaling, etc.
    
    :param data: pd.DataFrame
    :return: pd.DataFrame, processed data with prepared features
    """
    # Example of encoding a categorical feature
    data = pd.get_dummies(data, drop_first=True)
    return data
