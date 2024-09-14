def calculate_variability(data):
    """
    Calculate the variability (standard deviation) for numerical features.
    """
    return data[['TotalPremium', 'TotalClaims']].std()
