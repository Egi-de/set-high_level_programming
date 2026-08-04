#!/usr/bin/python3
"""Module that defines a list subclass with sorted printing."""


class MyList(list):
    """A list that can print a sorted view of itself."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
