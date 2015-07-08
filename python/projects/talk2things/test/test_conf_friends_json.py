#!/usr/bin/python
# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append('../code/')

from cfg.conf_json import JsonFriendsList  as FriendList

class JsonSelfSettingsTestCase(unittest.TestCase):
    """Test friends list in json format
    """
    @classmethod
    def setUpClass(self):
        self.friends_list = FriendList("../code/data/friends.json")

    def setUp(self):
        print ""

    def test_get_friends(self):
        print self.friends_list.get_friends()

    def test_get_first_friend(self):
        friends = self.friends_list.get_friends()
        print self.friends_list.get_friend(friends[0]["name"])


if __name__ == '__main__':
    unittest.main()
