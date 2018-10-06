#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:42:20 2018

@author: yin
"""
class cityGrid:
    def __init__(self,inputfile):
        self.inputfile = inputfile
    
    def citySpecificaiton(self):
        self.InputFile = open(self.inputfile,"r")
        specification = (self.InputFile.readline())
        self.cityLength = int(specification.split()[0])
        self.cityWidth = int(specification.split()[1])
        self.buildWidth = int(specification.split()[2])
        self.velocity = int(specification.split()[3])
        self.hideout = (int(specification.split()[4]),int(specification.split()[5]))
        if self.cityLength < 1 or self.cityLength >= 20:
            raise Exception("cityLength, dx, is out of range")
        if self.cityWidth < 1 or self.cityWidth >= 20:
            raise Exception("cityWidth, dy, is out of range")
        
        
    def cityMap(self):
        spec = self.citySpecificaiton()
        city = []
        for i in range(self.cityWidth):
            temp = self.InputFile.readline().split()
            temp = [int(i) for i in temp]
            #temp = map(int,temp) 
            city.append(temp)
            #city.append(list(temp)) 
        print (city)
        
test = cityGrid("Input1.txt")
test.cityMap()