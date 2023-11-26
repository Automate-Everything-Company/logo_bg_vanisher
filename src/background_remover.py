"""
Interface for background removal
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union


class BackgroundRemovalStrategy(ABC):
    """
    Interface for background removers
    """

    @abstractmethod
    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        """
        :param input_path: Path object to a user specified directory
        :param output_path: Optional argument to a user specified directory, in case the converted pic should be saved
        in anoter folder
        :return: None
        """
        pass
