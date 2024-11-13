import os
import argparse
from PIL import Image

def rotate_images_in_directory(directory, angle):
    """
    Rota todas las imágenes JPG en el directorio dado y las guarda con el mismo nombre.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg")):
            image_path = os.path.join(directory, filename)
            
            with Image.open(image_path) as img:
                rotated_img = img.rotate(angle, expand=True)
                rotated_img.save(image_path)  # Sobrescribe el archivo original
                print(f"Imagen {filename} rotada {angle} grados y guardada.")

def main():
    parser = argparse.ArgumentParser(description="Rotar todas las imágenes JPG en un directorio.")
    parser.add_argument("directory", type=str, help="Directorio donde están las imágenes.")
    parser.add_argument("angle", type=int, help="Ángulo de rotación en grados (en sentido horario).")
    
    args = parser.parse_args()
    
    rotate_images_in_directory(args.directory, args.angle)

if __name__ == "__main__":
    main()

