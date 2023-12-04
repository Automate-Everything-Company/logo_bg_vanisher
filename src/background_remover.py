"""
Interface for background removal
"""

from abc import ABC, abstractmethod

from PIL import Image


class BackgroundRemovalStrategy(ABC):
    """
    Interface for background removers
    """

    def __init__(self, img: Image):
        self.image = img

    @abstractmethod
    def remove_background(self) -> Image:
        """
        :return:  Pillow Image object
        """
        pass
