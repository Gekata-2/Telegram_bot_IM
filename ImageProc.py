print('ImageProc imported correctly')

import cv2 as cv
import numpy as np
from io import BytesIO

def Inversion(image_name):
    image=cv.imread('image.jpg')
    b,g,r=cv.split(image)

    b=255-b
    g=255-g
    r=255-r
    inv_image=cv.merge((b,g,r))
    cv.imwrite('archive/inv_'+image_name,inv_image)
    cv.imwrite('image.jpg',inv_image)
    
    img=BytesIO(open('image.jpg','rb').read())
    return img
    

def Sobel(image_name):
    image=cv.imread('image.jpg')

    cv.imwrite('archive/sob_'+image_name,image)
    
    img=BytesIO(open('image.jpg','rb').read())
    return img

def GreyScale(image_name):
    image=cv.imread('image.jpg')

    cv.imwrite('archive/gs_'+image_name,image)
    
    img=BytesIO(open('image.jpg','rb').read())
    return img

def Glass(image_name):
    image=cv.imread('image.jpg')

    cv.imwrite('archive/glass_'+image_name,image)
    
    img=BytesIO(open('image.jpg','rb').read())
    return img
