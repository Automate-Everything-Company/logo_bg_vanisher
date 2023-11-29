import os
import pytest
from pathlib import Path
from PIL import Image

from src import RmbgrBackgroundRemoval
from src.remover_pillow import PillowBackgroundRemoval

TEST_FOLDER = Path(__file__).parents[0]


@pytest.fixture
def input_path() -> Path:
    return TEST_FOLDER / "logo/logo.png"


@pytest.fixture
def output_path() -> Path:
    return TEST_FOLDER / "logo/"


@pytest.fixture
def output_filename_pillow() -> Path:
    return TEST_FOLDER / "logo/logo_pillow_converted.png"


@pytest.fixture
def output_filename_rmbg() -> Path:
    return TEST_FOLDER / "logo/logo_rmbgr_converted.png"


def test_transparent_pillow(input_path, output_path, output_filename_pillow):
    remover = PillowBackgroundRemoval()
    remover.remove_background(input_path=input_path, output_path=output_path)
    # Test that the processed image was created
    assert output_filename_pillow.exists(), "Processed image file does not exist"

    # Open the processed image and check for transparency
    with Image.open(output_filename_pillow) as processed_img:
        assert processed_img.mode == 'RGBA', "Image is not in RGBA mode"
        corner_pixel = processed_img.getpixel((0, 0))
        assert corner_pixel[3] == 0, "Background is not transparent"
    # Clean up

    os.remove(output_filename_pillow)


def test_removal_rmbg(input_path, output_path, output_filename_rmbg):
    remover = RmbgrBackgroundRemoval()
    remover.remove_background(input_path=input_path, output_path=output_path)
    # Test that the processed image was created
    assert output_filename_rmbg.exists(), "Processed image file does not exist"

    # Open the processed image and check for transparency
    with Image.open(output_filename_rmbg) as processed_img:
        assert processed_img.mode == 'RGBA', "Image is not in RGBA mode"
        corner_pixel = processed_img.getpixel((0, 0))
        assert corner_pixel[3] == 0, "Background is not transparent"
    # Clean up

    os.remove(output_filename_rmbg)
