#!/usr/bin/python3
"""module contains the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry to command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Ends the interpreter"""
        return True

    def do_EOF(self, args):
        """End-Of-File to exit the interpreter"""
        print("")
        return True

    def do_help(self, args):
        """Get help about the command"""
        return super().do_help(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
