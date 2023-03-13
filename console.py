#!/usr/bin/python3

""" This file contains the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class that initiates the command interpreter
    """

    prompt = '(hbnb)'

    def emptyline(self):
        """ What should be done when an empty line + ENTER key is pressed """
        pass

    def do_quit(self, argv):
        """ Used to exit the console """
        return True

    def do_EOF(self, argv):
        """ Another way to exit the console """
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
