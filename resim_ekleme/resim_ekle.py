import cv2 as cv 
img=cv.imread("resim1.jpg",0)
cv.imshow("manas",img)

k=cv.waitKey(0) &0xFF
if k==27: #27 esc nin sayısal karşılığıdır.
   cv.destroyAllWindows()
elif k==ord("s"):
    cv.imwrite("resim.jpg",img)
    cv.destroyAllWindows()