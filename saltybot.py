# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 19:44:03 2015

@author: Greg
"""



class Fighter():
    
    
    fighters = [] #Multiple fighter instances are stored here.
    
    def __init__(self, string, name):
        self.string = string        
        self.bet_ratio=[]
        self.opponent = []
        self.avg_bet_ratio = 0.0
        self.streak = 0
        self.wlRatio = 0.0
        self.wins = []
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
       
        
        
        ratio1 = bet1/(bet2+bet1)
        
        
       
        self.bet_ratio.append(ratio1)
        if len(self.wins) != 0:
            avg = sum(self.bet_ratio)/float(len(self.wins))
        else:
            avg = self.bet_ratio
        self.avg_bet_ratio = avg
    
    
    def test_bet_ratio(self):
        
        
        
        fighter1 = Fighter('- $100,000', "John")
        fighter2 = Fighter('- $100,000', "Jill")
        fighter2.wins.append(1)
        fighter1.wins.append(0)
        fighter1.UpdateBetRatio(fighter2)
        fighter2.UpdateBetRatio(fighter1)
        
        fighter2.string ='- $100,000'
        fighter1.string ='- $500,000'
        fighter2.wins.append(1)
        fighter1.wins.append(0)
        fighter1.UpdateBetRatio(fighter2)
        fighter2.UpdateBetRatio(fighter1)
        
        fighter2.string ='- $100,000'
        fighter1.string ='- $500,000'
        fighter2.wins.append(1)
        fighter1.wins.append(0)
        fighter1.UpdateBetRatio(fighter2)
        fighter2.UpdateBetRatio(fighter1)
        
      
        
        
        print fighter1.bet_ratio
        print fighter2.bet_ratio
        print fighter1.avg_bet_ratio
        print fighter2.avg_bet_ratio
        
        fighter1.DisplayBetRatio()
        fighter2.DisplayBetRatio()
        if (fighter1.avg_bet_ratio/(1-fighter1.avg_bet_ratio)) == 2.6:
            return True
        else:
            return False
            
    def DisplayBetRatio(self):
    
        displayRatio = self.avg_bet_ratio/(1-self.avg_bet_ratio)
        
        print displayRatio
