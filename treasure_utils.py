# Melissa Qian
# 261120131
# Assignment 2: Question 2

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(str_map, n, w, h):
    """ (str, int, int, int) -> str
    Return nth row in string map.
    
    >>> get_nth_row_from_map('^..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('ABCDEFGH', 2, 2, 4)
    'EF'
    >>> get_nth_row_from_map('---...AB', 4, 2, 4)
    ''
    """
    str_map = str(str_map)
    n = int(n)
    w = int(w)
    h = int(h)
    
    if n > h-1:
        return ''
    else:
        start = w*n
        end = start+w
        nth_row = slice(start, end)
        return str_map[nth_row]

def print_treasure_map(str_map, w, h):
    """ (str, int, int) -> Nonetype
    Prints out the treasure map with each row on its own line
    
    >>> print_treasure_map('<..vvv..^', 3, 3)
    <..
    vvv
    ..^
    >>> print_treasure_map('</3</3</3', 3, 3)
    </3
    </3
    </3
    >>> print_treasure_map('<><>1<><>2<><>3', 5, 3)
    <><>1
    <><>2
    <><>3
    """
    str_map = str(str_map)
    w = int(w)
    h = int(h)
    for n in range(h):
        treasure_map = get_nth_row_from_map(str_map, n, w, h)
        print(treasure_map)
        
def change_char_in_map(str_map, row, column, c, w, h):
    """ (str, int, int, str, int, int) -> str
    Returns a string with changed character.
    
    >>> change_char_in_map('.........', 1, 1, 'X', 3, 3)
    '....X....'
    >>> change_char_in_map('I***Y', 2, 0, 'L', 1, 5)
    'I*L*Y'
    >>> change_char_in_map('bruhwhat', 3, 0, 'X', 4, 2)
    'bruhwhat'
    """
    str_map = str(str_map)
    row = int(row)
    column = int(column)
    c = str(c)
    w = int(w)
    h = int(h)
    if row > h-1 or column > w-1:
        return str_map
    else: 
        c_position = w*row + column
        start = str_map[:c_position]
        end = str_map[c_position+1:]
        new_map = start + c + end
        return new_map

def get_proportion_travelled(str_map):
    """ (str) -> float
    Returns as a float the percentage (between 0 and 1) of the map
    that was travelled
    
    >>> get_proportion_travelled('.X..X.XX.')
    0.44
    >>> get_proportion_travelled('.X.')
    0.33
    >>> get_proportion_travelled('❀X❀X❀X❀X❀X❀')
    0.45
    """
    str_map = str(str_map)
    number_breadcrumb = str_map.count(BREADCRUMB_SYMBOL)
    total_length = len(str_map)
    proportion_travelled = float(number_breadcrumb/total_length)
    return round(proportion_travelled,2)

def get_nth_map_from_3D_map(str_map_3D, n, w, h, d):
    """ (str, int, int, int, int) -> str
    Returns the n’th map of the 3D treasure map
    
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map('ABCDEFGH', 0, 2, 2, 2)
    'ABCD'
    >>> get_nth_map_from_3D_map('^v^v^v^v^v^v^v^', 2, 3, 3, 2)
    ''
    """
    str_map_3D = str(str_map_3D)
    n = int(n)
    w = int(w)
    h = int(h)
    d = int(d)
    
    if n > d-1 or n > h-1 or n > w-1:
        return ''
    else:
        start = (h*n)**d
        end = start+w*h
        nth_map = slice(start, end)
        return str_map_3D[nth_map]

#How to add the space
def print_3D_treasure_map(str_map_3D, w, h, d):
    """ (str, int, int, int) -> NoneType
    Prints out the treasure map with each row on its own line, and each
    map separated by a blank line
    
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)
    .X.
    XXX
    .X.
    
    .v.
    vXv
    .v.
    >>> print_3D_treasure_map('ABCDEFGH', 2, 2, 2)
    AB
    CD
    
    EF
    GH
    >>> print_3D_treasure_map('^v^v^v^v^v^v^v^v^v', 3, 3, 2)
    ^v^
    v^v
    ^v^

    v^v
    ^v^
    v^v
    """
    str_map_3D = str(str_map_3D)
    w = int(w)
    h = int(h)
    d = int(d)
    
    i = 0
    for i in range(d):
        map_3D = get_nth_map_from_3D_map(str_map_3D, i, w, h, d)
        print_treasure_map(map_3D, w, h)
        if i != d-1:
            print(end="\n")

def change_char_in_3D_map(str_map_3D, row, column, depth, c, w, h, d):
    """ (str, int, int, int, str, int, int, int) -> str
    Returns a copy of the given 3D treasure
    map string but with the character at the given row, column and depth index
    replaced by c.
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 2, '#', 3, 3, 2)
    '.X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('ABCDEFGH', 0, 1, 0, '#', 2, 2, 2) 
    """ 'A#CDEFGH'
    str_map_3D = str(str_map_3D)
    row = int(row)
    column = int(column)
    depth = int(depth)
    c = str(c)
    w = int(w)
    h = int(h)
    d = int(d)
    
    if row > h*d-1 or column > w-1 or depth > d-1:
        return str_map_3D
    else:
        c_position = w*row + column + w*h*depth
        start = str_map_3D[:c_position]
        end = str_map_3D[c_position+1:]
        new_map_3D = start + c + end
        return new_map_3D
    
    
    
    
    
    
