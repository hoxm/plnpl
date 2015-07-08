"""
This demo is to test 5 roles in the same LAN network
Two human entries, two device entries, one router.
"""

from ttt.ui import ConsoleUI
from ttt import TttEntryHuman, TttEntryRouter, TttEntryDevice
from ttt.nwk import NwkLAN

def demo_roles_console_ui(port_start):
    port = port_start
    roles = {
        'human1': {'type':TttEntryHuman,  'ui':ConsoleUI.name}
        'human2': {'type':TttEntryHuman,  'ui':ConsoleUI.name}
        'router': {'type':TttEntryRouter, 'ui':None}
        'Device1':{'type':TttEntryDevice, 'ui':None}
        'Device2':{'type':TttEntryDevice, 'ui':None}
    }

    for i in roles:
        nwk = NwkLAN(port)
        roles[i]['entry'] = roles[i]['type'](i, nwk, roles[i]['ui'])  
        port += 1

        roles[i]['entry'].start_talk()

if __name__ == '__main__':
    demo_roles_console_ui(5800)
