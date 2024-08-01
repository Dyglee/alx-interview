#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """

    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
