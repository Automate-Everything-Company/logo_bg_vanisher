"""
Module to handle file operations
"""
from pathlib import Path
from typing import List, Tuple, Union

from PIL.Image import Image


def find_files(path: Path, extension: Union[Tuple, None]) -> List[Path]:
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


