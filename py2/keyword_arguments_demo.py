"""Keyword Arguments""" 

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'): 
    print "-- This parrot wouldn't", action, 
    print "if you put", voltage, "volts through it." 
    print "-- Lovely plumage, the", type 
    print "-- It's", state, "!" 
    print 

parrot(1000) 
parrot(voltage=1000) 
parrot(voltage=1000000, action='VOOOOOM') 
parrot(action='VOOOOM', voltage=10000000) 
parrot('a million', 'bereft of life', 'jump') 
parrot('a thousand', state='pushing up the daisies') 
