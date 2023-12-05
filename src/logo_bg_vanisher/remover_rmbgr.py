"""
Module which handles background removal from pics using Rmbgr
"""
import rembg
from PIL import Image

from .background_remover import BackgroundRemovalStrategy


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self, img):
        super().__init__(img)
        self.filename = img.filename
        self.suffix = "rmbgr_converted"

    def remove_background(self) -> Image:
        if self.image is None or not hasattr(self.image, 'convert'):
            raise ValueError("Invalid image object provided")

        img = self.image.convert("RGBA")
        processed_img = rembg.remove(img)
        processed_img.filename = self.filename
        return processed_img
