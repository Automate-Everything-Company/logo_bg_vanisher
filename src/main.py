import os

from src.gui import select_folder
from src.remover_pillow import process_images


def main():
    folder_path = select_folder()

    output_folder = os.path.join(folder_path, "no_bg")

    # Process the images in the selected folder
    process_images(folder_path, output_folder)

    print("Images processed and saved with no background.")



if __name__ == "__main__":
    main()