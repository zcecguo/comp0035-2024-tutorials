from pathlib import Path
import pandas as pd

# Define a function to print DataFrame information
def analyze_dataframe(df, df_name):
    """Print key information about the DataFrame."""
    
    print(f"\nAnalyzing {df_name}:")
    
    # Print shape (number of rows and columns)
    print(f"\nShape of {df_name} (Rows, Columns): {df.shape}")
    
    # Print the first 5 rows
    print(f"\nFirst 5 rows of {df_name}:")
    print(df.head())
    
    # Print the last 5 rows
    print(f"\nLast 5 rows of {df_name}:")
    print(df.tail())
    
    # Print the column labels
    print(f"\nColumn Labels of {df_name}:")
    print(df.columns)
    
    # Print the data types of each column
    print(f"\nData Types of Each Column in {df_name}:")
    print(df.dtypes)
    
    # Print DataFrame info
    print(f"\n{df_name} Info:")
    df.info()
    
    # Print descriptive statistics
    print(f"\nDescriptive Statistics of {df_name}:")
    print(df.describe())

     # Display any missing values in the dataframe
    print("Rows with missing values:")
    print(df[df.isna().any(axis=1)])

    # Print columns with missing values
    print("\nColumns with missing values:")
    print(df.isnull().sum())

def prepare_event_data(df_raw, df_npc=None):
    """Prepare the event data for analysis

    Parameters:
    df_raw (DataFrame): Pandas DataFrame with the event data
    df_npc (DataFrame): Optional. Pandas DataFrame with the NPC codes data

    Returns:
    df_prepared (DataFrame): Pandas DataFrame
    """

    # Activity 7: Deal with the NaN values in the Rome row (index 0)
    # Drop the rows
    df_raw = df_raw.drop(index=[0, 17, 31])
    # Reset the index
    df_raw = df_raw.reset_index(drop=True)

    # Activity 4: Convert the data type float64 columns to int
    float_columns = df_raw.select_dtypes(include=['float64']).columns
    for col in float_columns:
        try:
            df_raw[col] = df_raw[col].astype('int')
        except ValueError as e:
            print(f"Error, can't convert column {df_raw[col].name} to int: {e}")

    print("\nData types of the float columns after conversion:")
    print(df_raw.loc[:, float_columns].dtypes)
    # Activity 4: Convert the start and end columns from object to datetime
    df_raw['start'] = pd.to_datetime(df_raw['start'], format='%d/%m/%Y')
    df_raw['end'] = pd.to_datetime(df_raw['end'], format='%d/%m/%Y')

    print("\nData types of the start/end columns after conversion:")
    print(df_raw.loc[:, ['start', 'end']].dtypes)


if __name__ == '__main__':
    # Filepaths for the CSV and Excel files
    try:
        paralympics_csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
        paralympics_xlsx_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')

        # Load the CSV and Excel files
        events_csv_df = pd.read_csv(paralympics_csv_file)
        xlsx_df1 = pd.read_excel(paralympics_xlsx_file)
        xlsx_df2 = pd.read_excel(paralympics_xlsx_file, sheet_name='medal_standings')

        # Call the function to describe each DataFrame
        analyze_dataframe(events_csv_df, "Paralympics CSV file")
        analyze_dataframe(xlsx_df1, "Paralympics Excel file (Sheet 1)")
        analyze_dataframe(xlsx_df2, "Medal standings Excel file")

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    df_npc_codes = pd.read_csv(npc_csv, usecols=['Code', 'Name'], encoding='utf-8', encoding_errors='ignore')
    merged_df = prepare_event_data(events_csv_df, df_npc_codes)


    

    
