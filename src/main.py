"""
Main entry
"""
from pathlib import Path

import argparse
from typing import Union

from PIL.Image import Image

from image_creator import CreatePillowImage
from remover_pillow import PillowBackgroundRemoval
from remover_rmbgr import RmbgrBackgroundRemoval
from background_remover import BackgroundRemovalStrategy
from cropper import AutoCropper, ManualCropper
from folder_utils import find_files
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
        description='Scans a folder for images and can do the following image processing operations:\n'
                    '- Makes background transparent (method: pillow)\n'
                    '- Removes background (method: rmbg)\n'
                    '- Resizes images\n'
                    '- Crops images\n'
    )
    parser.add_argument("--file", required=True, help="Absolute path of a file")
    parser.add_argument("--input_path", required=False, help="Path to the input folder")
    parser.add_argument("--output_path", required=False, help="Path where the new images are saved")
    parser.add_argument("--method", choices=["pillow", "rmbg"], required=True, help="Background removal method")
    parser.add_argument("--resize", help="Resize the image. Format: 'width,height' or 'width' for aspect ratio")
    parser.add_argument("--crop", help="Crop the image. Use 'auto' for autocrop or 'width,height' for manual crop")
    parser.add_argument('--verbose', action='store_true', help="Debug mode")
    return parser.parse_args()


def _load_image(picture: Path) -> Union[Image, None]:
    try:
        if picture:
            image_creator = CreatePillowImage()
            image_obj = image_creator.convert_image(file=picture)
            return image_obj
    except IOError as e:
        print(f"Error opening image: {e}")
        return None


def _process_image(pic: Path, user_args: argparse.Namespace, output_path: Union[Path, None] = None) -> None:
    image_object = _load_image(picture=pic)
    suffix = ""
    # Background removal
    if user_args.method == "pillow":
        remover = PillowBackgroundRemoval()
        image_object = remover.remove_background(img=image_object)
        suffix = suffix + "_converted_pillow"
    elif user_args.method == "rmbg":
        remover = RmbgrBackgroundRemoval()
        image_object = remover.remove_background(img=image_object)
        suffix = suffix + "_converted_rmbg"

    # Resize
    if user_args.resize:
        scaler = ManualSizer() if ',' in user_args.resize else AspectRatioSizer()
        if ',' in user_args.resize:
            width, height = map(int, user_args.resize.split(','))
            scaler.width = width
            scaler.height = height
            image_object = scaler.set_size(image=image_object)
            suffix = suffix + "_scaled"
        else:
            width = int(user_args.resize)
            scaler.width = width
            image_object = scaler.set_size(image=image_object)
            suffix = suffix + "_scaled"

    # Crop
    if user_args.crop:
        if user_args.crop.lower() == 'auto':
            cropper = AutoCropper()
            image_object = cropper.crop_image(image=image_object)
            suffix = suffix + "_cropped"
        else:
            cropper = ManualCropper()
            cropper.dimensions = map(int, user_args.crop.split(','))
            image_object = cropper.crop_image(image=image_object)
            suffix = suffix + "_cropped"

    path_to_save = output_path if output_path else pic.parent
    image_saver = SavePic()
    image_saver.save_image(img=image_object, path=path_to_save, suffix=suffix)


def main() -> None:
    """
    Main entry for the CLI
    :return: None
    """
    args = parse_arguments()
    file = Path(args.file)
    input_path = Path(args.input_path) if args.output_path else None
    output_path = Path(args.output_path) if args.output_path else None

    if output_path:
        output_path.mkdir(parents=True, exist_ok=True)

    if input_path:
        pics = find_files(path=input_path, extension=('.png', '.jpeg'))
        for pic in pics:
            _process_image(pic=pic, user_args=args)
    elif file:
        _process_image(pic=file, user_args=args, output_path=input_path)

    if args.verbose:
        print("Done!")


if __name__ == "__main__":
    main()
