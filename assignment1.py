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
        
    def hideoutLocHeight(self,citymap,lx,ly):
        return citymap[lx-1][ly-1]
        
    def jumpList(self,dx,dy):
        jump_List = [[0 for i in range (dx)] for j in range (dy)]
        for i in range (dy):
            for j in range (dx):
                jump_List[i][j] = str(i)+str(j)
        return jump_List

    def isPossibleToJump(self,velocity,w,jumpFrom,jumpTo):
        pass
        #jumpFrom is (xi,yi)
        #jumpTo is (xf,yf)
        # i = intial, f = final

    def empty_s(self,dx,dy):
        return np.full((dy,dx),1)
    
    def run(self):
        dx,dy,w,v,lx,ly = self.citySpecificaiton()
        result = self.empty_s(dx,dy)
        j_List = self.jumpList(dx,dy)
        cityMap = self.cityMap(dy)
        h_loc = self.hideoutLocHeight(cityMap,lx,ly)
        result[lx-1][ly-1] = 0
        print (j_List)
        print (result)
                 
        
    
test = cityGrid("Input1.txt")
test.run()