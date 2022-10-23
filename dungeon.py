# Melissa Qian
# 261120131
# Assignment 2: Question 1

ROOM_NAME = 'The Classroom'
AUTHOR = 'Melissa Qian'
PUBLIC = True

# PUBLIC = False, not displayed to public

def list_command_b():
    """ () -> NoneType
    Prints the list of commands B.
    
    >>> list_command_b()
    modify your grade
    look at the second tab
    """
    print("modify your grade.\nlook at the second tab.")
            
def list_command_a():
    """ () -> NoneType
    Prints the list of commands A.
    
    >>> list_command_a()
    examine the computer
    investigate the sound
    use the flashlight 
    """
    print ("examine the computer\ninvestigate the sound\nuse the flashlight")

def computer_actions():
    """ () -> NoneType
    Prints out the results of action_1 to action_3.

    >>> computer_actions
    > list commands
    list_command_b() 
    
    >>> computer_actions
    > modify your grade
    GAME OVER!
    As you were about to change your grade to A+, the computer suddenly catches on fire and you perish.
    Rest in Peace.
    Try again.
    
    >>> computer_actions
    > look at the second tab
    The page provides the following phone number:
    1800-JAN-ITOR
    If you had a phone, you could call this number.
    """
    while True:
        action_1 = "commands"
        action_2 = "grade"
        action_3 = "second tab"
        command = input("> ").lower()
        if action_1 in command:
            list_command_b()
        elif action_2 in command:
            print("""GAME OVER!
As you were about to change your grade to A+, the computer suddenly catches on fire and you perish.
Rest in Peace.
Try again.""")
        elif action_3 in command:
            print("The page provides the following phone number:\n1800-JAN-ITOR\nIf you had a phone, you could call this number.")
            break
        else:
            print("Invalid command. Please try again.")
            
def room_setting():
    """ () -> NoneType
    Prints out the setting of the room.
    
    >>> room_setting()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    """
    print(ROOM_NAME)
    print("by",AUTHOR)
    print ("""After snoozing off in class, you wake up to an empty classroom.
Your phone is dead and you have no way to make use of it since you left your charger back home.
You tried opening the door and the windows, but they are locked.
The room is pitch black, and only the professor's computer screen is letting out some light in the room.
You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
What do you do?""")
    
def public_room():
    """ () -> NoneType
    Prints out the results of action_1 to escape_action.
    
    >>> public_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > list commands
    examine the computer
    investigate the sound
    use the flashlight
    
    >>> public_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > use the flashlight
    You flash the light towards the classroom's blackboard. It states the following:
    Janitors save lives!
    
    >>> public_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > investigate the sound
    You follow the sound which leads you to the desk of your classmate Katherine.
    The sound was coming out of a mini musical box attached to her flip phone in her desk.
    She has a flip phone because she lost her Iphone 13 in Sherbrooke and is too lazy to get it back, hence the old phone.
    However, a plus side to this phone is that it almost never dies.
    Do you have a number you want to try calling?
    """
    room_setting()
    action_1 = "command"
    action_2 = "computer"
    action_3 = "flashlight"
    action_4 = "sound"
    escape_action = "number"
    while True:
        command = input("> ").lower()
        if action_1 in command:
            list_command_a()
        elif action_2 in command:
            print("""There are two tabs opened.
The first tab reveals that you received a failing grade in your comp202 assignment.
The second tab is hidden by the first tab.
What do you do?""")
            computer_actions()
        elif action_3 in command:
            print("""You flash the light towards the classroom's blackboard. It states the following:
Janitors save lives!""")
        elif action_4 in command:
            print("""You follow the sound which leads you to the desk of your classmate Katherine.
The sound was coming out of a mini musical box attached to her flip phone in her desk.
She has a flip phone because she lost her Iphone 13 in Sherbrooke and is too lazy to get it back, hence the old phone.
However, a plus side to this phone is that it almost never dies.
Do you have a number you want to try calling?""")
        elif escape_action in command:
            print("""The phone rings and the school's night-janitor answers.
After telling them that you are stuck in the classroom, they come open the door and you get to go home and sleep.
Sweet dreams!""")
            break
        else:
            print("Invalid command. Please try again.")
    
def escape_room():
    """ () -> NoneType
    Displays the escape room.
    
    This example is True if PUBLIC is set to True: 
    
    >>> escape_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > list commands
    examine the computer
    investigate the sound
    use the flashlight
    
    >>> escape_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > use the flashlight
    You flash the light towards the classroom's blackboard. It states the following:
    Janitors save lives!
    
    >>> escape_room()
    The Classroom
    by Melissa Qian
    After snoozing off in class, you wake up to an empty classroom.
    Your phone is dead and you have no way to make use of it since you left your charger back home.
    You tried opening the door and the windows, but they are locked.
    The room is pitch black, and only the professor's computer screen is letting out some light in the room.
    You also remember you have a flashlight in your bag. Finally, you hear some muffled sound in the classroom.
    What do you do?
    > call number
    The phone rings and the school's night-janitor answers.
    After telling them that you are stuck in the classroom, they come open the door and you get to go home and sleep.
    Sweet dreams!
    
    This example is True if PUBLIC is set to False:
    
    >>> escape_room()
    The Classroom by Melissa Qian is not available to the public.
    """
    if PUBLIC:
        public_room()
    else:
        print(ROOM_NAME,"by",AUTHOR,"is not available to the public.")