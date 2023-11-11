#!/usr/bin/env python3
"""
    A command line processor module
"""
import cmd
import models


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
            bm = models.base_model.BaseModel()
            print('{}'.format(bm.id))
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ prints all instances """
        if line:
            if line != "BaseModel":
                print("** class doesn't exist **")
                return
        all_obj = models.storage.all()
        for key, value in all_obj.items():
            print(value)

    def do_show(self, line):
        """ prints a string representation of a BaseModel instance """
        if line:
            if " " not in line:
                if line != 'BaseModel':
                    print("** class doesn't exist **")
                    return
            try:
                first, second = line.split(' ')
                if first != 'BaseModel':
                    print("** class doesn't exist **")
                    return
            except ValueError:
                print("** instance id missing **")
                return
            else:
                all_obj = models.storage.all()
                for key, value in all_obj.items():
                    if value.id == second:
                        print(value)
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ deletes an instance based on class name """
        if line:
            if " " not in line:
                if line != 'BaseModel':
                    print("** class doesn't exist **")
                    return
            try:
                first, second = line.split(' ')
                if first != 'BaseModel':
                    print("** class doesn't exist **")
                    return
            except ValueError:
                print("** instance id missing **")
                return
            else:
                all_obj = models.storage.all()
                for key, value in all_obj.items():
                    if second == value.id:
                        del all_obj[key]
                        models.storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """ updates an instance based on class name """
        if line:
            if " " not in line:
                if line != 'BaseModel':
                    print("** class doesn't exist **")
                    return
            inputs = line.split(' ')
            if inputs[0] != 'BaseModel':
                print("** class doesn't exist **")
                return
            if len(inputs) == 1:
                print("** instance id missing **")
                return
            elif len(inputs) == 2:
                print("** attribute name missing **")
                return
            elif len(inputs) == 3:
                print("** value missing **")
                return
            else:
                all_obj = models.storage.all()
                key = inputs[0] + '.' + inputs[1]
                setattr(all_obj[key], inputs[2], inputs[3])
                models.storage.save()
                return
                print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(''.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
