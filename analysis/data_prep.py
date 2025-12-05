import pandas as pd



def load_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)


def preview_data(df: pd.DataFrame) -> dict:
    return {
        "head": df.head(),
        "shape": df.shape,
        "columns": df.columns.tolist()
    }


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()



    # Filling the missing values
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
    df['date_added'] = df['date_added'].fillna('Unknown')



    # Country groupwise mode imputation
    mode_country = df.groupby(['type', 'listed_in'])['country'].transform(
        lambda x: x.fillna(x.mode().iloc[0] if not x.mode().empty else 'Unknown')
    )
    df['country'] = df['country'].fillna(mode_country)



    # Drop rows with missing duration
    df.dropna(subset=['duration'], inplace=True)

    return df


def convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert date_added
    df['date_added'] = pd.to_datetime(df['date_added'], errors="coerce")



    # Convert selected columns to categorical
    for col in ['type', 'listed_in', 'country', 'rating']:
        df[col] = df[col].astype('category')



    # Split duration into int + type
    df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
    df['duration_int'] = df['duration_int'].astype('int')

    return df


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handleing outliers in the dataset:
    - Remove extreme movie durations (>250 mins) unless interactive
    - Keep interactive titles flagged
    """
    df = df.copy()



    # Known interactive titles
    interactive_titles = [
        'Headspace: Unwind Your Mind',
        'Black Mirror: Bandersnatch'
    ]

    # Tag interactive
    df['duration_note'] = df['title'].apply(
        lambda x: 'interactive' if x in interactive_titles else 'standard'
    )



    # Keep only valid durations (<=250 mins for movies, unless interactive)
    clean_df = df[
        (df['type'] != 'Movie') |
        ((df['type'] == 'Movie') & (
            (df['duration_int'] <= 250) | (df['duration_note'] == 'interactive')
        ))
    ].copy()



    # Droping the helper column
    clean_df.drop(columns='duration_note', inplace=True)

    return clean_df


    
