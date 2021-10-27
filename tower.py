import cv2

cam = cv2.VideoCapture(0)
ret, image = cam.read()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.blur(image, (3,3))
ret, image = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)

print("Printing Image")
cv2.imwrite('../testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()
