import sys
import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


def process_image(image_path):
    try:
        img = Image.open(image_path)
        output_path = os.path.splitext(image_path)[0] + ".png"
        img.save(output_path, 'png')
        print(f"Processed {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")


def process_images_parallel(image_folder):
    if not os.path.exists(image_folder):
        print(f"Error: Image folder '{image_folder}' not found.")
        sys.exit(1)

    with ThreadPoolExecutor() as executor:
        image_paths = (
            os.path.join(image_folder, filename)
            for filename in os.listdir(image_folder)
        )
        executor.map(process_image, image_paths)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_folder>")
        sys.exit(1)

    image_folder = os.path.join(sys.argv[1], '')
    process_images_parallel(image_folder)

    print('All done!')
