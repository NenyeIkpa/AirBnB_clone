#!/usr/bin/env python3
"""
    A command line processor module
"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, line):
        """ creates an instance of the BaseModel class """
        if not line:
            print("** class name missing **")
            return
        if line == 'BaseModel':
            bm = BaseModel()
            print('{}'.format(bm.id))
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
