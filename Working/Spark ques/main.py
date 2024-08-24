import pandas as pd
import re

# Load data from the existing CSV file
df = pd.read_csv('raw.csv')

# Function to extract the question number from the 'Spark' column
def extract_question_number(text):
    match = re.search(r'question (\d+)', text)
    if match:
        return int(match.group(1))
    return None

# Apply the function to create a new column for the question number
df['Question Number'] = df['Spark'].apply(extract_question_number)

# Sort the DataFrame by the 'Question Number' column
df_sorted = df.sort_values(by='Question Number')

# Save the sorted DataFrame with the new 'Question Number' column back to the 'raw.csv' file
df_sorted.to_csv('raw2.csv', index=False)

print("CSV file 'raw.csv' has been updated, sorted, and includes a separate 'Question Number' column.")
