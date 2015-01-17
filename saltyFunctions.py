# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 01:53:06 2015

@author: Greg
"""
from saltybot import Fighter

def split_data(data):
    """
    
    """
    if data.find('Bets are OPEN for ') != -1:
        name1_start = data.find('Bets are OPEN for ')+ 18
        data = data[name1_start:]
        
        name2_start = data.find(' vs ')+4       
        player1_data = data[0:name2_start - 4]
        player2_data = data[name2_start:data.find("! (")]   
    
    elif data.find('Bets are locked. '):
        name1_start = data.find('Bets are locked. ') + 17
        
        name2_start = data.find(", ") +2
            
        player1_data = data[name1_start:name2_start - 2]
        player2_data = data[name2_start:]
    
    else:
        
        print "Error, string to be split did not meet the requirments."
    
    return [player1_data, player2_data] 
    
def AnnounceWinner(fighter1,fighter2,winner):
    if winner[0:3]!= "Team":
        print " "        
        print "Results:"        
        print "Winner: " + winner
        if winner == fighter1.name:
            fighter1.wins = fighter1.wins + 1
            fighter2.loses = fighter2.loses + 1
            
            
        elif winner== fighter2.name:
            fighter2.wins = fighter2.wins + 1
            fighter1.loses = fighter1.loses + 1
            
        
        else:
            print "Error, Winner's name does not match either fighter's names"   
        
        fighter1.UpdateBetRatio(fighter2)
        fighter2.UpdateBetRatio(fighter1)
    
    print " "
    print "Fighter 1"
    print fighter1.name
    print "Wins: %s" % fighter1.wins
    print "Loses: %s" %fighter1.loses
    print "Betting Ratio: %s" % DisplayBetRatio(fighter1)
    print " "
    print "Fighter 2"
    print fighter2.name
    print "Wins: %s" % fighter2.wins
    print "Loses: %s" %fighter2.loses
    print "Betting Ratio: %s" % DisplayBetRatio(fighter2)

def FindNames(players):
    if players[0].find('Team') == -1:
        name1 = players[0]
    if players[1].find('Team') == -1:
        name2 = players[1]
            
    if players[0].find('Team') != -1:
        print "Player 1 is a team and will not be recorded."
    if players[1].find('Team') != -1:
        print "Player 2 is a team and will not be recorded."
                
    print players[0] + " vs " + players[1] + " Begin\n"
    
    try:
        return name1, name2
    except(UnboundLocalError):
        pass
    
    
def CheckNames(twitchData, name1, name2):
        
    name1_start = twitchData.find('Bets are locked. ')+17    
    if twitchData.find(') - $') != -1:
        
        name1_end =  twitchData.find(" (")
        name2_start = twitchData.find(", ") +2
        name2_end = twitchData.rfind(" (")
    else:
        
        name1_end = twitchData.find('- $')
        name2_start = twitchData.find(", ") +2
        name2_end = twitchData.rfind('- $')
    
    if name1 == twitchData[name1_start:name1_end] or name2 == twitchData[name2_start:name2_end]:
                
        is1Found = False
        is2Found = False
        for fighter in Fighter.fighters:
            
            if fighter.name == name1:
                fighter1 = fighter
                is1Found = True
                print "Player 1 found"
                    
            if fighter.name == name2:
                fighter2 = fighter
                is2Found = True
                print "Player 2 found"
                    
        if not is1Found:
            fighter1 = Fighter(twitchData[name1_start:name2_start - 2], name1)
        if not is2Found:
            fighter2 = Fighter(twitchData[name2_start:], name2)
        
    
    return fighter1, fighter2
    
def FindTier(twitchData):
    if twitchData.find(" Tier)")!= -1:
        tier = twitchData[twitchData.find(" Tier)") - 1]
        return tier
    
    else:
        print "Tier not given\n"
        tier = "Unknown"
        return tier
            
def DisplayBetRatio(fighter):
    
    #if fighter.bet_ratio < 0:
        
        #displayRatio = 1/ (-fighter.bet_ratio + 1)
    #elif fighter.bet_ratio > 0:
    displayRatio = fighter.bet_ratio
    
    #else:
    #    displayRatio = 1
    
    return displayRatio
    