#!/usr/bin/python
# -*- coding:utf-8 -*-
#===============================================================================
# Description: Talk to things demo
#===============================================================================
"""
Usage
=====

"""

#import sys
#import os
#import optparse
from cfg.config import Config
from ui.console import ConsoleUI
from app.console import ConsoleUI

class TttEntryBase:
    """This is the top entry class for TTT
    """
    
    def __init__(self)
        self.ui = ConsoleUI()

    def start_talk():
        """Start to talk
        """
        self.network.connect()
        self.ui.start()
    
    def stop_talk():
        """Stop the talk
        """
        self.ui.exit()

class TttEntryRouter(TttEntryBase):
    def __init__(self):
        self.app = TttAppRouter()
        self.supper().__init__()

class TttEntryDevice(TttEntryBase):
    def __init__(self):
        self.app = TttAppDevice()
        self.supper().__init__()

class TttEntryHuman(TttEntryBase):
    def __init__(self):
        self.app = TttAppHuman()
        self.supper().__init__()
