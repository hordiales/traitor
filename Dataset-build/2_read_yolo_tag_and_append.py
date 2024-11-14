import pandas as pd
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process CSV and read YOLO format files from a directory.')
parser.add_argument('csv_file', type=str, help='Path to the CSV file')
parser.add_argument('directory', type=str, help='Directory containing the YOLO .txt files')

args = parser.parse_args()

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(args.csv_file)


# Initialize new columns to store YOLO class and bounding boxes
df['tag_class_number'] = None
df['tag_x_center'] = None
df['tag_y_center'] = None
df['tag_width'] = None
df['tag_height'] = None

print("Warning: each bound box is named _Number")
# Loop through each row of the DataFrame
for index, row in df.iterrows():
    
    # Construct the corresponding .txt filename
    # [:-2] is to remove _1 or _2 of each file, correspondind to each bb detected in extracted dir by traitor
    # txt_filename = os.path.join(args.directory, row['image_name'][-2] + '.txt') #Grain Dataset 
    txt_filename = os.path.join(args.directory, row['image_name'].rsplit('_', 1)[0] + '.txt')
    #txt_filename = os.path.join(args.directory, row['image_name'] + '.txt')  # SojaBinario
    # print(txt_filename)


    # Check if the corresponding .txt file exists
    if os.path.exists(txt_filename):
        print(f'Processing {txt_filename}')
        # Open the .txt file and read the YOLO format data
        with open(txt_filename, 'r') as file:
            content = file.readline().strip()  # Read the first line (assuming one line per file)
            values = content.split()  # Split the content by spaces

            # Extract the YOLO data (class number, bounding box)
            class_number = int(values[0])
            x_center = float(values[1])
            y_center = float(values[2])
            width = float(values[3])
            height = float(values[4])

            # Append the data to the DataFrame
            df.at[index, 'tag_class_number'] = class_number
            df.at[index, 'tag_x_center'] = x_center
            df.at[index, 'tag_y_center'] = y_center
            df.at[index, 'tag_width'] = width
            df.at[index, 'tag_height'] = height
    else:
        print(f"Warning: {txt_filename} does not exist.")

# Save the updated DataFrame to a new CSV file
# output_csv = os.path.join(args.directory, 'MaizTest_measurements_with_YOLO.csv')
output_csv = args.directory+'_measurements_with_YOLO.csv'
df.to_csv(output_csv, index=False)

#TODO: print only on sucess (check errors first)
print(f"Updated CSV saved as {output_csv}")
