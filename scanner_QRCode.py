#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import zbar
import PIL.Image

#initialize CV2
cap = cv2.VideoCapture(0)
cap.set(3, 800)  # Width
cap.set(4, 800)  # Heigh
cap.set(5, 15)   # FPS
if cap.isOpened() is False:
    raise("IO Error")

#initialize QR_Code
scanner = zbar.ImageScanner()
scanner.parse_config('enable')


while True:
    #input image
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Binarization
    tresh = 100
    max_pixel = 255
    ret, img = cv2.threshold(img, tresh, max_pixel, cv2.THRESH_BINARY)

    #picture change PIL
    pil_img = PIL.Image.fromarray(img)
    width, height = pil.size
    raw = pil_img.tostring()
    image = zbar.Image(width, height, 'Y800', raw)

    #result
    scanner.scan(image)
    for symbol in image:
        print symbol.data

    #finish flag
    k = cv2.waitKey(1)
    if k == 27: #ESC
        break;

cap.release()