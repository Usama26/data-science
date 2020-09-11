# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 22:24:17 2020

@author: Usama
"""

firstList = [x for x in range(0,12)]
lastEight = firstList.copy()
lastEight = lastEight[-8:]


four = lastEight[:4]
revFour = four[::-1]

revFour.sort()

newList = [x  for x in revFour if x > 5]
