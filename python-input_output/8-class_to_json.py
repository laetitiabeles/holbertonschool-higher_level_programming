#!/usr/bin/python3
""" Class to JSON Function """


def class_to_json(obj):
    """Return the dictionary representation of simple data structure"""
    return obj.__dict__
