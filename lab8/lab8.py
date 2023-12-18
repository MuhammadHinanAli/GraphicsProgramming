# Import OpenCV, NumPy, and Matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('ATU.jpg')
#img = cv2.imread('STADIUM.jpg')

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

# Apply GaussianBlur with different kernel sizes
kernel_sizes = [3, 5, 9, 13]

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Grayscale'), plt.xticks([]), plt.yticks([])

for i, kernel_size in enumerate(kernel_sizes):
    if i < 3:  # Limit the number of subplots to 3

        imgOut = cv2.GaussianBlur(imgGray, (kernel_size, kernel_size), 0)
        
        # Plotting images with Matplotlib
        plt.subplot(2, 2, i + 2), plt.imshow(imgOut, cmap='gray')
        plt.title(f'Blurred (Kernel {kernel_size})'), plt.xticks([]), plt.yticks([])
plt.show()

# Sobel edge detection
sobelHorizontal = cv2.Sobel(imgGray, cv2.CV_64F, 1, 0, ksize=5)
sobelVertical = cv2.Sobel(imgGray, cv2.CV_64F, 0, 1, ksize=5)

# Plot Sobel output images
#plt.subplot(1, 2, 1), plt.imshow(sobelHorizontal, cmap='gray')
#plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])
#plt.subplot(1, 2, 2), plt.imshow(sobelVertical, cmap='gray')
#plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])
#plt.show()

# Combine horizontal and vertical edges
sobelCombined = cv2.addWeighted(sobelHorizontal, 0.5, sobelVertical, 0.5, 0)

# Plot combined Sobel output
#plt.imshow(sobelCombined, cmap='gray')
#plt.title('Combined Sobel Edges'), plt.xticks([]), plt.yticks([])
#plt.show()

# Canny edge detection
cannyThreshold = 100
cannyParam2 = 200
canny = cv2.Canny(imgGray, cannyThreshold, cannyParam2)

# Plot Canny edge detection result
#plt.imshow(canny, cmap='gray')
#plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
#plt.show()

#nrow and ncols
nrow = 2
ncol = 3

# Plotting images with Matplotlib
plt.subplot(nrow, ncol, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 2), plt.imshow(imgGray, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 3), plt.imshow(sobelHorizontal, cmap='gray')
plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 4), plt.imshow(sobelVertical, cmap='gray')
plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 5),plt.imshow(sobelCombined, cmap='gray')
plt.title('Combined Sobel Edges'), plt.xticks([]), plt.yticks([])
plt.subplot(nrow, ncol, 6),plt.imshow(canny, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
plt.show()