"""
Module which handles background removal from pics using Pillow
"""
from typing import Union
from pathlib import Path

from PIL import Image, ImageFilter

from background_remover import BackgroundRemovalStrategy


class PillowBackgroundRemoval(BackgroundRemovalStrategy):
    """
    Removes the background using the Pillow standard library.
    It identifies the first pixel (upper left), which is background, and not the logo itself.
    """

    def __init__(self, tolerance: int = 50, edge_tolerance: int = 50):
        self.tolerance = tolerance
        self.edge_tolerance = edge_tolerance
        self.suffix = "converted_pillow"

    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        img = Image.open(input_path).convert("RGBA")
        processed_img = self._process_image_data(img=img)
        self.save_image_pillow(img=processed_img, input_path=input_path, output_path=output_path, suffix=self.suffix)

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

    @staticmethod
    def save_image_pillow(img: Image, input_path: Path, output_path: Union[bool, Path],
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
            output_path = Path(f"{input_path.stem}_Pillow_converted.png")
        else:
            if not output_path.is_dir():
                output_path.mkdir(parents=True, exist_ok=True)
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
            else:
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
        img.save(output_path, "PNG")
