# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:13:14 2018

@author: Diego
"""

print('\tdecimal\tbinary\thex')

go = -1

while go < 31:

    go = go + 1

    print('\t' + str(go) + '\t' + bin(go) + '\t' + hex(go))

    

#print(bin(0))

#   hex()