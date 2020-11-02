# OpenCV Threshold Program, It display its orginal, binary threshold, Gause Threshold, and Otsu Threshold.
# There should be image name page.png is the same folder.
# Press any key to exit.
import cv2

img1 = cv2.imread("page.png")
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img1_gray, 10, 250, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(img1_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1.5)
ret2, otsu = cv2.threshold(img1_gray, 125, 200, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Orginal", img1)
cv2.imshow("Binary Thershold", threshold)
cv2.imshow("GAUS Threshold", gaus)
cv2.imshow("OSTU Threshold", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()