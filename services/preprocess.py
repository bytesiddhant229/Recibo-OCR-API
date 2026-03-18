import cv2 #openCV
import numpy as np

def preprocess_image(image_np: np.ndarray):

    resizedImage = cv2.resize(image_np, None, fx=0.5, fy=0.5) # resizing image for faster processing

    grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_RGB2GRAY) # convert it into grayimage

    return grayImage
