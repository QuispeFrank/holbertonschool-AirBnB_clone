#!/usr/bin/python3
import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "


    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program\n"""
        return True

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            o = BaseModel()
            o.save()
            print(o.id)

    def do_show(self, arg):
        all_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_dict:
            print("** no instance found **")
        else:
            print(all_dict[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        json_to_dic = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) != 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in json_to_dic:
            print('** no instance found **')
        else:
            del json_to_dic[f'{args[0]}.{args[1]}']
            storage.save()

    def do_update(self, arg):
        args = arg.split()
        json_to_dic = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in json_to_dic:
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            o = json_to_dic[f'{args[0]}.{args[1]}']
            setattr(o, args[2], args[3].replace('\"',''))
            o.save()

    def do_all(self, arg):
        args = arg.split()
        lst = []
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif args:
            for i in storage.all().values():
                lst.append(str(i))
            print(lst)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
