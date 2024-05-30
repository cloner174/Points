# ImageRelated

#### *Some Scripts for Enhancing and More, with Images.*


# Enhanced Image Processing Script

## Introduction
This Python script, titled "Enhanced Image Processing Script", is an enhanced version of the original image processing examples provided by OpenCV. It includes functionalities for applying erosion and dilatation transformations to images. This script can be used for educational purposes or integrated into larger image processing projects.

## Features
- **Erosion and Dilatation**: Apply morphological transformations to enhance or reduce features in images.
- **Flexible File Handling**: Load images from file paths or directly from images in memory.
- **Visualization**: Compare original and transformed images side by side.
- **Save Results**: Optionally save the resulting images with a timestamp and transformation details.

## Prerequisites
Before running the script, ensure you have Python installed on your system. This script is compatible with Python 3.6 or higher.

## Installation
To run this script, you need to install several dependencies. The required libraries are listed in the `requirements.txt` file. Install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use this script, you need to create an instance of the ErosAndDilat class with either a path to an image file or an image object. Here's a quick example on how to use the class:

```python

from enhancements import ErosAndDilat

# Initialize with an image path
image_processor = ErosAndDilat('path/to/your/image.jpg')

# Perform erosion and dilatation, display results, and save them
image_processor.main(eros=True, dilate=True, show=True, save=True)
```
## Parameters

    eros: Enable erosion (default: True)
    dilate: Enable dilatation (default: True)
    show: Display the images using matplotlib (default: True)
    save: Save the images to disk (default: False)
    save_path: Directory to save the images (default: 'results')
    file_name: Base file name for saved images (default: None)

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.
License

    This project is open-sourced under the MIT License. See the LICENSE file for more details.
## Acknowledgements

Special thanks to the OpenCV community for providing the base examples which were enhanced in this project. Also, check out the original script and documentation at OpenCV GitHub.
## Contact

For more information, please contact: cloner174.org@gmail.com