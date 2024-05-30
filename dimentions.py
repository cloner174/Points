import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.ndimage import binary_dilation


class Dim3:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def rotate_3d_points(points, theta, axis='z'):
        """Rotate 3D points around the specified axis by theta degrees."""
        theta = np.radians(theta)
        if axis == 'x':
                rot_matrix = np.array([
                        [1, 0, 0],
                        [0, np.cos(theta), -np.sin(theta)],
                        [0, np.sin(theta), np.cos(theta)]
                ])
        elif axis == 'y':
                rot_matrix = np.array([
                        [np.cos(theta), 0, np.sin(theta)],
                        [0, 1, 0],
                        [-np.sin(theta), 0, np.cos(theta)]
                ])
        else:  # Default
                rot_matrix = np.array([
                        [np.cos(theta), -np.sin(theta), 0],
                        [np.sin(theta), np.cos(theta), 0],
                        [0, 0, 1]
                ])
        
        return np.dot(points, rot_matrix.T)
    
    @staticmethod
    def plot_3d_points(v, f=None, axis = 'on', title = '3D Data Visualization', faces_colors = 'blue', alpha=0.75, linewidths=1, edgecolors='r', point_color='blue',show =True, save=False, file_name = None ):
        """
        Plot 3D points or a mesh from vertices and optionally faces.
        
        Parameters:
        - v: List of vertices where each vertex is a list or tuple [x, y, z].
        - f: Optional. List of faces, where each face is a list of indices of vertices forming that face.
        - axis: if 'on' shows the title for each axis -> 'X-axis' and 'Y-axis' and 'Z-axis'.
        - title: if set to  None  or an empty string  ''  it will remove the title in result.
        - faces_colors: Can be whether a single color or a list of colors. It's the color for face's points.
        - alpha: Transparency of the faces when plotting a mesh.
        - linewidths: Width of the edges when plotting a mesh.
        - edgecolors: Color of the edges when plotting a mesh.
        - point_color: Color of the points when plotting only points.
        Example usage:
        vertices = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]]
        faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], [0, 1, 2, 3]]
        plot_3d_data(vertices, faces)  # Plotting a mesh
        plot_3d_data(vertices)  # Plotting points
        """
        vertices = np.array(v)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        if f is not None:
                faces = np.array(f, dtype=int)
                for face in faces:
                        verts = vertices[face]
                        poly = Poly3DCollection([verts], alpha=alpha, linewidths=linewidths, edgecolors=edgecolors)
                        poly.set_facecolor(faces_colors)
                        ax.add_collection3d(poly)
        else:
                ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=point_color, alpha=alpha)
        
        ax.set_xlim([vertices[:, 0].min(), vertices[:, 0].max()])
        ax.set_ylim([vertices[:, 1].min(), vertices[:, 1].max()])
        ax.set_zlim([vertices[:, 2].min(), vertices[:, 2].max()])
        if axis == 'on':
                ax.set_xlabel('X-axis')
                ax.set_ylabel('Y-axis')
                ax.set_zlabel('Z-axis')
        if title is not None and title != '':
                if save == True and file_name is None:
                        if title != '3D Data Visualization':
                                file_name = title
                plt.title(title)
        if save:
                if file_name is not None:
                        if not file_name.endswith('.png') or not file_name.endswith('.jpg'):
                                file_name = file_name + '.png'
                else:
                        now = datetime.datetime.now()
                        now = now.strftime('%Y%m%d-%H%M%S')
                        file_name = f'Fig{now}.png'
                plt.savefig(file_name)
        if show:
                plt.show()
        else:
                plt.clf()
                plt.close()
                return
    
    @staticmethod
    def create_bool_image_from_3d_points(points, image_size=(500, 500)):
        """
        Create a grayscale image from 3D points by projecting them onto a 2D plane using the z-coordinate
        as intensity.
        Args:
        points (numpy.ndarray): An array of points with shape (N, 3), where each row represents a 3D point (x, y, z).
        image_size (tuple): The dimensions of the output image (width, height).
        
        Returns:
        numpy.ndarray: A grayscale image where pixels' intensity is based on the z-value of points.
        """
        # use z for intensity
        projected_points = points[:, :2]
        z_values = points[:, 2]
        
        min_vals = np.min(projected_points, axis=0)
        max_vals = np.max(projected_points, axis=0)
        scaled_points = (projected_points - min_vals) / (max_vals - min_vals) * (np.array(image_size) - 1)
        
        z_min = np.min(z_values)
        z_max = np.max(z_values)
        z_scaled = (z_values - z_min) / (z_max - z_min) * 255 if z_max > z_min else np.zeros_like(z_values)
        
        image = np.zeros(image_size, dtype=np.uint8)
        
        for (point, intensity) in zip(scaled_points.astype(int), z_scaled.astype(np.uint8)):
                current_intensity = image[point[1], point[0]]
                image[point[1], point[0]] = max(current_intensity, intensity)  # Use the maximum intensity if overlapping
        
        return image
    
    @staticmethod
    def fill_points(image, iterations=5, structure=None, structure_like = (3,3) ):
        """Fill in the gaps in a binary image using morphological dilation."""
        if structure is None:
                structure = np.ones(structure_like)
        filled_image = binary_dilation(image, structure=structure, iterations=iterations)
        
        return filled_image
    
#end#