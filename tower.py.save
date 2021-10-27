import cv2

cam = cv2.VideoCapture(0)

ret, image = cam.read()

print("Printing Image")
cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()
