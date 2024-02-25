#!/usr/bin/python3
""" Defines a base model class """

import json
import os
import turtle


class Base:
    """ Represent the base model for this project
    Attributes:
        __nb_objects (int): number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base
        Args:
            id (int): identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string rep of a list dict
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a file
        Args:
            list_objs (list): a list of objects
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            objects = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(objects)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ Return the JSON string rep of a list dict
        Args:
            json_string (str): a JSON string
        Returns:
            JSON string representation of list_dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a list of instances
        Args:
            dictionary (dict): key/value pairs of attributes
        Returns:
            instance of the created object
        """
        if cls.__name__ == "Rectangle":
            fake_instance = cls(10, 10)
        elif cls.__name__ == "Square":
            fake_instance = cls(10)

        fake_instance.update(**dictionary)

        return fake_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
            instance_list = cls.from_json_string(json_string)
            return [cls.create(**dictionnary) for dictionnary in instance_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        draw = turtle.Turtle()
        draw.pensize(2)
        draw.shape("turtle")
        draw.shapesize(3, 3, 3)
        draw.width(3)
        draw.pencolor("#90ee90")
        draw.screen.bgcolor("#9ad7db")
        draw.screen.title("Drawing with a turtle because why not")

        draw.penup()
        draw.goto(-100, 200)

        for rectangles in list_rectangles:
            draw.fillcolor("#91a3b0")
            Base.setup_draw(draw, rectangles)
            for _ in range(2):
                draw.forward(rectangles.width)
                draw.left(90)
                draw.forward(rectangles.height)
                draw.left(90)
            draw.end_fill()
            draw.penup()

        for squares in list_squares:
            draw.fillcolor("#fef580")
            Base.setup_draw(draw, squares)
            for _ in range(4):
                draw.backward(squares.width)
                draw.right(90)
            draw.end_fill()
            draw.penup()

        draw.color("#90ee90")
        draw.goto(-200, 100)
        draw.screen.exitonclick()

    @staticmethod
    def setup_draw(instance, obj):
        instance.goto(instance.xcor(), instance.ycor() - (obj.height + 10))
        instance.penup()
        instance.pendown()
        instance.begin_fill()
