#!/usr/bin/python
# -*- coding:utf-8 -*-
#===============================================================================

#===============================================================================
"""
Usage
=====

"""

#import sys
#import os
#import optparse
from ui.console import ConsoleUI

def main():
    """This is the enter point of the TTT demo
    """
    myName = "John"
    fdName = "Sensor"

    ui = ConsoleUI()

    ui.speak(myName, "hello")
    ui.heard(fdName, "hi, John, my name is Sensor")
    ui.speak(myName, "@John, What could you do?")
    ui.heard(fdName, "temperature")
    ui.speak(myName, "@John, temperature")
    ui.heard(fdName, "27.5.C")

if __name__ == '__main__':
    main()
