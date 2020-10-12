# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:24:07 2020

@author: Kodai
"""

#前処理

import numpy
import cv2

RGB_image = cv2.imread('C:/Users/kodai/Desktop/case04.png')
cv2.imshow('image', RGB_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
