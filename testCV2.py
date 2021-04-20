import numpy as np, cv2, time, os

# shrek = cv2.imread("images/shrek.png")

# cv2.imshow("output", shrek)

# testVid = cv2.VideoCapture("images/testVideo.mov")
testVid = cv2.VideoCapture(0)
testVid.set(3, 640)
testVid.set(4, 480)

while True:
    test, image = testVid.read()
    cv2.imshow("output", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam = cv2.VideoCapture(0)
print(cam.isOpened())
cam.release()

"""
cv2.waitKey(1)
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)
return
"""


