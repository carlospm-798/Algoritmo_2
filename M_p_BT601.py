#Escala de grises
#Paredes Márquez Carlos
#17 / 08 / 2021
'''Aplica todos los diferentes métodos de conversión a escala de grises que se explican en el video'''
import cv2
import numpy as np

im= cv2.imread('Jessy.png')

R = im[:,:,2]
G = im[:,:,1]
B = im[:,:,0]

ig= R*0.299 + G*0.587 + B*0.114

ig= ig.astype(np.uint8)

cv2.imshow('image0', im)
cv2.imshow('image', ig) #R G B, ig
cv2.waitKey(0)