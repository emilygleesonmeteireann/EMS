#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 27 November 2019

@author: Romain Roehrig
"""

import numpy as np

class Axis:

    def __init__(self,axisid,data,name=None,units=None,**kwargs):

        self.id = axisid
        self.data = np.array(data,dtype=np.float64)
        self.length, = self.data.shape
        self.units = units
        self.name = name
        for x in kwargs.keys():
            self.__dict__[x] = kwargs[x]

    def info(self,data=False):
        print ("-", "axis id:", self.id)
        print ("-", "name:", self.name)
        print ("-", "units:", self.units)
        print ("-", "length:", self.length)
        for x in self.__dict__.keys():
            if not(x in ['id','name','units','length','data']):
                print ("-", "{0}: {1}", format(x,self.__dict__[x]))
        if data:
            print ("-", "data:", self.data)


    def write(self,filein):

        if not(self.id in filein.dimensions):
            dim = filein.createDimension(self.id, self.length)
            ax = filein.createVariable(self.id,"f8",(self.id,))
            ax[:] = self.data
            ax.standard_name = self.name
            ax.units = self.units
            for x in self.__dict__.keys():
                if not(x in ['id','units','name','data','length']):
                    ax.setncattr(x,self.__dict__[x])
