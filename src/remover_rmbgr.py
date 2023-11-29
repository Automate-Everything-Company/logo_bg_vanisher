"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path
import rembg
from PIL import Image

from .background_remover import BackgroundRemovalStrategy
from .saver import SavePic


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self):
        self.suffix = "rmbgr_converted"
        self.saver = SavePic()

    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        img = Image.open(input_path).convert("RGBA")
        processed_img = rembg.remove(img)
        self.save_pic(img=processed_img, input_path=input_path, output_path=output_path)

    @staticmethod
    def _open_image(input_path):
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        return input_data

    def save_pic(self, img, input_path, output_path) -> None:
        """
        Saves pics
        :param img: Pillow image object
        :param input_path: User defined input path
        :param output_path: User defined output path (optional)
        :return: None
        """
        self.saver.save_image(img=img, input_path=input_path, output_path=output_path, suffix=self.suffix)
