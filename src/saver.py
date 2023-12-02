"""
Module which handles saving the picture
"""
from pathlib import Path
from PIL import Image


class SavePic:
    """
    Class to save the Pillow image object
    """

    @staticmethod
    def save_image(img: Image, path: Path, suffix: str = "converted") -> None:
        """
        Saves the image

        :param path: Path to the unedited picture
        :param img: PIL Image object
        :param suffix: Suffix for converted images
        :return: None
        """
        try:
            output_path = path.parent / f"{path.stem}{suffix}.png"
            img.save(output_path, "PNG")
        except OSError as e:
            print(f"Error saving image: {e}")
        except ValueError as e:
            print(f"Invalid image: {e}")