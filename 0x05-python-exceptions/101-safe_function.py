#!/usr/bin/python3

def safe_function(fct, *args):
    import sys

    try:
        value = fct(*args)
        return value
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
