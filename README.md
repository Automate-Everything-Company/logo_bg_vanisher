# AI Logo Background Remover

This Python tool is designed to efficiently remove backgrounds from AI-generated logos, leveraging the power of popular libraries like Pillow and rmbg. 
It offers a straightforward and simple user interface.

## Inspiration
The package draws inspiration from the need to handle common issues encountered in AI-generated logos, 
such as gray areas in black and white logos or the complete removal of backgrounds. 
These tasks can be challenging and often require sophisticated tools. 
This package simplifies the process, making it accessible to a wider audience.

## Motivation
While image generator models like DALL-E produce high-quality logos, they sometimes leave behind undesired backgrounds. 
This package aims to address these issues by providing an easy-to-use solution for background removal, 
incorporating machine learning techniques for more complex scenarios.

## Features
- Easy background removal from AI-generated logos
- Supports both Pillow and rmbgr methods
- Simple command-line interface

## Installation
To install AI Logo Background Remover, run:
```shell
pip install your_package_name
```

## Usage
### Pillow
To remove the background with Pillow run:
```shell
python3 src/main.py --input_path <your_input_path> --output_path <your_output_path> --method pillow
```
### Rmbg
To remove the background with Rmbg run:
```shell
python3 src/main.py --input_path <your_input_path> --output_path <your_output_path> --method rmbgr
```

## Requirements
- Python 3.7+
- Pillow
- rembg

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support or inquiries, please contact us at [info@automate-everything-company.com](mailto:info@automate-everything-company.com).

## Acknowledgments
- This project was inspired by [https://github.com/danielgatis/rembg](mailto:info@automate-everything-company.com).
