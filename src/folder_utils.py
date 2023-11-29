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


def _save_image_pillow(img: Image, input_path: Path, output_path: Union[bool, Path],
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
