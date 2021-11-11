import cv2 as cv
import numpy as np

src=cv.imread("Source.jpg")
###############
dst=np.zeros(src.shape,dtype="int32")
border_shift=25
replicate=cv.copyMakeBorder(src,border_shift,border_shift,border_shift,border_shift,cv.BORDER_REFLECT)
   
h,w=dst.shape[:2]
   
for x in range(h):
    for y in range(w):
        shift=np.random.randint(-5, 6)
        dst[x,y]=replicate[border_shift+x+shift,border_shift+y+shift]

cv.imwrite("glass.png",np.concatenate([src,dst],axis=1))
##################
b,g,r=cv.split(src)

intensity=np.zeros((src.shape[0],src.shape[1]),dtype="int32")
intensity=cv.add(0.299 *r ,0.587 * g , 0.144 * b)
intensity_rgb=np.zeros(src.shape,dtype="int32")
intensity_rgb[:,:,0]=intensity
intensity_rgb[:,:,1]=intensity
intensity_rgb[:,:,2]=intensity
cv.imwrite("GreyScale.png",np.concatenate([src,intensity_rgb],axis=1))
#################
sobelx = cv.Sobel(src=src, ddepth=cv.CV_64F, dx=1, dy=0, ksize=1) 
sobely = cv.Sobel(src=src, ddepth=cv.CV_64F, dx=0, dy=1, ksize=1)  

res=np.sqrt(cv.add(sobelx**2,sobely**2))
    
cv.imwrite("Sobel.png",np.concatenate([src,res],axis=1))
############
b,g,r=cv.split(src)

b=255-b
g=255-g
r=255-r
inv_image=cv.merge((b,g,r))

cv.imwrite("Inversion.png",np.concatenate([src,inv_image],axis=1))