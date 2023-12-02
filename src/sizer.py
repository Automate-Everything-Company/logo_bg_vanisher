"""
Module which handles the sizing
"""
from abc import ABC, abstractmethod
from typing import Union

import PIL
from PIL import Image


class Sizer(ABC):
    """
    Interface for sizer objects
    """

    @abstractmethod
    def set_size(self, image: Image) -> Image:
        """
        Abstract method for sizer objects.
        :return: Pillow image
        """


class AspectRatioSizer(Sizer):
    """
    Changes the picture size while keeping the aspect ratio.
    """

    def __init__(self):
        self.width: Union[None, int] = None

    def set_size(self, image: Image) -> Image:
        if not self.width:
            raise ValueError("No width provided. The width must be an integer")
        else:
            new_height = self._calculate_height(img=image)
            resized_img = image.resize(size=(self.width, new_height))
            return resized_img

    def _calculate_height(self, img: Image):
        """
        Calcules for the user given width the new height in order to keep the original aspect ratio.
        :param img: Pillow Image object
        :return: New calculated height
        """
        w_percent = (self.width / float(img.size[0]))
        new_height = int((float(img.size[1]) * float(w_percent)))
        return new_height


class ManualSizer(Sizer):
    """
    Changes the picture size from user width and height
    """

    def __init__(self):
        self.width: Union[None, int] = None
        self.height: Union[None, int] = None

    def set_size(self, image: Image) -> Image:
        if not all((self.width, self.height)):
            raise ValueError("Width and height must be provided in integer form (width, height)")
        else:
            resized_img = image.resize((self.width, self.height), Image.ANTIALIAS)
            return resized_img
