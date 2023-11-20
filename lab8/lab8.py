import cv2
import numpy as np
from matplotlib import pyplot as plt

print("Hello World") #TO SEE WORKING OR NOT

img = cv2.imread('ATU.jpg',) #img Variable to image read the jpg/photo
cv2.imshow('Coloured', img) #Shows/Displays img variable
cv2.waitKey(0)  

# Convert to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Scale', imgGray) #Shows/Displays img variable
cv2.waitKey(0) 

