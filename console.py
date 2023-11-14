#!/usr/bin/env python3
"""
    A command line processor module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        """ called when an empty line entered to prompt. prints a new prompt"""
        pass

    def do_create(self, line):
        """ creates an instance of the BaseModel class """
        if not line:
            print("** class name missing **")
            return
        for name in classnames:
            if line == name:
                bm = classnames[name]()
                print('{}'.format(bm.id))
                return
        print("** class doesn't exist **")

    def do_all(self, line):
        """ prints all instances """
        if line:
            for name in classnames:
                if line == name:
                    all_obj = storage.all()
                    for key, value in all_obj.items():
                        print(value)
                    return
            print("** class doesn't exist **")
            return
        else:
            all_obj = storage.all()
            for key, value in all_obj.items():
                print(value)
            return

    def do_show(self, line):
        """ prints a string representation of a BaseModel instance """
        if line:
            inputs = line.split(" ")
            if len(inputs) == 0:
                print("** class name missing **")
                return
            if len(inputs) == 1:
                if inputs[0] not in classnames:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
                return
            for name in classnames:
                if inputs[0] == name:
                    all_obj = storage.all()
                    for key, value in all_obj.items():
                        if value.id == inputs[1]:
                            print(value)
                            return
                    print("** no instance found **")
                    return
            print("** class doesn't exist **")
            return
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ deletes an instance based on class name """
        if line:
            if " " not in line:
                if line not in classnames:
                    print("** class doesn't exist **")
                    return
            try:
                first, second = line.split(' ')
                if first not in classnames:
                    print("** class doesn't exist **")
                    return
            except ValueError:
                print("** instance id missing **")
                return
            else:
                all_obj = storage.all()
                for key, value in all_obj.items():
                    if second == value.id:
                        del all_obj[key]
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """ updates an instance based on class name """
        if line:
            inputs = line.split(' ')
            if inputs[0] not in classnames:
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
                all_obj = storage.all()
                key_id = inputs[0] + '.' + inputs[1]
                for key in all_obj.keys():
                    if key == key_id:
                        setattr(all_obj[key], inputs[2], inputs[3])
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")


classnames = {
        'BaseModel': BaseModel,
        'User': User,
        "Place": Place,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Review": Review
        }

if __name__ == "__main__":
    # import sys
    # if len(sys.argv) > 1:
    #    HBNBCommand().onecmd(''.join(sys.argv[1:]))
    # else:
    HBNBCommand().cmdloop()
