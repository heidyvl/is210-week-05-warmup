#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module sets a default value."""


def defaults(my_optional=True, my_required=None):
    """This function sets a default value in our function definition.

    Args:
        my_optional (bool): which has a default value of True
        my_required (bool):

    Returns:
        bool:  a logical comparison

    Examples:

       >>> defaults(True)
        True
       >>> defaults(True, False)
        False
       >>> defaults(False, False)
        True    """

    return my_optional is my_required
print defaults(True, False)
