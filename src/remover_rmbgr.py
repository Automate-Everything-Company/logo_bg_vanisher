"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path
import rembg
from PIL import Image

from background_remover import BackgroundRemovalStrategy
from saver import SavePic


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self):
        self.suffix = "rmbgr_converted"
        self.saver = SavePic()

    def remove_background(self, img: Image) -> Image:
        img = img.convert("RGBA")
        processed_img = rembg.remove(img)
        return processed_img
Fix relative import for build.
Make remove_background method work with and Image object.
Remove the save file capabilities.