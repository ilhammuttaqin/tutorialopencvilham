import cv2
img = cv2.imread('Kucing.jpg',1)

width=600
height=450
size=(width,height)

baru=cv2.resize(img,size)

cv2.imshow('gambar kucing',baru)
cv2.waitKey(0)
cv2.destroyAllWindows()
