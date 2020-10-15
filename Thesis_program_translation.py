# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:58:39 2020

@author: TANAKA
"""


#前処理

import numpy as np
import cv2
import matplotlib.pyplot as plt

#RGB_image = cv2.imread('C:/Users/kodai/Desktop/case04.png')
RGB_image = cv2.imread('C:/Users/TANAKA/Desktop/case04.png')
#cv2.imshow('image', RGB_image)
#cv2.destroyAllWindows()
#cv2.waitKey(0)

[size_x, size_y, _] = RGB_image.shape

HSV_image = cv2.cvtColor(RGB_image, cv2.COLOR_BGR2HSV)
#cv2.imshow('image', HSV_image)
#cv2.destroyAllWindows()
#cv2.waitKey(0)

S_image = HSV_image[:,:,1]

S_level, im_gray_th_otsu = cv2.threshold(S_image, 0, 255, cv2.THRESH_OTSU)
S_level = int(S_level)

S_histo, _ = np.histogram(np.array(S_image).flatten(), bins=np.arange(256 + 1))
plt.plot(S_histo)
plt.show()

skin_max_integer = 0
skin_max_count = 0
for i in range(S_level-1):
    if S_histo[i+1,] >= skin_max_count:
        skin_max_count = S_histo[i+1,]
        skin_max_integer = i + 1

burn_max_integer = 0
burn_max_count = 0
for j in range(S_level, 255):
    if S_histo[j+1,] >= burn_max_count:
        burn_max_count = S_histo[j+1,]
        burn_max_integer = j + 1
        
"""
skin_seed = imbinarize(S_image, skin_max(1, 1));
skin_seed = imcomplement(skin_seed);
skin_seed = imerode(skin_seed, se);
%figure, imshow(skin_seed)

burn_seed = imbinarize(S_image, burn_max(1, 1));
%burn_seed = imerode(burn_seed, se);
%figure, imshow(burn_seed)

% ここからは GrowCut のための機械的処理
label = zeros(size_x, size_y, 3);

for i = 1: size_x
    for j = 1: size_y
        if burn_seed(i,j) == 1
            label(i,j,1) = 255;
        end

        if skin_seed(i,j) == 1
            label(i,j,3) = 255;
        end
    end
end

figure, imshow(label)
"""