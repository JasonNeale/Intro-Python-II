from room import Room
from player import Player
from helpers import kolors
import os
import sys

game_title = (f"""
{kolors.BackgroundDarkGray}                                                                {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                         Welcome to...                        {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC} (¯`·.___.··¸.-~*´¨¯¨`*·~-.---|----.-~*´¨¯¨`*·~-.¸··.___.·´¯) {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}     \         |                       |                      {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}    _ \     _` | \ \   /   _ \  __ \   __|  |   |   __|   _ \ {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}   ___ \   (   |  \ \ /    __/  |   |  |    |   |  |      __/ {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC} _/    _\ \__._|   \_/   \___| _|  _| \__| \__._| _|    \___| {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray}                       Text Adventure Game                      {kolors.ENDC}
""")

game_title_2 = (f"""
{kolors.BackgroundDarkGray}                                                                {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                          Buh Bye...                          {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC} (¯`·.___.··¸.-~*´¨¯¨`*·~-.---|----.-~*´¨¯¨`*·~-.¸··.___.·´¯) {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}     \         |                       |                      {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}    _ \     _` | \ \   /   _ \  __ \   __|  |   |   __|   _ \ {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}   ___ \   (   |  \ \ /    __/  |   |  |    |   |  |      __/ {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC} _/    _\ \__._|   \_/   \___| _|  _| \__| \__._| _|    \___| {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray} {kolors.ENDC}                                                              {kolors.BackgroundDarkGray} {kolors.ENDC}
{kolors.BackgroundDarkGray}                       Text Adventure Game                      {kolors.ENDC}
""")

print(game_title)

# Declare all the rooms
room = {
    'outside': Room(
        "Outside Cave Entrance", 
        """North of you, the cave mount beckons"""
        ),
    'foyer': Room(
        "Foyer", 
        """Dim light filters in from the south.\nDusty passages run north and east."""
        ),
    'overlook': Room(
        "Grand Overlook", 
        """A steep cliff appears before you, falling into the darkness.\n\nAhead to the north, a light flickers in the distance,\nbut there is no way across the chasm."""
        ),
    'narrow':   Room(
        "Narrow Passage", 
        """The narrow passage bends here from west to north.\nThe smell of gold permeates the air."""
        ),
    'treasure': Room(
        "Treasure Chamber", 
        """You've found the long-lost treasure chamber! Sadly,\nit has already been completely emptied by earlier adventurers.\nThe only exit is to the south."""
        ),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
def get_user_choice():
    return input(choice_message)

def move_to(room, direction):
    new_room = room

    if direction == 'n':
        if room.n_to:
            new_room = room.n_to
    if direction == 's':
        if room.s_to:
            new_room = room.s_to
    if direction == 'e':
        if room.e_to:
            new_room = room.e_to
    if direction == 'w':
        if room.w_to:
            new_room = room.w_to

    return new_room

def get_user_name():
    username = input(f"\n{kolors.OKGREEN}Enter your username:{kolors.ENDC}\n")

    if sys.platform == 'win32':
        clear = lambda: os.system('cls')
        clear()
    else:
        clear = lambda: os.system('clear')
        clear()
    
    return Player(username, room['outside'])

playing = True
player = get_user_name()
choice_message = (f"\n{kolors.UNDERLINE}{kolors.OKBLUE}Which direction would you like to go?{kolors.ENDC}\n\n{kolors.WARNING}[n] North\n[s] South\n[e] East\n[w] West{kolors.ENDC}\n\n{kolors.OKGREEN}Navigate:{kolors.ENDC}\n")

while playing:
    current_location = f"{kolors.UNDERLINE}{kolors.OKBLUE}Location:{kolors.ENDC}\n{player.current_room.name}\n\n{kolors.UNDERLINE}{kolors.OKBLUE}Description:{kolors.ENDC} \n{player.current_room.description}"
    print(current_location)
    choice = get_user_choice().split(' ')

    # If the user enters "q", quit the game.
    if choice[0] == 'q':
        print(game_title_2)
        playing = False

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if playing:
        if choice[0] == 'n' or choice[0] == 's' or choice[0] == 'e':
            player.move(choice[0])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.