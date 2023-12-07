# Import OpenCV, NumPy, and Matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('ATU1.jpg')

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#nrow and ncols
nrow = 2
ncol = 1

# Plotting images with Matplotlib
plt.subplot(nrow, ncol, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 2), plt.imshow(imgGray, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()