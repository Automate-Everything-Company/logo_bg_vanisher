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

    def __init__(self, img: Image):
        self.image = img

    @abstractmethod
    def crop_image(self) -> Image:
        """
        Abstract method for cropping objects.
        :return: Pillow image
        """


class AutoCropper(Cropper):
    """
    Performs auto-cropping
    """

    def __init__(self, img):
        super().__init__(self)
        self.image = img
        self.filename = img.filename

    def crop_image(self) -> Image:
        if self.image.mode != 'RGBA':
            raise ValueError("Image must be in RGBA mode for auto cropping")

        bbox = self.image.getbbox()
        if bbox is None:
            raise ValueError("Unable to determine bounding box for cropping")
        cropped_image = self.image.crop(bbox)
        cropped_image.filename = self.filename
        return cropped_image


class ManualCropper(Cropper):
    """
    Performs manual-cropping
    """

    def __init__(self, img: Image, dimensions: Union[None, Tuple[int, int, int, int]]):
        super().__init__(self)
        self.image = img
        self.filename = img.filename
        self.dimensions = dimensions

    def crop_image(self) -> Image:
        if not self.dimensions:
            msg = "No dimensions provided. Dimensions must be a tuple of four integers (left, upper, right, lower)"
            raise ValueError(msg)

        if not all(isinstance(n, int) for n in self.dimensions):
            raise TypeError("All dimensions must be integers")

        if len(self.dimensions) != 4:
            raise ValueError("Dimensions must be a tuple of four integers (left, upper, right, lower)")
        cropped_image = self.image.crop(self.dimensions)
        cropped_image.filename = self.filename
        return cropped_image
