# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 16:27:40 2015

@author: Greg

This script is intended to log into saltybet IRC and store fighting history
of the fighters. This will then be used later to 
"""
import socket
from saltybot import Fighter
import cPickle as pickle
from read_fighters import read_fighters

"""
Log in information.
"""
HOST="irc.twitch.tv"
PORT=6667
NICK="greggopotato"
IDENT="greggopotato"
REALNAME="greggopotato"
CHANNEL="#saltybet"
PASSWORD="macqlq0v2b86ry7a89yn9h9rwaujor" #From http://twitchapps.com/tmi/


s=socket.socket( )
s.connect((HOST, PORT))
s.send("PASS oauth:%s\r\n" % PASSWORD)
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" % CHANNEL)

filename= 'fighter_data.pkl'

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
    player1_data = data[0:name2_start]
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

Fight_count = 0

with open(filename, 'r') as fp:
    try:    
        Fighter.fighters = pickle.load(fp)
    except(EOFError):
        print "No initial data"

print "Welcome to Greg's Saltybet Tracker"
print " "

while 1: #Keeps the connection
    data=s.recv(1024)
    if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    
    #print data #Displays the chat
    
        
    """
    The following if statement locates announcements on the betting stats.
    Immediately after Bets are locked. is the first Fighters name.
    """
    if data.find('Bets are OPEN for ') != -1:
        
        players = split_data(data)
        if players[0][0:3] != "Team":
            name1 = players[0]
            name2 = players[1]
        
            
            
            print name1 + ' vs ' +name2 + ' BEGIN'
            
            
        elif players[0][0:3] == "Team":
            print "Stupid Team fights\n"
        else:
            print "Error: Code to determine if team not working.\n"
            
    if data.find('Bets are locked. ') != -1:
        name1_start = data.find('Bets are locked. ')+17    
        name1_end =  data.find(" (")
        name2_start = data.find(", ") +2
        name2_end = data.rfind(" (")
        
        
        if name1 == data[name1_start:name1_end] or name2 == data[name2_start:name2_end]:
            is1Found = False
            is2Found = False
            for fighter in Fighter.fighters:
                
                if fighter.name == name1:
                    fighter1 = fighter
                    is1Found = True
                    
                if fighter.name == name2:
                    fighter2 = fighter
                    is2Found = True
                    
            if not is1Found:
                fighter1 = Fighter(data[name1_start:name2_start - 2], name1)
            if not is2Found:
                fighter2 = Fighter(data[name2_start:], name2)
                    
        
    if data.find(' wins! Payouts to') != -1:
        winner= data[data.find('#saltybet :') + 11:data.find(' wins! Payouts to')]
        try:
            AnnounceWinner(fighter1, fighter2, winner)
            Fight_count += 1
        except(NameError):
            print "Program started mid fight. The program will record the next fight.\n"
        
        
        
        
        print "\n Fight number: %s\n" % Fight_count
    
        
      
    
        with open(filename, 'w') as fp:
             pickle.dump(Fighter.fighters, fp)
    
        if Fight_count % 3 ==0:
            read_fighters(filename)
        


               
       
    
    