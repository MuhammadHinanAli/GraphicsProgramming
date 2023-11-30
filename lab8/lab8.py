import cv2
import numpy as np
from matplotlib import pyplot as plt

print("Hello World") #TO SEE WORKING OR NOT

img = cv2.imread('ATU.jpg',) #img Variable to image read the jpg/photo #https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
cv2.imshow('Original', img) #Shows/Displays img variable
cv2.waitKey(0)  

# Convert to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale', imgGray) #Shows/Displays imgGray variable
cv2.waitKey(0) 

#nrows and ncols variable
nrows = 2
ncols = 1

#Convert the channels
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#displays photos together using subplot/mathplot 
plt.subplot(nrows, ncols,1),plt.imshow(img , cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()

