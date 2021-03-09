#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 04:14:08 2021

@author: mluisadiez
"""
class Cola:

    def __init__(self,tipo):
       self.__cola=list()
       self.tipo=tipo
       
    def estaVacia(self):
        return not self.__cola
    
    def primero(self):
        try:
            return self.__cola[0]
        except:
            return None
       
            
    def encolar(self,elemento):
        if type(elemento)==self.tipo:
                self.__cola.append(elemento)
                return
        else: 
                raise TypeError
        
    def desencolar(self):
        try:
            self.__cola.pop(0)
            return self.__cola[0]
        except:
            None
            
    def __str__(self):
        return str(self.__cola)
    
    
cola=Cola(int)
cola.encolar(3)
cola.encolar(7)
print(cola.primero())
print(cola)
    