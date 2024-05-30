import tempfile
from PIL import Image
import matplotlib.pyplot as plt
from utils import save_path_generator
import os

def invert_image_color(image, save = False, save_path = None, file_name = None):
    
    if isinstance(image, str):
        with Image.open(image) as img:
            img = img
    else:
        try:
            img = Image.fromarray(image)
        except Exception as e:
            TypeError(f" You Should pass a valid path to a valid image ! to this Function could work! \n in addition: {e}")
    img = img.convert('RGBA')
    datas = img.getdata()
    new_data = []
    for item in datas:
        
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((0, 0, 0, 255))
        else:
            new_data.append((255, 255, 255, 255))
    img.putdata(new_data)
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        img.save(tmp.name)
        tmp.seek(0)
        inverted_image = plt.imread(tmp.name)
    os.unlink(tmp.name)
    if save:
        save_path = save_path_generator(file_name,  save_path, flag=None)  
        plt.imsave(save_path, inverted_image)
    
    return inverted_image