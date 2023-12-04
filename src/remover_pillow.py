"""
Module which handles background removal from pics using Pillow
"""
from PIL import Image, ImageFilter

from .background_remover import BackgroundRemovalStrategy
from .saver import SavePic


class PillowBackgroundRemoval(BackgroundRemovalStrategy):
    """
    Removes the background using the Pillow standard library.
    It identifies the first pixel (upper left), which is background, and not the logo itself.
    """

    def __init__(self, img: Image, tolerance: int = 50, edge_tolerance: int = 50):
        super().__init__(img)
        self.filename = img.filename
        self.tolerance = tolerance
        self.edge_tolerance = edge_tolerance
        self.suffix = "pillow_converted"

    def remove_background(self) -> Image:
        if self.image is None or not hasattr(self.image, 'convert'):
            raise ValueError("Invalid image object provided")

        img = self.image.convert("RGBA")
        processed_img = self._process_image_data(img=img)
        processed_img.filename = self.filename
        return processed_img

    def _process_image_data(self, img: Image) -> list:
        # Get the background color (assuming it's the color of the top-left pixel)
        bg_color = img.getpixel((0, 0))
        # Convert img to grayscale for better edge detection and create an edge mask
        edge_mask = img.convert("L").filter(ImageFilter.FIND_EDGES)
        data = img.getdata()
        edge_data = edge_mask.getdata()
        new_data = []
        for i, item in enumerate(data):
            if edge_data[i] > 0:  # If the pixel is on an edge
                if all(abs(item[j] - bg_color[j]) <= self.edge_tolerance for j in range(3)):
                    new_data.append((255, 255, 255, 0))  # Transparent
                else:
                    new_data.append(item)
            else:
                if all(abs(item[j] - bg_color[j]) <= self.tolerance for j in range(3)):
                    new_data.append((255, 255, 255, 0))  # Transparent
                else:
                    new_data.append(item)
        img.putdata(new_data)
        return img
