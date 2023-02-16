#!/usr/bin/python3
"""
 0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise
    """
    m = len(matrix)
    copy_matrix = [row[:] for row in matrix]
    for i in range(0, n):
        for j in range(m - 1, -1, -1):
            matrix[j][m - 1 - i] = copy_matrix[i][j]
