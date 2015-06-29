#!/usr/bin/python
# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append('../code/')

from ui.console import ConsoleUI

class ConsoleUITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.consoleUI = ConsoleUI()
        self.color_fg_list = [
            ConsoleUI.FG_BLACK,
            ConsoleUI.FG_RED,
            ConsoleUI.FG_GREEN,
            ConsoleUI.FG_YELLOW,
            ConsoleUI.FG_BLUE,
            ConsoleUI.FG_MAGENTA,
            ConsoleUI.FG_CYAN,
            ConsoleUI.FG_WHITE,
            ConsoleUI.FG_RESET]
        self.color_bg_list = [
            ConsoleUI.BG_BLACK,
            ConsoleUI.BG_RED,
            ConsoleUI.BG_GREEN,
            ConsoleUI.BG_YELLOW,
            ConsoleUI.BG_BLUE,
            ConsoleUI.BG_MAGENTA,
            ConsoleUI.BG_CYAN,
            ConsoleUI.BG_WHITE,
            ConsoleUI.BG_RESET]
        self.my_name = "John"
        self.fd_name = "Sensor"

    def setUp(self):
        print ""
        self.consoleUI.set_speak_color(ConsoleUI.FG_YELLOW, ConsoleUI.BG_BLACK)
        self.consoleUI.set_heard_color(ConsoleUI.FG_GREEN, ConsoleUI.BG_BLACK)
        
    def test_talk(self):
        self.consoleUI.speak(self.my_name, "hello")
        self.consoleUI.heard(self.fd_name, "hi, John, my name is Sensor")
        self.consoleUI.speak(self.my_name, "@John, What could you do?")
        self.consoleUI.heard(self.fd_name, "temperature")
        self.consoleUI.speak(self.my_name, "@John, temperature")
        self.consoleUI.heard(self.fd_name, "27.5.C")

    #@unittest.skip("Don't want to test talkEx!")
    def test_talkEx(self):
        self.consoleUI.speakEx(self.my_name, "hello")
        self.consoleUI.heardEx(self.fd_name, "hi, John, my name is Sensor")
        self.consoleUI.speakEx(self.my_name, "@John, What could you do?")
        self.consoleUI.heardEx(self.fd_name, "temperature")
        self.consoleUI.speakEx(self.my_name, "@John, temperature")
        self.consoleUI.heardEx(self.fd_name, "27.5.C")

    def test_change_color(self):
        for fg in self.color_fg_list:
            for bg in self.color_bg_list:
                if(self.color_fg_list.index(fg) == self.color_bg_list.index(bg)):
                    continue
                self.consoleUI.set_speak_color(fg, bg)
                self.consoleUI.set_heard_color(fg, bg)
                self.consoleUI.speak(self.my_name, "hello")
                self.consoleUI.heard(self.fd_name, "hi, John, my name is Sensor")

if __name__ == '__main__':
    unittest.main()
