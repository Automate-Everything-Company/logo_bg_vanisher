"""
Module which handles cropping of images.
"""
from abc import ABC, abstractmethod
from typing import Tuple, Union

from PIL import Image


class Cropper(ABC):
    """
    Interface for future cropping classes
    """

    @abstractmethod
    def crop(self, image: Image) -> Image:
        """
        Interface for cropping classes.
        """
        pass


class AutoCropper(Cropper):
    """
    Performs auto-cropping
    """

    def crop(self, image: Image) -> Image:
        if image.mode != 'RGBA':
            raise ValueError("Image must be in RGBA mode for auto cropping")

        bbox = image.getbbox()
        if bbox is None:
            raise ValueError("Unable to determine bounding box for cropping")

        return image.crop(bbox)


class ManualCropper(Cropper):
    """
    Performs manual-cropping
    """

    def __init__(self):
        self.dimensions: Union[None, Tuple[int, int, int, int]] = None

    def crop(self, image: Image) -> Image:
        if not self.dimensions:
            msg = "No dimensions provided. Dimensions must be a tuple of four integers (left, upper, right, lower)"
            raise ValueError(msg)

        if not all(isinstance(n, int) for n in self.dimensions):
            raise TypeError("All dimensions must be integers")

        if len(self.dimensions) != 4:
            raise ValueError("Dimensions must be a tuple of four integers (left, upper, right, lower)")

        return image.crop(self.dimensions)
