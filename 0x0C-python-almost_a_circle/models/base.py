#!/usr/bin/python3
"""Module containing the Base Class."""
import json
import os
import csv


class Base:
    """The Base Class."""

    # private class attr containing number of
    # object initialized from this class.
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = f"{cls.__name__}.json"

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        file_name = f"{cls.__name__}.json"

        if not os.path.isfile(file_name):
            return []

        with open(file_name, "r", encoding="utf-8") as f:
            return [cls.create(**ob) for ob in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import time
        import turtle
        from random import randrange

        turtle.Screen().colormode(255)
        for shape in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(0.5)
            t.penup()
            t.pendown()
            t.setpos((t.pos()[0] + shape.x, shape.y - t.pos()[1]))
            t.pensize(8)
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)
        time.sleep(7)
