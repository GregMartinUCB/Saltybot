# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 19:44:03 2015

@author: Greg
"""

class Fighter():
    
    
    fighters = [] #Multiple fighter instances are stored here.
    
    def __init__(self, string, name):
        self.string = string        
        self.bet_ratio=0.0
        self.streak = 0
        self.wlRatio = 0.0
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
    
    def UpdateBetRatio(self, otherPlayer):
        bet1Start = self.string.find(' - $') + 4
        bet2Start = otherPlayer.string.find(' - $') + 4
        
        bet1 = int(self.string[bet1Start:].replace(',',''))
        bet2 = float(otherPlayer.string[bet2Start:].replace(',',''))
        
        ratio = bet1/bet2        
        
        if self.bet_ratio != 0.0:
        
            totalFights = self.loses+self.wins
        
            self.bet_ratio = (self.bet_ratio * totalFights + ratio)/(totalFights + 1)
            
        else:
            self.bet_ratio = ratio
    
    
        
    
        