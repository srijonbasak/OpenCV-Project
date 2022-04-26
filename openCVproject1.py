import cv2
import numpy as np
import matplotlib.pyplot as plt

def readimg(x):
    img = cv2.imread(x)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
def display(x):
    plt.imshow(x)

display(readimg('cat-head.jpg'))