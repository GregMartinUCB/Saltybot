# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 05:47:37 2015

@author: Greg
"""

from saltybot import Fighter
import cPickle as pickle
import socket
from saltyFunctions import *

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


        
while 1: #Keeps the connection
    data=s.recv(1024)
    if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    
    if data.find('Bets are OPEN for ') != -1:
        with open(filename, 'r') as fp:
            try:    
                Fighter.fighters = pickle.load(fp)
            except(EOFError):
                print "No initial data"
                
        players = split_data(data)
        try:
            name1, name2 = FindNames(players)
        
            
            totalFights = 0
            for fighter in Fighter.fighters:
                totalFights += fighter.wins + fighter.loses
                if name1 == fighter.name:
                    print "Player 1:\n"
                    print fighter.name
                    print "Wins: %s" % fighter.wins
                    #print "Loses: %s" % fighter.loses
                    print "Average Bet Ratio: %s" % DisplayBetRatio(fighter)
                    #print "Tier: %s" % fighter.tier
                if name2 == fighter.name:
                    print "Player 2:\n"
                    print fighter.name
                    print "Wins: %s" % fighter.wins
                    #print "Loses: %s" % fighter.loses
                    print "Average Bet Ratio: %s" % DisplayBetRatio(fighter)
                    #print "Tier: %s" % fighter.tier
            totalFights = totalFights/2
            print "The total number of fights is: %s" % totalFights
        except(TypeError):
            print "Current fight is a team match. No data available."