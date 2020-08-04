import cv2
from imutils import paths
import numpy as np
import imutils

def distance_to_camera(objWdth, fclLnth, perWdth):
	# calculating distance between camera and object
	return (objWdth * fclLnth) / perWdth

# object pre-defined distance from the camera
objDist = 12

# object pre-defined width
objWdth = 6.5

# reading pre-defined image
image = cv2.imread("images/1.jpeg")
# finding contour in image
marker = find_marker(image)
# manipulating focal length through pre-defined data
fclLnth = (marker[1][0] * objDist) / objWdth

lst = []
# accessing images from folder
for i in range(1, 5):
	lst.append(str(i) + '.jpeg')