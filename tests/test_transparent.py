import os
from pathlib import Path

import pytest
from logo_bg_vanisher.folder_utils import load_image
from logo_bg_vanisher.remover_pillow import PillowBackgroundRemoval
from logo_bg_vanisher.remover_rmbgr import RmbgrBackgroundRemoval
from logo_bg_vanisher.saver import SavePic

TEST_FOLDER = Path(__file__).parents[0]


@pytest.fixture
def file() -> Path:
    return TEST_FOLDER / "logo/logo.png"


@pytest.fixture
def input_path() -> Path:
    return TEST_FOLDER / "logo/"


@pytest.fixture
def expected_pillow() -> Path:
    return TEST_FOLDER / "logo/logo_PIL_converted.png"


@pytest.fixture
def expected_rmbg() -> Path:
    return TEST_FOLDER / "logo/logo_rmbgr_converted.png"


def test_transparent_pillow(file, expected_pillow):
    image_object = load_image(picture=file)
    remover = PillowBackgroundRemoval(img=image_object)
    image_object = remover.remove_background()
    image_saver = SavePic(img=image_object)
    image_saver.save_image(suffix="PIL_converted")

    # Check if processed image was created
    assert expected_pillow.exists(), "Processed image file does not exist"

    # Open the processed image and check for transparency
    assert image_object.mode == 'RGBA', "Image is not in RGBA mode"
    corner_pixel = image_object.getpixel((0, 0))
    assert corner_pixel[3] == 0, "Background is not transparent"

    # Clean up
    os.remove(expected_pillow)


def test_removal_rmbg(file, expected_rmbg):
    image_object = load_image(picture=file)
    remover = RmbgrBackgroundRemoval(img=image_object)
    image_object = remover.remove_background()

    image_saver = SavePic(img=image_object)
    image_saver.save_image(suffix="rmbgr_converted")
    # Test that the processed image was created
    assert expected_rmbg.exists(), "Processed image file does not exist"

    # Open the processed image and check for transparency
    assert image_object.mode == 'RGBA', "Image is not in RGBA mode"
    corner_pixel = image_object.getpixel((0, 0))
    assert corner_pixel[3] == 0, "Background is not transparent"

    # Clean up
    os.remove(expected_rmbg)
