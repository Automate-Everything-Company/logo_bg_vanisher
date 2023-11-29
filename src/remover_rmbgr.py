"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path
import rembg
from PIL import Image

from .background_remover import BackgroundRemovalStrategy


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self):
        self.suffix = "converted_rmbgr"

    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        img = Image.open(input_path).convert("RGBA")
        processed_img = rembg.remove(img)
        self.save_image_pillow(img=processed_img, input_path=input_path, output_path=output_path, suffix=self.suffix)

    @staticmethod
    def _open_image(input_path):
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        return input_data

    @staticmethod
    def _save_image_pillow(img: Image, input_path: Path, output_path: Union[bool, Path],
                          suffix: str = "converted") -> None:
        """
        Saves the image

        :param img: PIL Image object
        :param input_path: User defined input path
        :param output_path: Optional output path
        :param suffix: Suffix for converted images
        :return: None
        """
        if not output_path:
            output_path = Path(f"{input_path.stem}_pillow_converted.png")
        else:
            if not output_path.is_dir():
                output_path.mkdir(parents=True, exist_ok=True)
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
            else:
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
        img.save(output_path, "PNG")
