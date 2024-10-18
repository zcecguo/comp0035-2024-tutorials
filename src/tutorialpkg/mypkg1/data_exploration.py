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

    
