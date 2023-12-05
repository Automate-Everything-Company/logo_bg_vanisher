"""
Module which handles saving the picture
"""
from pathlib import Path

from PIL import Image


class SavePic:
    """
    Class to save the Pillow image object
    """

    def __init__(self, img: Image):
        self.image = img

    def save_image(self, suffix: str = "converted") -> None:
        """
        Saves the image
        :param suffix: Suffix for converted images
        :return: None
        """
        try:
            filename = Path(self.image.filename)
            output_path = filename.parent / f"{filename.stem}_{suffix}.png"
            self.image.save(output_path, "PNG")
        except OSError as e:
            print(f"Error saving image: {e}")
        except ValueError as e:
            print(f"Invalid image: {e}")
