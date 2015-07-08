"""
This is the module to provide API for handling json.
"""

import json

class JsonSelfSettings:
    """Class for parsing self settings file in json format.
    """

    def __init__(self, file_name):
        self.file_name = file_name

        f = file(file_name, "r");
        self.cfg = json.load(f)
        f.close()
    
    def _save(self):
        f = file(self.file_name, "w")
        json.dump(self.cfg, f)
        f.close()

    def get_name(self):
        return self.cfg["name"]

    def get_type(self):
        return self.cfg["type"]

    def set_name(self, name):
        self.cfg["name"] = name
        self._save()


class JsonFriendsList:
    """Class for parsing friend list file in json format.
    """

    def __init__(self, file_name):
        self.file_name = file_name

        f = file(file_name, "r");
        self.cfg = json.load(f)
        self.friends = self.cfg["friends"]
        f.close()
    
    def _save(self):
        f = file(self.file_name, "w")
        json.dump(self.cfg, f)
        f.close()

    def get_friends(self):
        return [friend for friend in self.friends]

    def get_friend(self, name):
        return filter(lambda f: f['name'] == name, self.friends)

    def set_friend_alias(self, name, alias):
        for i in range(len(self.friends)):
            if(name == friends[i]["name"]):
                friends[i]["alias"] = alias
                self._save()
