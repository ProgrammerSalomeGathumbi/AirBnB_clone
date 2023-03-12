#!/usr/bin/python3
""" command interpreter module """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models import city
from models import state
from models import amenity
from models import place
from models import review
from models import user

Class_Dict = {"BaseModel": BaseModel,
              "User": user,
              "Place": place,
              "State": state,
              "Amenity": amenity,
              "Review": review,
              "City": city}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter prompt """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": user,
               "Place": place,
               "State": state,
               "Amenity": amenity,
               "Review": review,
               "City": city}

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

    def do_create(self, args):
        """
        Create new instance of BaseModel
        """
        if not args:
            print('** class name missing **')
            return
        elif args in Class_Dict:
            for key, value in Class_Dict.items():
                if key == args:
                    new_instance = Class_Dict[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Print str repr of an instance
        bases on class name and id
        """
        new_instance = args.partition(' ')
        class_name = new_instance[0]
        class_id = new_instance[2]

        if not args:
            print('** class name missing **')
            return
        if class_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not class_id:
            print('** instance id missing **')
            return
        new_key = class_name + '.' + class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except BaseException:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance basesd on
        class name and id
        """
        new_args = ""
        class_name = ""
        class_id = ""
        try:
            new_args = arg.split(" ")
            class_name = new_args[0]
            class_id = new_args[1]
        except BaseException:
            pass
        if not class_name:
            print('** class name missing **')
        elif class_name not in Class_Dict:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            new_key = class_name + '.' + class_id
            try:
                del(storage._FileStorage__objects[new_key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all instances based on class
        """
        new_list = []
        if arg:
            if arg not in Class_Dict:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == arg:
                    new_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                new_list.append(str(value))
        print(new_list)

    def do_update(self, args):
        """
        updates object
        """
        new_object = ""
        class_name = ""
        class_id = ""
        at_name = ""
        at_val = ""
        objects = ""
        try:
            new_object = args.split(" ")
            class_name = new_object[0]
            class_id = new_object[1]
            at_name = new_object[2]
            at_val = new_object[3]
            objects = storage._FileStorage__objects.items()
        except (IndexError, NameError):
            pass
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        if not at_name:
            print("** attribute name missing **")
            return
        if not at_val:
            print("** value missing **")
            return

        new_key = class_name + "." + class_id
        no_touchy = ["id", "created_at", "updated_at"]
        for key, value in storage._FileStorage__objects.items():
            if new_key not in no_touchy:
                if new_key == key:
                    setattr(value, at_name, at_val)
                    new = value
                    new.save()
        print("** no instance found **")
        if new_key not in storage._FileStorage__objects.keys():
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
