from __future__ import print_function, division

"""This module provides one funcuon, structshape(), which takes
an object of any type and returns a string that summarizes the
"shape" of the data structure; that is, the type, sizw and
composition.
"""
def structshape(ds):
    """Returns a string that describes the shape if a data structure.

    ds: any Python object

    Returns:string
    """
    typename = type(ds).__name__

    #

