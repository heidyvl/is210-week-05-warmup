#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function determines what you mean.

    Args:
        wink (int): No default value.
        numwink (int): Default value 2.

    Returns:
        str: What I mean.

    Examples:

        >>>
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
