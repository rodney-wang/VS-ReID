#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:29:00 2018

@author: administrator
"""
import numpy as np
import cv2


def convertColorMask2Ordinary(img):
    
    uniq_scale=np.unique(img)
    
    count=1
    for i in uniq_scale:
        if i>0 and i<256:
            img[img==i]=count
            count+=1
    
    print(np.unique(img))
    return img
    
    
    


fname='/home/administrator/data/DAVIS-Semantics/Annotations_semantics/480p/girl-dog/00000.png'
img=cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
print(np.unique(img))
img=convertColorMask2Ordinary(img)
print(np.unique(img))
    

 
    