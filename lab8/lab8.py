# Import OpenCV, NumPy, and Matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('ATU.jpg')

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Plotting images with Matplotlib
plt.subplot(2, 1, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 1, 2), plt.imshow(imgGray, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.show()
