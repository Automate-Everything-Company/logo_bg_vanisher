"""
Main entry
"""
from pathlib import Path

from src.folder_utils import find_files
from src.gui import select_folder
from src.remover_pillow import process_image_with_edge_removal
from src.remover_rmbgr import process_image_with_rembg


def main():
    folder_path = select_folder()

    pics = find_files(path=folder_path, extension=(".png", ".jpeg", ".jpg"))
    for pic in pics:
        process_image_with_edge_removal(input_path=pic)
        process_image_with_rembg(input_path=pic, output_path=Path.cwd()/"converted")

    print("Images processed and saved with no background.")


if __name__ == "__main__":
    main()
