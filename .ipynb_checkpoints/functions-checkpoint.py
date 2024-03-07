import pandas as pd

def clean_airbnb_data(df):
    """
    Clean the Airbnb dataset.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing Airbnb data.

    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    """
    # Step 1: Drop 'name' column
    df_cleaned = df.drop(['name'], axis=1)

    # Step 2: Drop 'host_name' column
    df_cleaned = df_cleaned.drop(['host_name'], axis=1)

    # Step 3: Drop 'last_review' column
    df_cleaned = df_cleaned.drop(['last_review'], axis=1)

    # Step 4: Rename 'id' column to 'address_id'
    df_cleaned = df_cleaned.rename(columns={'id': 'address_id'})

    # Step 5: Rename 'availability_365' column to 'yearly_availability_365'
    df_cleaned = df_cleaned.rename(columns={'availability_365': 'yearly_availability_365'})

    # Step 6: Fill null/empty values of 'reviews_per_month' column with mean of the column
    reviews_per_month_mean = df_cleaned['reviews_per_month'].mean()
    df_cleaned['reviews_per_month'] = df_cleaned['reviews_per_month'].fillna(reviews_per_month_mean)

    return df_cleaned

# Example usage:
# df_cleaned = clean_airbnb_data(df)
