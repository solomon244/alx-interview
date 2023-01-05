#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    
    if (type(boxes)) is not list:
        return False
    if len(boxes) == 0:
        return False

    for x in range(1, len(boxes) - 1):
        boxes_checked = False
        for y in range(0,len(boxes)):
            if x in boxes[y] and y != x:
                boxes_checked = True
                break
        if boxes_checked is False:
            return False
    return True
