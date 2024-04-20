#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """simple command processor"""
    prompt = "(hbnb)"
    name_of_models = ["BaseModel"]

    def do_create(self, class_name):
        """create a new instance of BaseModel, saves it and prints the id"""
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.name_of_models:
            print("** class doesn't exist **")
        else:
            args = class_name.split()
            new_ins = eval(args[0])()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        line_list = line.split()
        if not line_list:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.name_of_models:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        else:
            key = line_list[0] + "." + line_list[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                obj = all_objs[key]
                print(str(obj))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        line_list = line.split()
        if not line_list:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.name_of_models:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        else:
            key = line_list[0] + "." + line_list[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        if line not in HBNBCommand.name_of_models and line != "":
            print("** class doesn't exist **")
            return
        else:
            list_t = []
            all_objs = storage.all()
            for value in all_objs.values():
                list_t.append(str(value))
            print(list_t)

    def do_update(self, line):
        list_output = []
        list_output.extend(line.split()[0:4])
        if list_output[0] == "" or list_output[0] is None:
            print("** class name missing **")
            return
        if list_output[0] not in HBNBCommand.name_of_models:
            print("** class doesn't exist **")
            return
        if list_output[1] == "" or list_output[1] is None:
            print("** instance id missing **")
            return
        if list_output[2] == "" or list_output[2] is None:
            print("** attribute name missing **")
            return
        if list_output[3] == "" or list_output[3] is None:
            print("** value missing **")
            return
        else:
            key = list_output[0] + "." + list_output[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                if type(eval(list_output[3])) != str:
                    setattr(all_objs[key], list_output[2],
                            eval(list_output[3]))
                else:
                    arg_str = list_output[3].replace('"', '')
                    setattr(all_objs[key], list_output[2], arg_str)
            else:
                print("** no instance found **")

    def emptyline(self):
        """Do nothing when press Enter"""
        pass

    def do_quit(self, command):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, command):
        """No more inputs"""
        print()
        return (True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
