import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display the names of the sheets
sheet_names = excel_data.sheet_names
print(sheet_names)

# Parse a specific sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the first few rows of the DataFrame
print(df.head())
