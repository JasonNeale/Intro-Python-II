from room import Room
from player import Player
from helpers import kolors
import os
import sys
from item import Item

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

items = {
    'ram': Item("RAM", "RAM is your system's short-term memory. Whenever your computer performs calculations, it temporarily stores the data in the RAM until it is needed."),
    'cpu': Item("CPU", "The central processing unit (CPU), also called a processor, is located inside the computer case on the motherboard. It is sometimes called the brain of the computer, and its job is to carry out commands."),
    'fans': Item('Fans', 'Fans are used to cool internal case components.'),
    
    'gpu': Item("GPU", "The video card is responsible for what you see on the monitor."),
    'psu': Item("PSU", "The power supply unit in a computer converts the power from the wall outlet to the type of power needed by the computer."),
    'motherboard': Item("Motherboard", "The motherboard is the computer's main circuit board. It's a thin plate that holds the CPU, memory, connectors for the hard drive and optical drives, expansion cards to control the video and audio, and connections to your computer's ports"),
    
    'cables': Item("Cables", "Assorted cables to connect components to an from each other."),
    'aio': Item("AIO", "An All-In-One liquid CPU cooler that contains a pump, fans and a radiator."),
    'm.2': Item("M.2", "The hard drive is where your software, documents, and other files are stored."),
    
    'monitor': Item("Monitor", "The monitor works with a video card, located inside the computer case, to display images and text on the screen."),
    'keyboard': Item("Keyboard", "The keyboard is one of the main ways to communicate with a computer."),
    'mouse': Item("Mouse", "Another important tool for communicating with computers. Commonly known as a pointing device, it lets you point to objects on the screen, click on them, and move them."),
    
    'os': Item("OS", "The operating system (OS) manages all of the software and hardware on the computer."),
    'case': Item("Case", "The metal and plastic box that contains the main components of the computer, including the motherboard, central processing unit (CPU), and power supply."),
    'rgb': Item("RGB", "Assorted RGB lighting accessories.")
}

# Add items to rooms

room['outside'].add_item(items['ram'])
room['outside'].add_item(items['cpu'])
room['outside'].add_item(items['fans'])

room['foyer'].add_item(items['gpu'])
room['foyer'].add_item(items['psu'])
room['foyer'].add_item(items['motherboard'])

room['overlook'].add_item(items['cables'])
room['overlook'].add_item(items['aio'])
room['overlook'].add_item(items['m.2'])

room['narrow'].add_item(items['monitor'])
room['narrow'].add_item(items['keyboard'])
room['narrow'].add_item(items['mouse'])

room['treasure'].add_item(items['os'])
room['treasure'].add_item(items['case'])
room['treasure'].add_item(items['rgb'])

def get_user_choice():
    return input(choice_message)

def concat_items(items):
    result = ""
    
    for item in items:
        result += f"{kolors.Magenta}{item.name}:{kolors.ENDC} {item.description}\n"
    
    return result

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
choice_message = (f"\n{kolors.UNDERLINE}{kolors.OKBLUE}Which direction would you like to go?{kolors.ENDC}\n\n{kolors.WARNING}[n] North\n[s] South\n[e] East\n[w] West{kolors.ENDC}\n\n{kolors.OKGREEN}Navigate:{kolors.ENDC}")

while playing:
    item_list = f"\n{kolors.UNDERLINE}{kolors.OKBLUE}Room items:{kolors.ENDC}\n{concat_items(player.current_room.items)}"
    player_inventory = f"\n{kolors.UNDERLINE}{kolors.OKBLUE}Current inventory:{kolors.ENDC}\n{concat_items(player.inventory)}"
    current_location = f"\n{kolors.UNDERLINE}{kolors.OKBLUE}Location:{kolors.ENDC}\n{player.current_room.name}\n\n{kolors.UNDERLINE}{kolors.OKBLUE}Description:{kolors.ENDC} \n{player.current_room.description}"
    
    if sys.platform == 'win32':
        clear = lambda: os.system('cls')
        clear()
    else:
        clear = lambda: os.system('clear')
        clear()
    
    print(current_location)
    print(item_list)
    print(player_inventory)
    
    choice = get_user_choice().split(' ')
    
    if choice[0] == 'i' or choice[0] == 'inventory':
        print(player_inventory)
    
    if choice[0] == 'q':
        print(game_title_2)
        playing = False

    if playing:
        if choice[0] == 'n' or choice[0] == 's' or choice[0] == 'e' or choice[0] == 'w':
            player.move(choice[0])
        
        if len(choice) == 2 and choice[0] == 'drop':
            item = items[choice[1].lower()]
            player.drop_item(item)
            player.current_room.add_item(item)

        if len(choice) == 2 and choice[0] == 'grab':
            item = items[choice[1].lower()]
            player.grab_item(item)
            player.current_room.remove_item(item)

        