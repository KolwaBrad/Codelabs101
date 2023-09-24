import pandas as pd
import re
import logging

# Specify the file path of the Excel file
# file_path = 'Test_Files_3B.xlsx'  # Replace with the actual file path


# Load the Excel files into DataFrames
file1 = "Test_Files_3B.xlsx"
file2 = "Test_Files_3C.xlsx"
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Concatenate the DataFrames vertically
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined_df.to_excel("combined_file.xlsx", index=False)

file_path = "combined_file.xlsx"
# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, engine='openpyxl')


def generate_email(name):
    names = name.split(',')
    first_name = names[0].strip()
    last_name = names[-1].strip()
    full_name = first_name + " " + last_name
    full_name = re.sub(r'[^\w\s]', '', full_name)  # Remove special characters
    email = f"{full_name.replace(' ', '.').lower()}@gmail.com"  # Replace spaces with dots
    return email

# Apply the generate_email function to create a new 'Email Address' column
df['Email Address'] = df['Student Name'].apply(generate_email)


# Save as TSV
df.to_csv('Combined_file.tsv', sep='\t', index=False)

# Save as CSV
df.to_csv('Combined_file.csv', index=False)


# Configure logging
logging.basicConfig(filename='project.log', level=logging.INFO)

# Count and log the number of male and female students
male_count = df[df['Gender'] == 'M'].shape[0]
female_count = df[df['Gender'] == 'F'].shape[0]

logging.info(f"Number of male students: {male_count}")
logging.info(f"Number of female students: {female_count}")

# List and log names with special characters
special_characters_names = df[df['Student Name'].str.contains(r'[^\w\s,]', regex=True)]['Student Name'].tolist()
logging.info(f"Students with special characters in names: {special_characters_names}")

# Generate separate male and female lists
male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']



# Concatenate the DataFrames vertically
combined_to_shuffle_df = pd.concat([male_students, female_students], ignore_index=True)

# Shuffle the rows
shuffled_file_df = combined_to_shuffle_df.sample(frac=1).reset_index(drop=True)


# Save the DataFrame to a JSON file
shuffled_file_df.to_json("combined_output_file.json", orient="records")


print("Test1")