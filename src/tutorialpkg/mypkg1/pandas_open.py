from pathlib import Path


# This script is located in a subfolder so you need to navigate up to the parent (src) and then its parent (project root), then down to the 'data' directory and finally the .csv file
csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
xlsx_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')
# Check if the file exists
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")

if xlsx_file.exists():
    print(f"XLSX file found: {xlsx_file}")
else:
    print("XLSX file not found.")

import pandas as pd

def some_function(df):
     """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
     """
df = pd.read_csv(csv_file)
xlsx_df1 = pd.read_excel(xlsx_file)
xlsx_df2 = pd.read_excel(xlsx_file, sheet_name='medal_standings')
if __name__ == '__main__': 
    print(df)
    print(xlsx_df1)
    print(xlsx_df2)
    