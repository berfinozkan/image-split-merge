import cv2
import numpy as np

# resmi yükle
img = cv2.imread("input.jpg")

h, w = img.shape[:2]

# ---------------- PARÇALA ----------------
left = img[:, :w//2]
right = img[:, w//2:]

cv2.imwrite("left.jpg", left)
cv2.imwrite("right.jpg", right)

print("Resim iki parçaya bölündü")

# ---------------- BİRLEŞTİR ----------------
left = cv2.imread("left.jpg")
right = cv2.imread("right.jpg")

result = np.hstack((left, right))

cv2.imshow("left", left)
cv2.imshow("right", right)
cv2.imshow("SONUC", result)
cv2.imwrite("result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Resim tekrar birleştirildi")