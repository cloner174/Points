import datetime
import os

def save_path_generator(filename = None, path = None, flag = None):
        
        try:
                if path is not None:
                        path = path
                else:
                        path = 'results'
                os.makedirs(path,exist_ok=True)
                if filename is not None:
                        if not filename.endswith('.png') or not filename.endswith('.jpg'):
                                filename = filename + '.png'
                else:
                        now = datetime.datetime.now()
                        now = now.strftime('%Y%m%d-%H%M%S')
                        filename = f'Fig{now}.png'
                if flag is not None:
                        filename = str(flag) + filename
                savepath = os.path.join(path,filename)
        except Exception as e:
                raise Exception(f"{e}")
        
        return savepath