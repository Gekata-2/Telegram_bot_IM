print('ImageProc imported correctly')

import cv2 as cv
import numpy as np
from io import BytesIO
from os import remove
def Inversion(ID):
    image=cv.imread('Sources/'+str(ID)+'.jpg')
   
    b,g,r=cv.split(image)

    b=255-b
    g=255-g
    r=255-r
    inv_image=cv.merge((b,g,r))

    cv.imwrite('Processed/Inversion/'+str(ID)+'.jpg',inv_image)
    img=BytesIO(open('Processed/Inversion/'+str(ID)+'.jpg','rb').read())
    remove('Processed/Inversion/'+str(ID)+'.jpg')
    return img
    

def Sobel(ID):
    image=cv.imread('Sources/'+str(ID)+'.jpg')

    sobelx = cv.Sobel(src=image, ddepth=cv.CV_64F, dx=1, dy=0, ksize=1) 
    sobely = cv.Sobel(src=image, ddepth=cv.CV_64F, dx=0, dy=1, ksize=1)  

    res=np.sqrt(cv.add(sobelx**2,sobely**2))
    
    cv.imwrite('Processed/Sobel/'+str(ID)+'.jpg',res)
    img=BytesIO(open('Processed/Sobel/'+str(ID)+'.jpg','rb').read())
    remove('Processed/Sobel/'+str(ID)+'.jpg')
    return img

def GreyScale(ID):
    image=cv.imread('Sources/'+str(ID)+'.jpg')

    b,g,r=cv.split(image)

    intensity=np.zeros((image.shape[0],image.shape[1]),dtype="int32")
    intensity=cv.add(0.299 *r ,0.587 * g , 0.144 * b)

    cv.imwrite('Processed/GreyScale/'+str(ID)+'.jpg',intensity)
    
    img=BytesIO(open('Processed/GreyScale/'+str(ID)+'.jpg','rb').read())
    remove('Processed/GreyScale/'+str(ID)+'.jpg')
    return img

def Glass(ID):
    image=cv.imread('Sources/'+str(ID)+'.jpg')
    #image=cv.imdecode(np.fromstring(input_stream,np.uint8),1)
    dst=np.zeros(image.shape,dtype="int32")
    print(image.shape)

    border_shift=25
    image=cv.copyMakeBorder(image,border_shift,border_shift,border_shift,border_shift,cv.BORDER_REFLECT)
   
    h,w=dst.shape[:2]
   
    for x in range(h):
        for y in range(w):
            shift=np.random.random_integers(-5, 5)
            dst[x,y]=image[border_shift+x+shift,border_shift+y+shift]


    cv.imwrite('Processed/Glass/'+str(ID)+'.jpg',dst)
    
    img=BytesIO(open('Processed/Glass/'+str(ID)+'.jpg','rb').read())
    remove('Processed/Glass/'+str(ID)+'.jpg')
    return img
    


