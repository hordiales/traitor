from google.cloud import storage
import os
import subprocess
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process PNG files from a directory.')
parser.add_argument('directory', type=str, help='Directory containing the PNG files')

args = parser.parse_args()

# input_path = 'input/'
# output_dir = 'output/'

input_folder = args.directory

def process_files():
    output_file = input_folder+"_measurements.csv"
    
    print(f"Processing {input_folder}")
    print("Extract process")
    subprocess.run(['traitor', 'extract', '-i', input_folder, '-o', input_folder+"_extracted", '-u', '-b'])
    print("Align process")
    subprocess.run(['traitor', 'align', '-i', input_folder, '-m', input_folder+"_extracted", '-o', input_folder+"_aligned"])
    print("Measure process")
    subprocess.run(['traitor', 'measure', '-i', input_folder+"_aligned", '-o', output_file])
    #TODO: check error code, print error o sucess message
    print(f"{output_file} output generated")
    
if __name__ == "__main__":
    process_files()
    print("WARNING: si hay warnings en el proceso con error \"Mean of empty slice., invalid value encountered in scalar divide\", tal vez por imagenes todas en negro, eliminarlas del dataset, sino luego out of index errors")

""" 
Error example
19/1276 [00:02<01:25, 14.66it/s] .. traitor/traitor/cli/extract.py:142: UserWarning: cf33569e-20241105_201505_24_A.jpg: Mean of empty slice., invalid value encountered in scalar divide
  warnings.warn(f"{image_file.name}: {warnings_str}")
"""