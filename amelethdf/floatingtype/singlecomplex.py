#!/usr/bin/env
# -*- coding: utf-8 -*-'''

'''
Created on 17 sept. 2009

@author: Cyril Giraudon
'''

from enthought.traits.api import Complex, String

from amelethdf.floatingtype.simple import Simple

class SingleComplex(Simple):
    floatingType = String("singleComplex")
    value = Complex(0.0 + 0.0j)


        
