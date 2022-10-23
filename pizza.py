# Melissa Qian
# 261120131
# Assignment 1: Question 2

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    """ (float) -> float
    Returns pizza area of diameter
    
    >>> round(get_pizza_area(1.5),2)
    1.77
    >>> round(get_pizza_area(4.2),2)
    13.85
    >>> round(get_pizza_area(3.0),2)
    7.07
    """
    import math
    diameter = float(diameter)
    area = math.pi*(diameter/2)**2
    return area

def get_fair_quantity(diameter1, diameter2):
    """ (float,float) -> int
    Returns the fair quantity for a pizza of diameter1 and diameter2
    These examples are true if FAIR is set to True :
    
    >>> get_fair_quantity(14.0, 8.0)
    4
    >>> get_fair_quantity(5.0, 15.0)
    9
    >>> get_fair_quantity(5.0, 5.0)
    1
    
    These examples are true if FAIR is set to False :
    
    >>> get_fair_quantity(14.0, 8.0)
    6
    >>> get_fair_quantity(5.0, 15.0)
    14
    >>> get_fair_quantity(5.0, 5.0)
    2
    """
    diameter1 = float(diameter1)
    diameter2 = float(diameter2)
    area1 = get_pizza_area(diameter1)
    area2 = get_pizza_area(diameter2)
    
    if area1 >= area2:
        minimum_quantity = round(-(-area1//area2))
    else:
        minimum_quantity = round(-(-area2//area1))
    
    if FAIR:
        return minimum_quantity
    else:
        return round(1.5*minimum_quantity)

def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    """ (float, float, float, float, int) -> float
    Returns the missing value when float == -1
    
    >>>pizza_formula(12.0, 6.0, 10.0, -1, 2)
    5.0
    >>>pizza_formula(12.0, 6.0, -1, 8.0, 2)
    16.0
    >>>pizza_formula(-1, 9.0, 16.0, 12.0, 3)
    18.0
    >>>pizza_formula(15.0, -1, 16.0, 11.0, 3)
    7.18
    >>>pizza_formula(20.0, 12.0, 25.0, 17.0, -1)
    1.89
    """
    import math
    d_large = float(d_large)
    d_small = float(d_small)
    c_large = float(c_large)
    c_small = float(c_small)
    n_small = int(n_small)
    
    a_small = get_pizza_area(d_small)
    a_large = get_pizza_area(d_large)
    
    if d_large == -1:
        d_large = round(2*math.sqrt(1/math.pi*((c_large/c_small)*n_small*a_small)),2)
        return d_large
    elif d_small == -1:
        d_small = round(2*math.sqrt(1/math.pi*((c_small/c_large)*(a_large/n_small))),2)
        return d_small
    elif c_large == -1:
        c_large = round((c_small*a_large)/(n_small*a_small),2)
        return c_large
    elif c_small == -1:
        c_small = round((c_large*n_small*a_small)/(a_large),2)
        return c_small
    else:
        n_small = round((c_small*a_large)/(c_large*a_small),2)
        return n_small

def get_pizza_cake_cost(base_diameter, height_per_level):
    """ (int,float) -> float
    Returns the cost of a pizza cake
    These examples are true if FAIR is set to True: 
    
    >>> get_pizza_cake_cost(10, 2.0)
    2419.03
    >>> get_pizza_cake_cost(3, 1.0)
    43.98
    >>> get_pizza_cake_cost(5, 2.0)
    345.58
    
    These examples are true if FAIR is set to False :
    
    >>> get_pizza_cake_cost(10, 2.0)
    3628.55
    >>> get_pizza_cake_cost(3, 1.0)
    65.97
    >>> get_pizza_cake_cost(5, 2.0)
    518.37
    """
    base_diameter = int(base_diameter)
    height_per_level = float(height_per_level)
    
    sum_of_areas = 0
    while base_diameter >= 1:
        area_pizza_cake = get_pizza_area(base_diameter)
        sum_of_areas += area_pizza_cake
        base_diameter -= 1
        
        volume_of_pizza = height_per_level*sum_of_areas
        pizza_cake_cost = round(PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED*volume_of_pizza,2)
    
    if FAIR:
        return pizza_cake_cost
    else:
        return round((1.5*pizza_cake_cost),2)

def get_pizza_poutine_cost(diameter, height):
    """ (int,float) -> float
    Returns the cost of a pizza poutine
    These examples are true if FAIR is set to True: 
    
    >>> get_pizza_poutine_cost(10, 2.0)
    471.24
    >>> get_pizza_poutine_cost(3, 1.0)
    21.21 
    >>> get_pizza_poutine_cost(5, 2.0)
    117.81
    
    These examples are true if FAIR is set to False :
    
    >>> get_pizza_poutine_cost(10, 2.0)
    706.86
    >>> get_pizza_poutine_cost(3, 1.0)
    31.82
    >>> get_pizza_poutine_cost(5, 2.0)
    176.72
    """
    diameter = int(diameter)
    height = float(height)
    volume_poutine = height*get_pizza_area(diameter)
    pizza_poutine_cost = round(PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED*volume_poutine,2)
    
    if FAIR:
        return pizza_poutine_cost  
    else:
        return(round(1.5*pizza_poutine_cost,2))
        
def display_welcome_menu():
    """ () -> NoneType
    Prints a welcome menu display
    
    >>> display_welcome_menu()
    Welcome To a Shop That Makes Bad Pizzas
    If you have nothing better to do, please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    """
    print('Welcome To a Shop That Makes Bad Pizzas')
    print('If you have nothing better to do, please choose an option:')
    print('A. Special Orders')
    print('B. Formula Mode')
    print('C. Quantity Mode')

def special_orders():
    """ () -> NoneType
    Prints the final cost of a pizza with or without the special ingredient
    These examples are true if FAIR is set to True :
    
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    
    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 3
    Enter height: 1.5
    Do you want the guacamole? no
    The cost is $31.81
    
    >>>special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 5
    Enter height: 2.0
    Do you want the guacamole? no
    The cost is $345.58 
    """
    choice = input("Would you like the cake or the poutine? ")
    diameter = int(input("Enter diameter: "))
    height = float(input("Enter height: "))
    special_ingredient = input("Do you want the guacamole? ")
    
    if choice == "cake":
        cost = round(get_pizza_cake_cost(diameter, height),2)
    elif choice == "poutine":
        cost = round(get_pizza_poutine_cost(diameter, height),2)
    
    if special_ingredient in ("yes","y"):
        final_cost = round(cost + SPECIAL_INGREDIENT_COST, 2)
        print("The cost is $" + str(final_cost))
    else:
        final_cost = round(cost,2)
        print("The cost is $" + str(final_cost))
            
def quantity_mode():
    """ () -> Nonetype
    Prints the minimum quantity of pizza
    These examples are true if FAIR is set to True :
    
    >>> quantity_mode()
    Enter diameter 1: 14.0
    Enter diameter 2: 8.0
    You should buy 4 pizzas.
    
    >>> quantity_mode()
    Enter diameter 1: 15.0
    Enter diameter 2: 9.0
    You should buy 3 pizzas.
    
    >>> quantity_mode()
    Enter diameter 1: 5.0
    Enter diameter 2: 15.0
    You should buy 9 pizzas. 
    """
    diameter1 = float(input("Enter diameter 1: "))
    diameter2 = float(input("Enter diameter 2: "))
    minimum_quantity = round(get_fair_quantity(diameter1, diameter2))
    print("You should buy",minimum_quantity, "pizzas.")

def formula_mode():
    """ () -> NoneType
    Prints the missing value

    >>> formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    
    >>> formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: -1
    Enter small price: 8.0
    Enter small number: 2
    The missing value is: 16.0 

    >>> formula_mode()
    Enter large diameter: 15.0 
    Enter small diameter: -1
    Enter large price: 16.0
    Enter small price: 11.0
    Enter small number: 3
    The missing value is: 7.18 
    """
    d_large = float(input("Enter large diameter: "))
    d_small = float(input("Enter small diameter: "))
    c_large = float(input("Enter large price: "))
    c_small = float(input("Enter small price: "))
    n_small = int(input("Enter small number: "))
    missing_value = pizza_formula(d_large, d_small, c_large, c_small, n_small)
    print("The missing value is:", missing_value)

def run_pizza_calculator():
    """ () -> NoneType
    Prints the output of choice A, B or C depending on what has been entered
    These examples are true if FAIR is set to True :
    
    >>> run_pizza_calculator()
    Welcome To a Shop That Makes Bad Pizzas
    If you have nothing better to do, please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    
    >>> run_pizza_calculator()
    Welcome To a Shop That Makes Bad Pizzas
    If you have nothing better to do, please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    
    >>> run_pizza_calculator()
    Welcome To a Shop That Makes Bad Pizzas
    If you have nothing better to do, please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: $
    Invalid mode.
    """
    display_welcome_menu()
    your_choice = input("Your choice: ")
    
    if your_choice == "A":
        special_orders()
    elif your_choice == "B":
        formula_mode()
    elif your_choice == "C":
        quantity_mode()
    else:
        print("Invalid mode.")

    
    

    

        
            


      
       
  


    
    
    
        
        
        
        
    
    

    
    
