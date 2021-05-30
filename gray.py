import cv2

img = cv2.imread('Kucing.jpg',0)
width=600
height=450
size=(width,height)

baru=cv2.resize(img,size)

if not img is None:
    cv2.imshow('gambar kucing',baru)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
