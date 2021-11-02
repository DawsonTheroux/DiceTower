import cv2
import numpy as np
import math

cam = cv2.VideoCapture(0)
	
def analyzeImage(filename):
	ret, image = cam.read()
	print(ret)
	print("x: " + str(image.shape[0]) + "y: " + str(image.shape[1]))

	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("../Gray" + filename + ".jpg",image)
	image = cv2.blur(image, (3,3))	#Blur the imaget to help with binary detection.
	cv2.imwrite("../Blur" + filename + ".jpg",image)
	ret, image = cv2.threshold(image, 50, 255, cv2.THRESH_TOZERO) #Turn into binary image.
	cv2.imwrite("../Threshold" + filename + ".jpg",image)
	image = cv2.Canny(image, 80, 230) #Create contour lines of the binary image.
	cv2.imwrite("../Canny" + filename + ".jpg",image)
	dummy,contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	#Rantagles detected using the contours of the algorithm above.
	dice_rects = []
	i = 0
	print("Contours:" + str(len(contours)))

	for contour in contours:
		rect = cv2.minAreaRect(contour)
		rectH = rect[1][1]
		rectW = rect[1][0]

		if rectW == 0 or rectH == 0:
			continue
		else:
			aspect = math.fabs(rectW/rectH - 1)

		if aspect < 0.25 and (rectW * rectH) > 2000:		#Check if the aspect ratio is close to a square and the area is more than 2000 pixels.
			process = True
			for i in range(len(dice_rects)):
				if rect[0][0] - dice_rects[i][0][0] < 5 and rect[0][1] - dice_rects[i][0][1] < 5:
					process = False
					break
			if process:
				i += 1
				dice_rects.append(rect)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				image = cv2.drawContours(image, [box], 0, (0,0,255),3)
				cv2.imwrite("../Contour" + str(i) + filename + ".jpg",image)
	print("Number Dice:" + str(len(dice_rects)))

	image = cv2.putText(image, "Dice: " + str(len(dice_rects)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
	cv2.imwrite("../Final" + filename + ".jpg", image)
filename = "default.jpg"
while(True):
	key = raw_input("Give a command: ")
	if key == "q" or key  == "Q":
		break
	else:
		analyzeImage(key)
		print("Done Analyzing")

print("Printing Image")
#cv2.imwrite('../testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()
