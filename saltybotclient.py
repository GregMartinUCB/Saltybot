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
PASSWORD="f0t47tdl06qd3q2mtpogu4g0oq6zw7" #From http://twitchapps.com/tmi/


s=socket.socket( )
s.connect((HOST, PORT))
s.send("PASS oauth:%s\r\n" % PASSWORD)
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" % CHANNEL)

filename= 'fighter_data.pkl'

#test_fighter = Fighter('TEST', 'TEST')

#print test_fighter.test_bet_ratio()


Fight_count = 0


if os.path.isfile(filename):

    with open(filename, 'r') as fp:
        try:    
            Fighter.fighters = pickle.load(fp)
        except(EOFError):
            print "No initial data"
        except(AttributeError):
            the_list = pickle.load(fp)
            for i in len(the_list):
                Fighter.fighters[i] = the_list[i]
                
    
else:
    pass


print "Welcome to Greg's Saltybet Tracker"
print " "
midfight = True
while 1: #Keeps the connection
    data=s.recv(1024)
    if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    
    #print data #Displays the chat
    
    
    """
    The following if statement locates announcements on the betting stats.
    Immediately after Bets are locked. is the first Fighters name.
    """
    if data.find('Bets are OPEN for ') != -1 and data.find('Team ') == -1:
        midfight = False
        try:
            players = split_data(data)
            name1, name2 = FindNames(players)
            tier = FindTier(data)
            
            
        except(NameError):
            print "Program started mid fight. The program will record the next fight.\n"
        
            
    
       
            
    if data.find('Bets are locked. ') != -1 and data.find('Team ') == -1:
        
        fighter1String, fighter2String = split_data(data)
        
        print fighter1String
        print fighter2String
        
        try:
            fighter1, fighter2 = CheckNames(data, name1, name2)
            fighter1.string = fighter1String
            fighter2.string = fighter2String
            
            fighter1.tier = tier
            fighter2.tier = tier
                        
        except(NameError):
             print "Program started mid fight. The program will record the next fight.\n"
    
    
        
    if data.find(' wins! Payouts to') != -1:
        winner= data[data.find('#saltybet :') + 11:data.find(' wins! Payouts to')]
        
        if midfight == False:
            try:
                AnnounceWinner(fighter1, fighter2, winner)
            
            
            
                        
            
                Fight_count += 1
                
                print "\nFight number: %s\n" % Fight_count
        
            
          
        
                with open(filename, 'w') as fp:
                    pickle.dump(Fighter.fighters, fp)
            
        #except(NameError):
            #print "Program started mid fight. The program will record the next fight.\n"
        #except(ZeroDivisionError):
            #print "Program started mid fight. The program will record the next fight.\n"
            
            except(ValueError):
                print "Fight not recorded, bet could not be casted into float."
        
        
        
        
        if Fight_count % 25 == 1:
            try:
                read_fighters(filename)
            except(IOError):
                pass
        if Fight_count % 100 == 1:
            num_fighters = str(len(Fighter.fighters))
            with open('backups/backup_'+ num_fighters +'.pkl', 'w') as fp:
                pickle.dump(Fighter.fighters, fp)


               
       
    
    