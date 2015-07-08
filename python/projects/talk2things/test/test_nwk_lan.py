#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import sys
sys.path.append('../code/')

from nwk.lan.network import LanNetwork as NwkNetwork
from nwk.lan.command import LanCommand as NwkCommand

class NwkLanTestCase(unittest.TestCase)
    """Test LAN Network server/client
    """

    @classmethod
    def setUpClass(self):
        self.network = NwkNetwork()
        self.command = NwkCommand()
        self.host
        self.server.start()

    def setUp(self):
        print ""

    def test_get_friends(self):
        self.command(host, command)

if __name__ == '__main__':
    unittest.main()

