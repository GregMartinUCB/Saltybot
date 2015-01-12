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
from saltyFunctions import *
import os

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


        

Fight_count = 0


if os.path.isfile(filename):

    with open(filename, 'r') as fp:
        try:    
            Fighter.fighters = pickle.load(fp)
        except(EOFError):
            print "No initial data"
    
else:
    pass


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
        try:
            players = split_data(data)
            name1, name2 = FindNames(players)
            tier = FindTier(data)
            
            
        except(NameError):
            print "Program started mid fight. The program will record the next fight.\n"
            
       
            
    if data.find('Bets are locked. ') != -1:
        
        
        try:
            fighter1, fighter2 = CheckNames(data, name1, name2)
            
            fighter1.tier = tier
            fighter2.tier = tier
                        
        except(NameError):
             print "Program started mid fight. The program will record the next fight.\n"
        
    if data.find(' wins! Payouts to') != -1:
        winner= data[data.find('#saltybet :') + 11:data.find(' wins! Payouts to')]
        try:
            AnnounceWinner(fighter1, fighter2, winner)
            
            fighter1.UpdateBetRatio(fighter2)
            fighter2.UpdateBetRatio(fighter1)
            
            
            Fight_count += 1
            
        except(NameError):
            print "Program started mid fight. The program will record the next fight.\n"
        
        
        
        
        print "\n Fight number: %s\n" % Fight_count
    
        
      
    
        with open(filename, 'w') as fp:
             pickle.dump(Fighter.fighters, fp)
    
        if Fight_count % 3 ==0:
           read_fighters(filename)
        


               
       
    
    