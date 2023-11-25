"""
Module which handles background removal from pics using Pillow
"""
from ctypes import Union
from pathlib import Path

from PIL import Image, ImageFilter


def process_image_with_edge_removal(input_path: Path, output_path: Union[Path,False], tolerance: int = 50,
                                    edge_tolerance: int = 50):
    # Open the image
    img = Image.open(input_path).convert("RGBA")

    # Get the background color (assuming it's the color of the top-left pixel)
    bg_color = img.getpixel((0, 0))

    # Convert img to grayscale for better edge detection and create an edge mask
    edge_mask = img.convert("L").filter(ImageFilter.FIND_EDGES)

    data = img.getdata()
    edge_data = edge_mask.getdata()
    new_data = []
    for i, item in enumerate(data):
        if edge_data[i] > 0:  # If the pixel is on an edge
            if all(abs(item[j] - bg_color[j]) <= edge_tolerance for j in range(3)):
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)
        else:
            if all(abs(item[j] - bg_color[j]) <= tolerance for j in range(3)):
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)

    img.putdata(new_data)
    if not output_path:
        output_path = Path(f"{input_path}_PIL_converted.png")
    else:
        filename = input_path.name
        output_path = Path(f"converted/{filename}_PIL_converted.png")

    img.save(output_path, "PNG")
