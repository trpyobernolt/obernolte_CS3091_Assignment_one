#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:02:02 2022

@author: troyobernolte

CS3091 Assignment 1 - working with data and github
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import random




image_file = "/Users/troyobernolte/Documents/GitHub/obernolte_CS3091_Assignment_one/DATA/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits"

plt.style.use(astropy_mpl_style)
hdul = fits.open(image_file)
#print(hdul.info())
image_data = fits.getdata(image_file, ext=0)
#print(image_data.shape)

#This code shows a slice of the first layer
def show_slice():
    photo_data = image_data[0][0]
    plt.figure()
    plt.imshow(photo_data, cmap='gray')
    plt.colorbar()








