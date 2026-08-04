#!/usr/bin/python3
"""Module that defines LockedClass."""


class LockedClass:
    """Prevents dynamically creating new instance attributes,
    except for first_name.
    """

    def __setattr__(self, name, value):
        """Only allow setting the 'first_name' attribute."""
        if name != "first_name":
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    type(self).__name__, name))
        super().__setattr__(name, value)
