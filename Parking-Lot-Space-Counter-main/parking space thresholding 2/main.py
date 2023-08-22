import cv2
from matplotlib import pyplot as plt
import numpy as np

#Thresholding empty parking space:
img = cv2.imread("assets/parking_space_empty.PNG")
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_equalized = cv2.equalizeHist(img_grayscale)

ret, thresh = cv2.threshold(img_equalized, 235, 255, cv2.THRESH_BINARY)

plt.figure("Original empty parking space")
plt.imshow(img_color)

plt.figure("Grayscale empty parking space")
plt.imshow(img_grayscale, cmap="gray")

plt.figure("Histogram equalized parking space")
plt.imshow(img_equalized, cmap="gray")

plt.figure("Thresholded empty parking space")
plt.imshow(thresh, cmap="gray")

img_median = cv2.medianBlur(thresh, 19)

plt.figure("Thresholded empty parking space with median filter")
plt.imshow(img_median, cmap="gray")

result1 = img_median

#Thresholding parking space with car lighter than ground:
img = cv2.imread("assets/parking_space_light_car.PNG")
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_equalized = cv2.equalizeHist(img_grayscale)

ret, thresh = cv2.threshold(img_equalized, 235, 255, cv2.THRESH_BINARY)

plt.figure("Original parking space with car lighter than ground")
plt.imshow(img_color)

plt.figure("Grayscale parking space with car lighter than ground")
plt.imshow(img_grayscale, cmap="gray")

plt.figure("Histogram equalized parking space 2")
plt.imshow(img_equalized, cmap="gray")

plt.figure("Thresholded parking space with car lighter than ground")
plt.imshow(thresh, cmap="gray")

img_median = cv2.medianBlur(thresh, 19)

plt.figure("Thresholded parking space with car lighter than ground with median filter")
plt.imshow(img_median, cmap="gray")

result2 = img_median

#Thresholding parking space with car darkerer than ground:
img = cv2.imread("assets/parking_space_dark_car.PNG")
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_equalized = cv2.equalizeHist(img_grayscale)

ret, thresh = cv2.threshold(img_equalized, 235, 255, cv2.THRESH_BINARY)

plt.figure("Original parking space with car darker than ground")
plt.imshow(img_color)

plt.figure("Grayscale parking space with car darker than ground")
plt.imshow(img_grayscale, cmap="gray")

plt.figure("Histogram equalized parking space 3")
plt.imshow(img_equalized, cmap="gray")

plt.figure("Thresholded parking space with car darker than ground")
plt.imshow(thresh, cmap="gray")

img_median = cv2.medianBlur(thresh, 19)

plt.figure("Thresholded parking space with car darker than ground with median filter")
plt.imshow(img_median, cmap="gray")

result3 = img_median

#Scanning the resulting images:
print(result1, result2, result3)

def scanResults(img_median):
    for row in img_median:
        for col in row:
            if(col == 255):
                return True
    return False

if scanResults(result1):
    print("Parking space 1 is not available.")
else:
    print("Parking space 1 is available.")

if scanResults(result2):
    print("Parking space 2 is not available.")
else:
    print("Parking space 2 is available.")

if scanResults(result3):
    print("Parking space 3 is not available.")
else:
    print("Parking space 3 is available.")

plt.show()
