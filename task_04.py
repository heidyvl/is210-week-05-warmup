#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module knows if we have enough litter boxes."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function determines if we have enough litter boxes.

    Args:
        kittens (int): the number of kittens
        litterboxes (int): number of available litterboxes
        catfood (bool): whether or not any catfood exists

    Returns:
        bool:  ensures we have at least one litterbox for each kitten
        and that we have some catfood.

    Examples:

       >>> too_many_kittens(12, 12, False)
        True

       >>> too_many_kittens(13, 12, True)
        True

       >>> too_many_kittens(12, 13, True)
        False >>>
    """

    return not (litterboxes >= kittens and catfood)

print too_many_kittens(12, 12, False)
