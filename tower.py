import cv2

cam = cv2.VideoCapture(0)
ret, image = cam.read()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.blur(image, (2,2))	#Blur the imaget to help with binary detection.

ret, image = cv2.threshold(image, 50, 255, cv2.THRESH_TOZERO) #Turn into binary image.

image = cv2.Canny(image, 80, 230) #Create contour lines of the binary image.

dummy,contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Rantagles detected using the contours of the algorithm above.
dice_rects = []

for contour in contours:
	x,y,w,h = cv2.boundingRect(contour)
	rect = [x,y,w,h]
	dice_rects.append(rect)
	if w>5 and h>10:
		cv2.rectangle(image,(x,y),(x+w,y+h),(155,155,0),1)
	
	print("Number Dice:" + str(len(dice_rects)))

image = cv2.putText(image, "Dice: " + str(len(dice_rects)), (10,10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

print("Printing Image")
cv2.imwrite('../testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()
