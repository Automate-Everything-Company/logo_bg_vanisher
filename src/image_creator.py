"""
Module which handles the Image creation

"""
from abc import ABC, abstractmethod
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
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file} was not found")
        except PermissionError:
            raise PermissionError(f"Permission denied for file {file}")
        except IOError as e:
            raise IOError(f"An error occurred while opening the file {file}: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")
