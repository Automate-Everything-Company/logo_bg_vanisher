"""
Interface for background removal
"""

from abc import ABC, abstractmethod

from PIL import Image


class BackgroundRemovalStrategy(ABC):
    """
    Interface for background removers
    """

    @abstractmethod
    def remove_background(self, img: Image) -> Image:
        """
        :param img: Pillow Image object
        :return:  Pillow Image object
        """
        pass
