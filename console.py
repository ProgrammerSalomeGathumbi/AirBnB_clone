#!/usr/bin/python3
""" command interpreter module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter prompt """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program\n """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program\n """
        print()
        return True

    def emptyline(self):
        """Enter and empty line dont execute """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
