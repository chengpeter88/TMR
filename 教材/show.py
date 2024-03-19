# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:43:06 2021

@author: howar
"""

from urllib.request import urlopen
def showimg(img = 'https://i.imgur.com/cEycfN7.png'):
    from PIL import Image
    try:
        img = Image.open(urlopen(img))
    except :
        img =Image.open(open(img, 'rb'))
    img.show()
    