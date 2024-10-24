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

    # Activity 5: Merge the event data with the NPC data
    # Add the NPC code to the event data using 'merge' function and a 'left' join
    # The left dataframe is the event data and the right dataframe is the NPC code data
    # The fields to join on are 'Name' in the NPC data and 'country' in the event data

    # Activity 7: Correct the country names before doing the merge
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    df_raw['country'] = df_raw['country'].replace(replacement_names)

    if df_npc is not None:
        df_merge = df_raw.merge(df_npc, left_on='country', right_on='Name', how='left')
        print("\nAll rows, 'country', 'Code', 'Name' columns, of the merged dataframe:")
        print(df_merge[['country', 'Code', 'Name']])

    


if __name__ == "__main__":
    # Activity 2: Filepath of the csv data file
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")

    # Activity 2: Filepath of the Excel data file.
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")

    # Activity 2: Filepath of the NPC codes csv data file
    npc_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")

    # Activity 2: Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        events_csv_df = pd.read_csv(paralympics_datafile_csv)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    events_excel_df = pd.read_excel(paralympics_datafile_excel)
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name="medal_standings")

    # Activities 5-8: Call the function to prepare the data and merge the event data with the NPC data
    df_npc_codes = pd.read_csv(npc_csv, usecols=['Code', 'Name'], encoding='utf-8', encoding_errors='ignore')
    merged_df = prepare_event_data(events_csv_df, df_npc_codes)