import cv2

image = cv2.imread('solar-system.jpg')

cv2.putText(image, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Mercury", (110,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Venus", (200,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Earth", (290,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Mars", (380,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Jupiter", (550,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Saturn", (750,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Uranus", (960,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(image, "Neptune", (1110,220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))


cv2.imshow("Output", image)
cv2.waitKey(0)

