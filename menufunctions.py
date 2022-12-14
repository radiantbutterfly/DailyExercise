import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def quit_function():
    raise FloatingPointError

def get_menu_selection(number_of_menu_items):
    while True:
        menu_selection = input("Enter your selection, or 'q' to quit: ")
        if menu_selection.lower() == "q":
            quit_function()
        elif not menu_selection.isnumeric():
            print("Invalid menu selection. Enter a number, or 'q' to quit: ")
            continue
        elif int(menu_selection) > number_of_menu_items or int(menu_selection) == 0:
            print("Invalid menu selection. Enter a number, or 'q' to quit: ")
            continue
        else:
            return int(menu_selection)

def press_enter_to_continue():
    user_input = input("Press enter to continue")
    if user_input == "q":
        quit_function()

def input_exercise_type():
    user_input = input("Enter exercise type, or 'c' to cancel: ")
    if user_input.lower() == "q":
        quit_function()
    return user_input