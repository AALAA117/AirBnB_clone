#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """simple command processor"""
    prompt = "(hbnb)"

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
