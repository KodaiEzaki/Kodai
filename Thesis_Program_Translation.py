# -*- coding: utf-8 -*-
"""
Program for master thesis from Matlab to Python
"""

#前処理

display('対象画像を選択')
filename = uigetfile('*.png')
RGB_image = imread(filename)
[size_x, size_y, ~] = size(RGB_image)

