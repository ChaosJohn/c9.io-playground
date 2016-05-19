"""Unpacking Argument Lists"""

def parrot(voltage, state='a stiff', action='voom'):
    """parrot"""
    print "-- This parrot would't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

# D = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
D = {
        "voltage": "four million",
        "state": "bleedin' demised",
        "action": "VOOM",
        }

parrot(**D)
