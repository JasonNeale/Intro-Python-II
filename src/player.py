from helpers import kolors
import os

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        new_room = self.current_room

        if direction == 'n':
            if self.current_room.n_to:
                new_room = self.current_room.n_to
        if direction == 's':
            if self.current_room.s_to:
                new_room = self.current_room.s_to
        if direction == 'e':
            if self.current_room.e_to:
                new_room = self.current_room.e_to
        if direction == 'w':
            if self.current_room.w_to:
                new_room = self.current_room.w_to

        if self.current_room.name != new_room.name:
            clear = lambda: os.system('cls')
            clear()
            self.current_room = new_room
        else:
            clear = lambda: os.system('cls')
            clear()
            print(f"{kolors.FAIL}\n############## WARNING ##############\n[{kolors.ENDC} {kolors.WARNING}You stepped on a Lego! Try again.{kolors.ENDC} {kolors.FAIL}]\n############## WARNING ##############{kolors.ENDC}\n\n")