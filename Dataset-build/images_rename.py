import os
import argparse

def rename_jpg_files(directory, suffix):
    for filename in os.listdir(directory):
        # Process only files with .jpg extension (ignoring case) or txt (to maintain yolo convention)
        if filename.lower().endswith((".jpg",".txt")):
            # Split the name and extension
            name, extension = os.path.splitext(filename)
            # Create the new filename by adding the suffix before the extension
            new_filename = f"{name}{suffix}{extension}"
            # Construct full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")

def main():
    parser = argparse.ArgumentParser(description="Rename all JPG files in a directory by adding a suffix.")
    parser.add_argument("directory", type=str, help="Path to the directory containing JPG files.")
    parser.add_argument("suffix", type=str, help="Suffix to add to the filename (e.g., '_A', '_B').")
    
    args = parser.parse_args()
    
    rename_jpg_files(args.directory, args.suffix)

if __name__ == "__main__":
    main()


