import numpy as np
import cv2 as cv

width=256
height=256
step=32

img=np.zeros((width,height),np.uint8)

for i in range(0,width,step*2):
    for j in range(0,height,step*2):
        img[i:i+step-1,j:j+step-1]=255

for i in range(0,width,step*2):
    for j in range(0,height,step*2):
        img[i+step:i+2*step-1,j+step:j+2*step-1]=255

cv.imshow('ChessBoard',img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('chess_board.jpg',img)