"""
Main entry
"""
from pathlib import Path

import argparse
from typing import Union

from remover_pillow import PillowBackgroundRemoval
from remover_rmbgr import RmbgrBackgroundRemoval
from background_remover import BackgroundRemovalStrategy
from cropper import AutoCropper, ManualCropper
from folder_utils import find_files, load_image
from saver import SavePic
from sizer import AspectRatioSizer, ManualSizer


def extract_remover_type(args):
    remover: BackgroundRemovalStrategy
    if args.method == "pillow":
        remover = PillowBackgroundRemoval(tolerance=50, edge_tolerance=50)
    elif args.method == "rmbgr":
        remover = RmbgrBackgroundRemoval()
    else:
        raise ValueError("Method must be either 'pillow' or 'rmbgr'.")
    return remover


def parse_arguments():
    """
    Parses user arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        prog='LogoBgVanisher',
        description='Can do the following image processing operations:\n'
                    '- Makes image background transparent (method: pillow)\n'
                    '- Removes image background (method: rmbg)\n'
                    '- Resizes image\n'
                    '- Crops image\n'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="File absolute path")
    group.add_argument("--input_path", help="Folder absolute path")

    parser.add_argument("--method", choices=["pillow", "rmbg"], required=True, help="Background removal method")
    parser.add_argument("--resize", help="Resize the image. Format: 'width,height' or 'width' for aspect ratio")
    parser.add_argument("--crop", help="Crop the image. Use 'auto' for autocrop or 'width,height' for manual crop")
    parser.add_argument('--verbose', action='store_true', help="Debug mode")
    return parser.parse_args()


def _process_image(pic: Path, user_args: argparse.Namespace) -> None:
    image_object = load_image(picture=pic)
    suffix = ""
    # Background removal
    if user_args.method == "pillow":
        remover = PillowBackgroundRemoval(img=image_object)
        image_object = remover.remove_background()
        suffix = suffix + "_converted_pillow"
    elif user_args.method == "rmbg":
        remover = RmbgrBackgroundRemoval(img=image_object)
        image_object = remover.remove_background()
        suffix = suffix + "_converted_rmbg"

    # Resize
    if user_args.resize:
        scaler = ManualSizer(img=image_object) if ',' in user_args.resize else AspectRatioSizer(img=image_object)
        if ',' in user_args.resize:
            width, height = map(int, user_args.resize.split(','))
            scaler.width = width
            scaler.height = height
            image_object = scaler.set_size()
            suffix = suffix + "_scaled"
        else:
            width = int(user_args.resize)
            scaler.width = width
            image_object = scaler.set_size(image=image_object)
            suffix = suffix + "_scaled"

    # Crop
    if user_args.crop:
        if user_args.crop.lower() == 'auto':
            cropper = AutoCropper(img=image_object)
            image_object = cropper.crop_image()
            suffix = suffix + "_cropped"
        else:
            cropper = ManualCropper(img=image_object)
            cropper.dimensions = tuple(map(int, user_args.crop.split(',')))
            image_object = cropper.crop_image()
            suffix = suffix + "_cropped"

    image_saver = SavePic(img=image_object)
    image_saver.save_image(suffix=suffix)


def main() -> None:
    """
    Main entry for the CLI
    :return: None
    """
    args = parse_arguments()
    file = Path(args.file)
    input_path = Path(args.input_path) if args.input_path else None

    if input_path:
        pics = find_files(path=input_path, extension=('.png', '.jpeg'))
        for pic in pics:
            _process_image(pic=pic, user_args=args)
    elif file:
        _process_image(pic=file, user_args=args)

    if args.verbose:
        print("Done!")


if __name__ == "__main__":
    main()
