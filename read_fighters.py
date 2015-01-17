# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 15:02:06 2015

@author: Greg
"""
def read_fighters(filename):
    import cPickle as pickle
    from saltyFunctions import DisplayBetRatio

    fighter_file = open(filename, 'r')

    fighter_list = pickle.load(fighter_file)
    for fighter in fighter_list:
        if fighter.loses != 0:
            WLR= float(fighter.wins/fighter.loses)
        
        else:
            WLR = "N/A"            
            
        print fighter.name + "\n"
        print "Wins: %s" % fighter.wins
        print "Loses: %s" % fighter.loses
        print "W/L ratio: %s" % WLR
        try:
            print "Latest tier: %s" % fighter.tier
        except(AttributeError):
            print "No Tier recorded."
        try:
            print "Average betting ratio: %s\n" % DisplayBetRatio(fighter)
        except(AttributeError):
            print "No ratio recorded"
    print " "
    print "Number of recorded fighters: %s" % len(fighter_list)

