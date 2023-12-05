"""
Module which handles the Image creation

"""
from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Union

from PIL import Image


class ImageCreator(ABC):
    """
    Interface for creating
    """

    @abstractmethod
    def convert_image(self, file: Path):
        """
        Abstract method for sizer objects.
        """


class CreatePillowImage(ImageCreator):
    """
    Converts a picture to a Pillow image object
    """
    def convert_image(self, file: Union[Path, str]) -> Image:
        """
        Converts a file path to a Pillow image
        :param file: Path to a file
        :return: Pilow Image object
        """
        if not any((isinstance(file, Path), isinstance(file, str))):
            raise ValueError("The file must be a Path object or a string")
        if not file.exists():
            raise FileNotFoundError(f"The file {file} does not exist")
        try:
            return Image.open(file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"The file {file} was not found") from exc
        except PermissionError as exc:
            raise PermissionError(f"Permission denied for file {file}") from exc
        except OSError as exc:
            raise OSError(f"An error occurred while opening the file {file}: {exc}") from exc
        except Exception as exc:
            raise Exception(f"An unexpected error occurred: {exc}") from exc
