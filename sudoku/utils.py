assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'
digits = cols


def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s + t for s in a for t in b]


boxes = cross(rows, cols)
row_units = [cross(row, cols) for row in rows]
column_units = [cross(rows, col) for col in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_units = [[r + c for r, c in zip(rows, cols)], [r + c for r, c in zip(rows, cols[::-1])]]
unit_list = row_units + column_units + square_units + diagonal_units
units = dict((box, [unit for unit in unit_list if box in unit]) for box in boxes)
peers = dict((box, set(sum(units[box], [])) - set([box])) for box in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values
