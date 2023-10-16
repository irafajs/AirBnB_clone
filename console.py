#!/usr/bin/python3
"""
Shebang to make PY script
"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class to implement command line interpretor"""
    prompt = "(hbnb) "

    classes = {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
            }

    def do_quit(self, arg):
        """exit the command line program"""
        return True

    def do_EOF(self, arg):
        """exit at the end of line command"""
        print()
        return True

    def do_help(self, arg):
        """method to overide help command"""
        if arg == "quit":
            print("Quit command: Exits the program")
            print()
        else:
            super().do_help(arg)

    def emptyline(self):
        """override emptyline"""
        pass

    def do_create(self, arg):
        """create new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            if class_name in HBNBCommand.classes:
                new_instance = HBNBCommand.classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(f"Error: {e}")

    def do_show(self, arg):
        """prints reprentation of an instance class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """delete instance based on classname id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """print representation of instances"""
        args = arg.split()
        all_instances = []
        if args:
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if key.split('.')[0] == class_name:
                    all_instances.append(str(value))
        else:
            for key, value in storage.all().items():
                all_instances.append(str(value))
        print(all_instances)

    def do_update(self, arg):
        """update instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3].strip('""')
        setattr(storage.all()[key], attribute_name, attribute_value)
        storage.all()[key].save()

    def parse_and_call_all(self, arg):
        """call all method when input is in format classname.all()"""
        parts = arg.strip('()').split('.')
        class_name, method = parts
        if method == 'count':
            self.do_count(class_name)
        else:
            self.do_all(class_name)

    def default(self, line):
        """default when the inpupt is not know this method is called"""
        if line.endswith('()'):
            self.parse_and_call_all(line)
        else:
            super().default(line)

    def do_count(self, arg):
        """return number of instances of a defined class"""
        parts = arg.strip('()').split('.')
        class_name, method = parts
        if class_name in HBNBCommand.classes:
            class_instance_count = 0
            for key in storage.all().values():
                if isinstance(key, HBNBCommand.classes[class_name]):
                    class_instance_count += 1
            print(class_instance_count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
