#!/usr/bin/python3
"""Defines a locked class."""

class lockedclass:
    """
    prevent the user form instantiating new lockedclass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
