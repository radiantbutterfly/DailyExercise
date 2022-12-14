import csv
from datetime import datetime
import pandas

MAIN_MENU_ITEMS = 4
STREAK_MENU_ITEMS = 4
HISTORY_MENU_ITEMS = 3

DEFAULT_CSV = "log.csv"
LONGEST_STREAK_FILE = "longest_streak.csv"
EXERCISE_FILE = "exerciselist.csv"


def get_exercise_dict():
    with open("exerciselist.csv", "r") as file:
        reader = csv.reader(file)
        exercise_dict = dict(reader)
        return exercise_dict


EXERCISE_DICT = get_exercise_dict()
EXERCISE_LIST = list(EXERCISE_DICT.keys())

STREAK_CONDITIONS_FILE = "streakconditions.csv"


def get_streak_conditions():
    with open(STREAK_CONDITIONS_FILE, "r") as file:
        reader = csv.reader(file)
        streak_conditions = dict(reader)
        return streak_conditions


STREAK_CONDITIONS = get_streak_conditions()