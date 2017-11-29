# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 00:22:23 2017

@author: aleba
"""
from estruturas3 import LList

class LStack(LList):
    
     def __init__(self, info, next=None):
         self.info = info
         self.next = next
        
     def insert(self, valor , pos):
         if (pos == LList.length(self)):
             LList.insert_n(self, valor, pos)
         else:
             return 'pos invalida'
    
     def remove(self, pos):
         if (pos == LList.length(self) - 1):
             LList.remove_n(self,pos)
         else:
             return 'pos invalida'
         
     def push(self, valor):
        return self.insert(valor,LList.length(self))
    
     def pop(self):
        return self.remove(LList.length(self) - 1)
        
        
        
l1 = LStack(1,None)
l1.push(LStack(2,None))
l1.push(LStack(3,None))