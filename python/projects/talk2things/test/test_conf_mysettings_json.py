#!/usr/bin/python
# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append('../code/')

from cfg.conf_json import JsonSelfSettings as SelfSettings

class JsonSelfSettingsTestCase(unittest.TestCase):
    """Test self settings in json format
    """
    @classmethod
    def setUpClass(self):
        self.settings = SelfSettings("../code/data/myself.json")

    def setUp(self):
        print ""

    def test_get_settings(self):
        print "Myself Name: " + self.settings.get_name()
        print "Myself Type: " + self.settings.get_type()

    def test_set_name(self):
        name_old = self.settings.get_name()
        self.settings.set_name("John")
        self.settings.set_name("")

if __name__ == '__main__':
    unittest.main()
