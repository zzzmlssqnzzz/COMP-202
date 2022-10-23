# Melissa Qian
# 261120131
# Assignment 2: Question 2

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

import random

def generate_treasure_map_row(w, b):
    """ (int, bool) -> str
    Creates and returns a single row of the given width (as a string) of
    a treasure map
    
    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, False)
    '^>^>..^>v.'
    
    >>> random.seed(9001)
    >>> generate_treasure_map_row(12, True)
    '..^<>^<>v.v|'
    
    >>> random.seed(9001)
    >>> generate_treasure_map_row(8, False)
    '^<^<.^>^'
    """
    w = int(w)
    row = ''
    for i in range(w):
        if random.randint(1,6) == 1:
            row +=EMPTY_SYMBOL
        else:
            symbol = random.randint(1,4)
            if symbol == 1:
                row +=MOVEMENT_SYMBOLS[0]
            if symbol == 2:
                row +=MOVEMENT_SYMBOLS[1]
            if symbol == 3:
                row +=MOVEMENT_SYMBOLS[2]
            if symbol == 4:
                row +=MOVEMENT_SYMBOLS[3]
                
    if b == True and random.randint(1,2) == 1:
        position = random.randint(0, w-1)
        symbol = random.randint(1,2)
        if symbol == 1:
            return row[:position]+MOVEMENT_SYMBOLS_3D[0]+row[position+1:]
        if symbol == 2:
            return row[:position]+MOVEMENT_SYMBOLS_3D[1]+row[position+1:]
    return row
        
def generate_treasure_map(w, h, b):
    """ (int, int, bool) -> 
    Creates and returns a treasure map of the given width and height (as a
    string)
    
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 3, False)
    '>>^>..^>v'
    
    >>> random.seed(9001)
    >>> generate_treasure_map(6, 3, False)
    '>.v.v>vv>^<^^<<<^^'
    
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 11, True)
    '>.*vv>|^^v<^v>*v.*vv.|^^>.|^v<.^*'
    """
    w = int(w)
    h = int(h)
    treasure_map= ''
    i = 0
    for i in range(h):
        if i == 0:
            treasure_map += MOVEMENT_SYMBOLS[0]
            treasure_map += generate_treasure_map_row(w-1, b)
        else:
            treasure_map += generate_treasure_map_row(w, b)
    return treasure_map

def generate_3D_treasure_map(w, h, d):
    """ (int, int, int) -> str
    Creates and returns a 3D treasure map of the given
    width, height and depth (as a string)

    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 3, 3)
    '>>|^>|.*v>|^v.*^v*>^^^v<.>|'
    
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(2, 4, 3)
    '>v*<.><v|.<*><v>v|<^...v'
    
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(5, 2, 3)
    '>*..<>><v.vv<.|^..<^<<vv.vv<vv'
    """
    w = int(w)
    h = int(h)
    d = int(d)
    b = True
    map_3D = ''
    i = 0
    for i in range(h*d):
        if i == 0:
            map_3D += MOVEMENT_SYMBOLS[0]
            map_3D += generate_treasure_map_row(w-1, b)
        else:
            map_3D += generate_treasure_map_row(w, b)
    return map_3D
    
def follow_trail(str_map_3D, row, column, depth, w, h, d, tiles):
    """ (str, int, int, int, int, int, int, int) -> str
    Prints the number of treasures collected in the format and the number of symbols visited and
    returns the travelled map
    
    >>> follow_trail('>+....', 0, 0, 0, 3, 2, 1, 3)
    Treasures collected: 1
    Symbols visited: 3
    'X+....'
    
    >>> follow_trail('>...v<.+.', 0, 0, 0, 4, 2, 0, 3)
    Treasures collected: 0
    Symbols visited: 1
    'X...v<.+.'
    
    >>> follow_trail('>*..<>><v.vv<.|^..<^<<v|.vv<vv', 0, 0, 0, 5, 2, 3, 3)
    Treasures collected: 0
    Symbols visited: 3
    'XX..+>><v.vX<.|^..<^<<v|.vv<v+'
    """
    import treasure_utils
    
    str_map_3D = str(str_map_3D)
    row = int(row)
    column = int(column)
    depth = int(depth)
    w = int(w)
    h = int(h)
    d = int(d)
    tiles = int(tiles)
    
    if row > h*d - 1 or column > w-1 or depth > d-1:
        return str_map_3D
    i = 0
    symbol =''
    for i in range(tiles):
        if symbol == MOVEMENT_SYMBOLS[0]:
            column+=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == MOVEMENT_SYMBOLS[1]:
            column-=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == MOVEMENT_SYMBOLS[2]:
            row+=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == MOVEMENT_SYMBOLS[3]:
            row-=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == MOVEMENT_SYMBOLS_3D[0]:
            depth+=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == MOVEMENT_SYMBOLS_3D[1]:
            depth-=1
            treasure_utils.change_char_in_3D_map(str_map_3D, row, column, depth, BREADCRUMB_SYMBOL, w, h, d)
        elif symbol == EMPTY_SYMBOL:
            if str_map_3D[i-1] == MOVEMENT_SYMBOLS[0]:
                column += 1
            if str_map_3D[i-1] == MOVEMENT_SYMBOLS[1]:
                column -= 1
                
        num_treasure = str_map_3D.count(TREASURE_SYMBOL)
        print("Treasures collected:", num_treasure)
        symbol_visited = str_map_3D.count(BREADCRUMB_SYMBOL)
        print("Symbols visited:", symbol_visited)
        break
    return str_map_3D
    
    
                    
        
    
    
    