"""
Module to handle file operations
"""
from pathlib import Path
from typing import List
from typing import Tuple
from typing import Union

from PIL.Image import Image

from src import CreatePillowImage


def find_files(path: Path, extension: Union[str, Tuple, None]) -> List[Path]:
    """
    Finds and returns files with certain extension
    :param path:
    :param extension:
    :return:
    """
    if extension:
        return [pic for pic in path.iterdir() if pic.suffix in extension]
    else:
        return [pic for pic in path.iterdir()]


def load_image(picture: Path) -> Union[Image, None]:
    try:
        if picture:
            image_creator = CreatePillowImage()
            image_obj = image_creator.convert_image(file=picture)
            return image_obj
    except OSError as e:
        print(f"Error opening image: {e}")
        return None
