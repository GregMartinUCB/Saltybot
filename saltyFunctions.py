# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 01:53:06 2015

@author: Greg
"""
from saltybot import Fighter

def split_data(data):
    """
    This function takes in the raw string that appears after Waifu4u anounces
    that Bets are OPEN, then splits the text into two strings. One for each
    player.
    
    Returns a list containing the string for each player. 
    """
    name1_start = data.find('Bets are OPEN for ')+ 18
    data = data[name1_start:]
        
    name2_start = data.find(' vs ')+4       
    player1_data = data[0:name2_start - 4]
    player2_data = data[name2_start:data.find("! (")]        
    
        
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
    
    print " "
    print "Fighter 1"
    print fighter1.name
    print fighter1.wins
    print fighter1.loses
    print " "
    print "Fighter 2"
    print fighter2.name
    print fighter2.wins
    print fighter2.loses

def FindNames(players):
    if players[0].find('Team') == -1:
        name1 = players[0]
    if players[1].find('Team') == -1:
        name2 = players[1]
            
    if players[0].find('Team') != -1:
        print "Player 1 is a team and will not be recorded."
    if players[1].find('Team') != -1:
        print "Player 2 is a team and will not be recorded."
                
    print players[0] + " vs " + players[1] + " Begin"
    
    return name1, name2
    
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