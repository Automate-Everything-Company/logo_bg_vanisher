"""
Module which handles saving the picture
"""
from pathlib import Path
from typing import Union

from PIL import Image


class SavePic:
    """
    Class to save the Pillow image object
    """
    @staticmethod
    def save_image(img: Image, input_path: Path, output_path: Union[bool, Path],
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
            output_path = Path(f"{input_path.stem}_{suffix}.png")
        else:
            if not output_path.is_dir():
                output_path.mkdir(parents=True, exist_ok=True)
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
            else:
                output_path = output_path / f"{input_path.stem}_{suffix}.png"
        img.save(output_path, "PNG")
