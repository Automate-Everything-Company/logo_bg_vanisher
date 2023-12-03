"""
Module which handles background removal from pics using Rmbgr
"""
import rembg
from PIL import Image

from .background_remover import BackgroundRemovalStrategy


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self, img):
        super().__init__(img)
        self.image = img
        self.suffix = "rmbgr_converted"

    def remove_background(self) -> Image:
        img = self.image.convert("RGBA")
        processed_img = rembg.remove(img)
        return processed_img
