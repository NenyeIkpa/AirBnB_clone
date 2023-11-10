#!/usr/bin/env python3
"""
    A command line processor module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ receives and processes command line inputs"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """ end of file """
        return True

    def do_quit(self, line):
        """ exit console """
        return True

    def emptyline(self):
        """ called when an empty line entred to prompt. prints a new prompt"""
        pass

    def do_rejoice(self, line):
        """ shout halleluyah!"""
        print("Hallelulyahhhhh!!!!!")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
