import cv2
import numpy as np

img1 = cv2.imread('img/current_board.png')
img2 = cv2.imread('img/current_probability.png')
cv2.namedWindow('Wizard-Chess')
cv2.namedWindow('Probability')
cv2.namedWindow('Post-Game-Analysis')

while True:

    try:
        cv2.imshow('Wizard-Chess', img1)
        cv2.imshow('Probability', img2)

        k = cv2.waitKey(1000)
        if k == ord('u'):
            img1 = cv2.imread('img/current_board.png')
            img2 = cv2.imread('img/current_probability.png')
        
        elif k == ord('e'):
            break
            
            
    except:
        continue

img3 = cv2.imread('img/post_analysis.png')
cv2.imshow('Post-Game-Analysis', img3)
cv2.waitKey(100000)
cv2.destroyAllWindows()