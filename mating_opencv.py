# -*- coding: utf-8 -*-
"""
by : Grégoire Kubler
"""

#import numpy as np
import matplotlib.pyplot as plt
#from sklearn import preprocessing
#import tensorflow as tf
import cv2
import os
import time


def hardcore_color_inv(mask):
    """
    Parameters:
    mask : cv2 gray img with only black and with px

    Returns:
    mask  --> with inversed black and with colors
    """
    for j in range(mask.shape[1]):
        for i in range(mask.shape[0]):
            flag = False #notifies if given px has already been modified
            if mask[i,j] == 0 :
                mask[i,j] = 255
                flag = True
            if mask[i,j] == 255 and not flag :
                mask[i,j] = 0
                flag = True
    return mask






if __name__ ==  "__main__":


    project_path = "C:/Users/G.R.E.G/Documents/Travail/test_technique_entreprise/enlapse/data/"
#    for img in os.listdir(project_path):
#        print(img)

    project_path = "C:/Users/G.R.E.G/Documents/Travail/test_technique_entreprise/enlapse/data/"
    path_img = project_path + "2021-03-10_080001.jpg"
    path_mask = project_path + "2021-03-10_080001_mask.png"

    img = cv2.imread(path_img)
    mask = cv2.imread(path_mask)
    mask = cv2.cvtColor(mask , cv2.COLOR_RGB2GRAY)

    mask = hardcore_color_inv(mask)


    #_______________inpainting
    start_ns = time.time()
    inpaint_ns = cv2.inpaint( img , mask , 5 , cv2.INPAINT_NS )
    end_ns = time.time()
    elapsed_ns = end_ns - start_ns
    print("elapsed_time for ns = " + str(elapsed_ns))
    start_telea = time.time()
    inpaint_telea = cv2.inpaint( img , mask , 5 , cv2.INPAINT_TELEA )
    end_telea = time.time()
    elapsed_telea = end_telea - start_telea
    print("elapsed_time for telea = " + str(elapsed_telea))


    #__________________displaying results
    display = 1

    if display == 1 :
        cv2.imshow("img" , img)
        cv2.imshow("mask" , mask)
        cv2.imshow("telea" , inpaint_telea)
        cv2.imshow("ns" , inpaint_ns )
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif display == 2 :
        plt.figure(figsize = [20,8])
        plt.subplot(2,2,1);
        plt.imshow(img)
        plt.title("original picture")

        plt.subplot(2,2,2);
        plt.imshow(mask  , cmap = 'gray')
        plt.title("mask")

        plt.subplot(2,2,3);
        plt.imshow(inpaint_ns)
        plt.title("restored_using Navier Stokes algo, duration = " + str(elapsed_ns))

        plt.subplot(2,2,4);
        plt.imshow(inpaint_telea)
        plt.title("restored_unsing Telea algo, duration = " + str(elapsed_ns))
