from datetime import datetime
import pandas
from constants import DEFAULT_CSV, LONGEST_STREAK_FILE

def get_log_dates():
    log = pandas.read_csv(DEFAULT_CSV)
    log_dates = log["DATE"].tolist()
    return log_dates


def get_last_log_date():
    log_dates = get_log_dates()
    if len(log_dates) == 0:
        return 0
    last_log_date = log_dates[-1]
    return last_log_date


def last_log_date_datetime():
    last_log_date = get_last_log_date()
    if last_log_date == 0:
        return 0
    try:
        datetime_date = datetime.strptime(last_log_date.strip(), "%Y-%m-%d")
    except ValueError:
        print("Error: Log file returned invalid date. If problem persists, delete log.csv "
        "and restart DailyExercise.")
    return datetime_date


def determine_log_age(log_date):
    date = datetime.strptime(log_date, "%Y-%m-%d")
    today = datetime.today()
    return abs((date - today).days)
    

def get_longest_streak_dict():
    dataframe = pandas.read_csv(LONGEST_STREAK_FILE, header=None, index_col=0).squeeze("columns")
    streak_dict = dataframe.to_dict()
    return streak_dict