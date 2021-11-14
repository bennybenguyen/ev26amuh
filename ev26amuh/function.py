import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

# Beispielbild erstellen
width = 256
height = 256

array = np.zeros([height, width, 3], dtype=np.uint8)
array[:, :128] = [255, 128, 0]  # fill img orange left side, howto: https://pythoninformer.com/python-libraries/numpy/numpy-and-images/
array[:, 128:] = [0, 0, 255]  # Blue right side


def imshow(X, resize=None):
    # resize funktion von pillow https://www.geeksforgeeks.org/python-pil-image-resize-method/
    newsize = (300, 300)
    resized_img = X.resize(newsize)
    # imshowmit resize
    X.imshow()
    pass


#imshow(array, 0)
