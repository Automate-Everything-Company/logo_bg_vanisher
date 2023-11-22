from tkinter import filedialog
from tkinter import Tk
from PIL import Image
import os

from PIL import Image

def remove_white_background(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGBA (if it's not already)
    img = img.convert("RGBA")

    # Get the alpha channel
    alpha = img.split()[3]

    # Iterate over each pixel and modify the alpha channel based on whether the pixel is white
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if pixel[:3] == (255, 255, 255):  # If the pixel is white
                alpha_value = 0  # Set alpha channel to 0 (fully transparent)
            else:
                alpha_value = pixel[3]  # Use the existing alpha value

            # Modify the pixel with the updated alpha channel value
            img.putpixel((x, y), (pixel[0], pixel[1], pixel[2], alpha_value))

    # Save the image with no background as PNG
    img.save(output_path, format='PNG')


def process_images(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(folder_path, filename)
            
            # Change the output extension to '.png'
            output_filename = f"no_bg_{os.path.splitext(filename)[0]}.png"
            output_path = os.path.join(output_folder, output_filename)
            
            remove_white_background(input_path, output_path)
            print(f"Processed: {filename}")


def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder")

    return folder_path

if __name__ == "__main__":
    # Get the folder path from the user using a GUI
    folder_path = select_folder()

    if not folder_path:
        print("No folder selected. Exiting.")
    else:
        # Get the output folder path
        output_folder = os.path.join(folder_path, "no_bg")

        # Process the images in the selected folder
        process_images(folder_path, output_folder)

        print("Images processed and saved with no background.")
