"""
Main entry
"""
from pathlib import Path

import argparse

from folder_utils import find_files
from remover_pillow import PillowBackgroundRemoval
from remover_rmbgr import RmbgrBackgroundRemoval


def parse_arguments():
    """
    Parses user arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        prog='logo_background_remover',
        description='Scans a defined user folder for images and replaces the background with a transparent one.',
    )
    parser.add_argument("--input_path", "-i", help="Path where the images are")
    parser.add_argument("--output_path", "-o", required=False, help="Path where new images are saved")
    parser.add_argument("--method", "-m", required=True, help="pillow or rmbgr")
    parser.add_argument("--resize", "-r", required=False, help="Resize the new image: 1000,700")
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag
    return parser.parse_args()


def main():
    args = parse_arguments()
    remover = args.method
    if remover not in ("pillow", "rmbgr"):
        raise ValueError("Method must be: pillow or rmbgr. Please try again.")
    else:
        remover = args.method
    folder_path = Path(args.input_path)
    if args.output_path:
        output_path = Path(args.output_path)

    else:
        output_path = False

    pics = find_files(path=folder_path, extension=(".png", ".jpeg", ".jpg"))
    for pic in pics:
        if remover == "pillow":
            pillow_remover = PillowBackgroundRemoval(tolerance=50, edge_tolerance=50)
            pillow_remover.remove_background(input_path=pic, output_path=output_path)
        else:
            rmbgr_remover = RmbgrBackgroundRemoval()
            rmbgr_remover.remove_background(input_path=pic, output_path=output_path)

    print("Done!")


if __name__ == "__main__":
    main()
