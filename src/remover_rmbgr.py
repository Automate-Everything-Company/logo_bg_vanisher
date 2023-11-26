"""
Module which handles background removal from pics using rmbgr
"""
from typing import Union
from pathlib import Path
import rembg

from background_remover import BackgroundRemovalStrategy


class RmbgrBackgroundRemoval(BackgroundRemovalStrategy):
    def __init__(self):
        self.suffix = "converted_rmbgr"

    def remove_background(self, input_path: Path, output_path: Union[bool, Path] = False) -> None:
        input_data = self._open_image(input_path)
        output_data = rembg.remove(input_data)
        self._save_picture(input_path=input_path, output_path=output_path, output_data=output_data)

    @staticmethod
    def _open_image(input_path):
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        return input_data

    def _save_picture(self, input_path: Path, output_path: Path, output_data: bytes) -> None:
        if not output_path:
            output_path = Path(f"{input_path.stem}_{self.suffix}.png")
        else:
            if not output_path.is_dir():
                output_path.mkdir(parents=True, exist_ok=True)
                output_path = output_path / f"{input_path.stem}_{self.suffix}.png"
            else:
                output_path = output_path / f"{input_path.stem}_{self.suffix}.png"
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
