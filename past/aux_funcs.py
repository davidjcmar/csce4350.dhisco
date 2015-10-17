#!/usr/bin/python -B
from more_itertools import unique_everseen


def set_filename(filepath, ext):
    start = len(filepath) - 1

    for i in xrange(len(filepath) - 1, -1, -1):
        if filepath[i] == '/':
            start += 1
            break
        start -= 1

    filename = str(filepath[start: -4]) + str(ext)
    return filename


def remove_dups (list_raw):
    return list(unique_everseen(list_raw))