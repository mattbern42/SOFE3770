#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:42:20 2018

@author: yin
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as plt3d

class cityGrid:
    def __init__(self,inputfile):
        self.inputfile = inputfile
    
    def citySpecificaiton(self):
        self.InputFile = open(self.inputfile,"r")
        specification = (self.InputFile.readline()).split()
        specification = [int(i) for i in specification]
        return specification
        
    def cityMap(self,cityWidth):
        city = []
        for i in range(cityWidth):
            temp = self.InputFile.readline().split()
            temp = [int(i) for i in temp]
            city.append(temp)
        return city
        
    def solution(self):
        pass

    def run(self):
        dx,dy,w,v,lx,ly = self.citySpecificaiton()
        a = self.cityMap(dy)
        print (a)
        
        
        
test = cityGrid("Input1.txt")
test.run()