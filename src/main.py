import os

from src.folder_utils import find_files
from src.gui import select_folder
from src.remover_pillow import process_image_with_edge_removal


def main():
    folder_path = select_folder()

    pics = find_files(path=folder_path, extension=(".png", ".jpeg", ".jpg"))
    for pic in pics:
        process_image_with_edge_removal(input_path=pic)

    print("Images processed and saved with no background.")


if __name__ == "__main__":
    main()
