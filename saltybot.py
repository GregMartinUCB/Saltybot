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
        self.tier = "Unknown"
        Fighter.fighters.append(self)
        

        
    def find_streak(self):
        streak_begin = self.string.find(' (') + 2
        streak_end = self.string.find(') ')
        
        if self.string[streak_begin]== "-":
            self.streak = int(self.string[streak_begin:streak_end])
        
        else:
            self.streak = int(self.string[streak_begin])
    
    def UpdateBetRatio(self, otherPlayer):
        bet1Start = self.string.find('- $') + 3
        bet2Start = otherPlayer.string.find('- $') + 3
        
        
        bet1 = float(self.string[bet1Start:].replace(',',''))
        bet2 = float(otherPlayer.string[bet2Start:].replace(',',''))
        print 'test ' + self.string[bet1Start:].replace(',','')
        print 'test2 ' + otherPlayer.string[bet2Start:].replace(',','')
        
        if bet1/bet2 >= 1:
            ratio = bet1/bet2        
        else:
            ratio = -(bet2/bet1)
        
                
        
        if self.loses+self.wins != 0:
        
            totalFights = self.loses+self.wins
            print totalFights
            try:
        
                self.bet_ratio = (self.bet_ratio * (totalFights-1) + ratio)/float((totalFights))
            except(ZeroDivisionError):
                print "Error has occured setting new bet ratio. Divide by Zero."
                
                
            
        else:
            self.bet_ratio = ratio
    
    
        
    
        