import numpy as np
import ipywidgets as IWG
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt

# Beispielbild erstellen
#width = 256
#height = 256
#array = np.zeros([height, width, 3], dtype=np.uint8)
#array[:, :128] = [1, 0.5, 0]
#array[:, 128:] = [0, 0, 1]  # Blue right side


def imshow(X, resize=None):
    im = Image.fromarray(np.uint8(X * 255))  # make np array PIL Object
    # resize function von pillow
    if resize != None:
        resized_img = im.resize(resize)
        plt.figure()
        plt.imshow(resized_img)
        plt.show()
        return resized_img
    else:
        plt.figure()
        plt.imshow(im)
        plt.show()
        return im


#imshow(array, (array.shape[0] // 2, array.shape[1] // 2)) # / float // integer division
