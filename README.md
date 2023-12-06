# LogoBgVanisher
LogoBgVanisher is a Python tool designed for quick and efficient background removal from AI-generated logos. 
It utilizes popular libraries like Pillow and Rembg to handle a variety of background issues.

## Overview
This tool addresses common challenges in AI-generated logos, such as refining gray areas, 
completely removing backgrounds, resizing and cropping.

## Key Features
- Support for both Pillow and Rembg methods
- Automated and manual image cropping options
- Image resizing with aspect ratio preservation
- Command-line interface for ease of use

## Example
### Original image generated with DALL-E 3:
<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/automate-everything-company/logo_bg_vanisher/main/examples/DALL-E_LOGO_ORIGINAL.png"/>
</p>

### Step 1, removing background:
<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/automate-everything-company/logo_bg_vanisher/master/examples/DALL-E_LOGO_ORIGINAL_converted_pillow.png"/>
</p>

### Step 2, auto-cropping:
<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/automate-everything-company/logo_bg_vanisher/master/examples/DALL-E_LOGO_ORIGINAL_converted_pillow_cropped.png"/>
</p>

### Step 3, resizing (to half the size):
<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/automate-everything-company/logo_bg_vanisher/master/examples/DALL-E_LOGO_ORIGINAL_converted_pillow_scaled_cropped.png"/>
</p>

## Installation
To install, run: 
```shell
pip install logo_bg_vanisher
```

## Usage
Run the following commands in your terminal:

### Using Pillow
To use Pillow, run: 
logo_bg_vanisher --file <file_path> [--resize <width,height>] [--crop <method>] --method pillow
or
logo_bg_vanisher --input_path <folder_path> [--resize <width,height>] [--crop <method>] --method pillow

### Using Rembg
Replace the method with '--method rembg'

Replace <file_path> or <folder_path> with your image or folder's path. 
For resizing, input width,height or just width for aspect ratio: --resize 512,512 
For cropping, use auto for automatic or width,height for manual: --crop auto

## Requirements
- Python 3.7 or higher
- Pillow
- rembg

## License
MIT License. See LICENSE for details.

## Contact
Reach out at info@automate-everything-company.com for support or inquiries.

## cknowledgments
Inspired by Daniel Gatis's rembg (https://github.com/danielgatis/rembg).
