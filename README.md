# Simple-Space 
### *A Try at Better Understanding Space*

# Dim3

The `Dim3` class offers tools for visualizing and processing 3D point data in Python, using libraries such as `numpy`, `matplotlib`, and `scipy`. This class provides methods to rotate 3D points, plot 3D data, create grayscale images from 3D points, and fill gaps in binary images.

## Features

- **Rotate 3D Points**: Rotate points around a specified axis by a given angle in degrees.
- **Plot 3D Points/Mesh**: Visualize 3D points or a mesh, with customizable visual attributes.
- **Create Grayscale Image from 3D Points**: Project 3D points onto a 2D plane using the z-coordinate for intensity.
- **Fill Points in Binary Image**: Use morphological dilation to fill gaps in binary images.

## Installation

Ensure you have Python installed, along with the following packages:
- `numpy`
- `matplotlib`
- `scipy`

You can install these packages via pip if they are not already installed:

```bash
pip install numpy matplotlib scipy
```
## Usage
Initializing the Class

```python

from your_module import Dim3
dim3 = Dim3()
```
Rotating 3D Points

```python

points = np.array([[1, 1, 1], [2, 2, 2]])
rotated_points = dim3.rotate_3d_points(points, 45, 'z')
```
Plotting 3D Points or Mesh

```python

vertices = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]]
faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], [0, 1, 2, 3]]
dim3.plot_3d_points(vertices, faces)
```
Creating a Grayscale Image from 3D Points

```python

points = np.random.rand(100, 3) * 100
image = dim3.create_bool_image_from_3d_points(points)
```
Filling Points in a Binary Image

```python

binary_image = np.random.randint(0, 2, (500, 500), dtype=np.uint8)
filled_image = dim3.fill_points(binary_image)
```
## Documentation

For more detailed information on each method, refer to the inline documentation within the class methods.

## Mistakes and Corrections
To err is human, and nobody likes a perfect person! If you come across any mistakes or if you have questions, feel free to raise an issue or submit a pull request. Your contributions to improving the content are highly appreciated.

## License
This project is open-sourced under the `MIT License`. See the LICENSE file for more details.

## Contact

For more information, please contact: cloner174.org@gmail.com
