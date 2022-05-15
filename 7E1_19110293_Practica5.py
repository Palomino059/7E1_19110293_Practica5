import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Pergamino.jpg')
imgris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaus = cv2.adaptiveThreshold(imgris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,155,1)

cv2.imshow('Original',img)
cv2.imshow('Gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
u,img1 = cv2.threshold(imgris,127,255,cv2.THRESH_BINARY)
u,img2 = cv2.threshold(imgris,127,255,cv2.THRESH_BINARY_INV)
u,img3 = cv2.threshold(imgris,127,255,cv2.THRESH_TRUNC)
u,img4 = cv2.threshold(imgris,127,255,cv2.THRESH_TOZERO)
u,img5 = cv2.threshold(imgris,127,255,cv2.THRESH_TOZERO_INV)

"------------ OTSU -------------------"
u,img6 = cv2.threshold(imgris,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
u,img7 = cv2.threshold(imgris,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
u,img8 = cv2.threshold(imgris,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
u,img9 = cv2.threshold(imgris,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
u,img10 = cv2.threshold(imgris,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)



imagenes = [imgris,img1,img2,img3,img4,img5] 
titulo = ['Gris','BINARY','BINARY_INV','TRUNC','TOZERO','TROZERO_INV']

for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(imagenes[i],'gray',vmin = 0,vmax = 255);
    plt.title(titulo[i])
    plt.xticks([]),plt.yticks([])

plt.show()
print(u)

imagenes2 = [imgris,img6,img7,img8,img9,img10] 
titulo2 = ['Gris','BINARY_OTSU','BINARY_INV_OTSU','TRUNC_OTSU','TOZERO_OTSU','TROZERO_INV_OTSU']

for x in range(6):
    plt.subplot(3,2,x+1)
    plt.imshow(imagenes2[x],'gray',vmin = 0,vmax = 255);
    plt.title(titulo2[x]) 
    plt.xticks([]),plt.yticks([])

plt.show()
print(u)
