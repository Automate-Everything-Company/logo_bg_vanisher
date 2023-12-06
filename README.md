# LogoBgVanisher

LogoBgVanisher is a Python tool designed for quick and efficient background removal from AI-generated logos. 
It utilizes popular libraries like Pillow and Rmbg to handle a variety of background issues.

## Overview
This tool addresses common challenges in AI-generated logos, such as refining gray areas or completely removing backgrounds. 
It's user-friendly and integrates advanced techniques for complex scenarios, making it ideal for both beginners and experienced users.

## Key Features
- Support for both Pillow and rmbg methods
- Automated and manual image cropping options
- Image resizing with aspect ratio preservation
- Command-line interface for ease of use

## Installation
```shell
pip install logo_bg_vanisher
```

## Installation
python3 src/main.py --file <file_path> [--resize <width,height>] [--crop <method>] --method pillow [--verbose]
