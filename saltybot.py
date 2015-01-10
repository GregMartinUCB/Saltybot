# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 19:44:03 2015

@author: Greg
"""

class Fighter():
    
    
    fighters = [] #Multiple fighter instances are stored here.
    
    def __init__(self, string, name):
        self.string = string        
        self.avg_value=0
        self.streak = 0
        self.wlRatio = 0
        self.wins = 0
        self.loses= 0
        self.name = name
        Fighter.fighters.append(self)
        

        
    def find_streak(self):
        streak_begin = self.string.find(' (') + 2
        streak_end = self.string.find(') ')
        
        if self.string[streak_begin]== "-":
            self.streak = int(self.string[streak_begin:streak_end])
        
        else:
            self.streak = int(self.string[streak_begin])
    
    
        
    
        