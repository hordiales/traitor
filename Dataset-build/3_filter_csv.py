import pandas as pd
import argparse

print("WARNING: In this process. It is assumed that there is only one entity per image")
print("WARNING: traitor uses length, YOLO tags uses heigth")

# Set up argument parser
parser = argparse.ArgumentParser(description='Process CSV and filter rows based on minimum error for each base_name.')
parser.add_argument('csv_file', type=str, help='Path to the input CSV file')

args = parser.parse_args()

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(args.csv_file)

# Create a new column 'base_name' by extracting the second-to-last character from 'image_name'
df['base_name'] = df['image_name'].apply(lambda x: x[:-2])

# Calculate the errors e1 and e2
df['e1'] = abs(df['length'] - df['tag_height'])
df['e2'] = abs(df['width'] - df['tag_width'])
# Sum e1 and e2 to get the total error
df['total_error'] = df['e1'] + df['e2']

# Group by 'base_name' and select the row with the minimum total_error for each group
df_min_error = df.loc[df.groupby('base_name')['total_error'].idxmin()]

# Select only the specified columns for the final DataFrame
final_columns = [
    # 'image_name','base_name','total_error',
    'tag_width', 'tag_height', 'tag_class_number', 'tag_x_center', 'tag_y_center',
    'aspect_ratio', 'area', 'perimeter', 'surface_structure', 'solidity', 'circularity'
]
df_final = df_min_error[['base_name'] + final_columns]
# df_final = df[final_columns]

# Save the filtered DataFrame with the specified columns to a new CSV file
output_csv = 'filtered_by_min_error.csv'
df_final.to_csv(output_csv, index=False)

print(f"Filtered CSV saved as {output_csv}")
