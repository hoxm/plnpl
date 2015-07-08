"""
Define the fore_end Console type UI.
"""

class ConsoleUI:
    """ The console similator UI class.
    """
    #foreground
    FG_BLACK = 30
    FG_RED = 31
    FG_GREEN = 32
    FG_YELLOW = 33
    FG_BLUE = 34
    FG_MAGENTA = 35
    FG_CYAN = 36
    FG_WHITE = 37
    FG_RESET = 39

    #background
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_WHITE = 47
    BG_RESET = 49

    def __init__(self, width=80):
        """initialize the console UI
        """
        self.ui_type = "console"
        self.ui_width = width
        self.speak_fg = ConsoleUI.FG_YELLOW
        self.speak_bg = ConsoleUI.BG_BLACK
        self.heard_fg = ConsoleUI.FG_GREEN
        self.heard_bg = ConsoleUI.BG_BLACK

    def _speak(self, line):
        """show console ui speak contents
        """
        print "\033[%dm\033[%dm" %(self.speak_fg, self.speak_bg),
        print "%s" % line.ljust(self.ui_width),
        print "\033[0m"

    def _heard(self, line):
        """show console ui heard contents
        """
        print "\033[%dm\033[%dm" %(self.heard_fg, self.heard_bg),
        print "%s" % line.rjust(self.ui_width),
        print "\033[0m"

    def set_speak_color(self, fg, bg):
        """set the speak content foreground/background color
        """
        self.speak_fg = fg
        self.speak_bg = bg

    def set_heard_color(self, fg, bg):
        """set the heard content foreground/background color
        """
        self.heard_fg = fg
        self.heard_bg = bg
   
    def speak(self, name, content):
        """show console ui speak contents simply
        """
        line = '[' + name + '] ' + content
        self._speak(line)

    def heard(self, name, content):
        """show console ui heard contents simply
        """
        line = content + ' [' + name + ']'
        self._heard(line)

    def speakEx(self, name, content):
        """show console ui speak contents beautifully
        """
        line = '[' + name + ']' + '-'*(len(content) + 4)
        self._speak(line)
        line = ' '*(len(name) + 2) + '| ' + content + ' |'
        self._speak(line)
        line = ' '*(len(name) + 2) + '-'*(len(content) + 4)
        self._speak(line)

    def heardEx(self, name, content):
        """show console ui heard contents beautifully
        """
        line = '-'*(len(content) + 4) + '[' + name + ']'
        self._heard(line)
        line = '| ' + content + ' |' + ' '*(len(name) + 2)
        self._heard(line)
        line = '-'*(len(content) + 4) + ' '*(len(name) + 2)
        self._heard(line)
