"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path

from rembg import remove

from background_remover import BackgroundRemovalStrategy


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        # Open the image
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()

        # Remove the background
        output_data = remove(input_data)
        if not output_path:
            output_path = Path(f"{input_path.stem}_Rmbgr_converted.png")
        else:
            if not output_path.is_dir():
                output_path.mkdir(parents=True, exist_ok=True)
                output_path = output_path / f"{input_path.stem}_Rmbgr_converted.png"
            else:
                output_path = output_path / f"{input_path.stem}_Rmbgr_converted.png"

        # Save the output
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
