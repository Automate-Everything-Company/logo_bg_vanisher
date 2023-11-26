"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path

from rembg import remove


def process_image_with_rembg(input_path, output_path: Union[bool, Path] = False):
    # Open the image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    # Remove the background
    output_data = remove(input_data)
    if not output_path:
        output_path = Path(f"{input_path.stem}_rmbgr_converted.png")
    else:
        if not output_path.is_dir():
            output_path.mkdir(parents=True, exist_ok=True)
            output_path = output_path / f"{input_path.stem}_rmbgr_converted.png"
        else:
            output_path = output_path / f"{input_path.stem}_rmbgr_converted.png"

    # Save the output
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)
