# DailyExercise
Terminal app for tracking exercise type, repetitions and duration

## References
### Code style guide
van Rossum, G., Warsaw, B. and Coghlan, N. (2013). *PEP 8 – Style Guide for Python Code*. [online] python.org. Available at: https://peps.python.org/pep-0008/ [Accessed 15 Dec. 2022].

## Link to repository
https://github.com/radiantbutterfly/DailyExercise

## Link to presentation
https://youtube.com/watch?v=UJK0-wscmeE&feature=shares

## Features
### Add workouts
With DailyExercise, users can log their workouts for tracking. After selecting "Log today's workout" from the main menu, users will be prompted to enter an exercise and the number of reps or the duration in minutes. For example, "push up 15" will log 15 push ups and "yoga 20" will log 20 minutes of yoga. The user can continue adding as many exercises as they want, or type 'f' to indicate that they are finished. They will then be prompted to save the workout, edit the workout, or quit. If they choose to save the workout, it will be added to a .csv file for later access.

When DailyExercise is opened, it automatically checks the last date recorded in the log. If there is a gap between that date and the current date, it will fill the log with zeros for the missing days. This ensures that streaks and history continue to function correctly even if the user does not open the program for several days.
### Add exercises
DailyExercise comes with a predefined list of 20 common exercises. Attempting to enter a workout containing an unrecognized exercise will fail. However, the user can define custom exercise types by selecting "Add new exercise type" from the main menu. They will be prompted to enter a name for the new exercise and a measurement (reps or minutes). It will then be possible to include the new exercise in workouts and access streaks and history for it.
### Streaks
DailyExercise tracks the users "streaks", or the number of consecutive days that they have successfully achieved their goals for a particular exercise. Streaks are individually tracked for each exercise, so that the user can simultaneously have a 30 day streak for yoga and a 10 day streak for running. The conditions for a streak can also be defined by the user. By default, a "streak" requires the user to log an exercise every day. However, by selecting "Streaks" from the main menu, and then "Define streak conditions", users can choose from a number of rules, such as "Every day" or "Three times a week". Goals defined in terms of "X times a week" are flexible, it doesn't matter which days of the week the user exercises as long as it is at least X times in a seven-day-period starting from each Monday. A streak is broken as soon as a week is detected that contains too many days without the exercise.

When a workout is logged, DailyExercise analyses the history of each exercise to see if the conditions for a streak have been met. If so, it will alert the user of their current streak for each exercise. It will also compare the current streak to the previous longest streak for that exercise, and update the longest streak if necessary.

A user can also view their current streaks by selecting "Streaks" from the main menu, and then "View all current streaks" from the Streaks submenu. If they have many current streaks, they can instead search for a specific exercise by selecting "Search for current streak".
### History
By accessing "History" from the main menu, users can search for a particular exercise to receive information about it. This includes the total number of days on which the exercise was performed, and the total number of reps, or if the exercise is measured in time, the total number of hours and minutes spent. It also includes the increase in reps or duration, comparing the first workout to the largest one recorded. Finally, it includes the length of the longest streak on record.

## Implementation plan
To create this app, I used Trello as a project management tracker (https://trello.com/b/9OnQOFW1/exercise-tracker). I created cards with user stories for each feature I wanted to include and moved them from "To Do" to "Doing" and "Done" as I made progress on them. Here is the approximate order in which I implemented each feature.

1. Main menu and the ability to choose options with numeric input. (Deadline: Dec 8)
2. Close program when the user types 'q' for quit. (Deadline: Dec 8)
### Add workouts 
3. Get workout information from user input. (Deadline: Dec 10)
4. Save workout information to .csv file. (Deadline: Dec 10)
5. Ask the user to confirm the workout before saving. (Deadline: Dec 11)
6. View and edit workout before saving. (Deadline: Dec 11)
7. Check for date of most recent workout (to prevent the user from logging two workouts with the same date). (Deadline: Dec 11)
### Add exercise type
8. Get new exercise name from user input. (Deadline: Dec 12)
9. Classify exercises by measurement type (reps or duration). (Deadline: Dec 12)
10. Confirm that exercise name and measurement are correct. (Deadline: Dec 12)
11. Save exercises to exercise list. (Deadline: Dec 12)
12. Update log to contain a column for the new exercise, and fill it with 0 for all previous dates. (Deadline: Dec 14)
13. Update longest streak file to set the longest streak for the new exercise to 0. (Deadline: Dec 14)
### Streaks
14. Get user-defined streak conditions. (Deadline: Dec 12)
15. Determine current streaks. (Deadline: Dec 13)
16. Return all current streaks to user. (Deadline: Dec 13)
17. Notify user of current streaks when they log a workout. (Deadline: Dec 13)
18. Allow user to search their current streaks by exercise name. (Deadline: Dec 13)
### History
19. Retrieve log history for a specific exercise. (Deadline: Dec 14)
20. Calculate total days on which the exercise was performed. (Deadline: Dec 14)
21. Calculate the total number of reps, or the total number of hours and minutes for an exercise. (Deadline: Dec 14)
22. Find the increase in reps or time between when the user first did the exercise, and their best workout. (Deadline: Dec 14)
23. Retrieve longest streak information. (Deadline: Dec 14)
24. Generate report displaying all of the above in a user-friendly manner. (Deadline: Dec 14)
25. Generate spreadsheet with full history of an exercise and dates. (Deadline Dec 18)

## Help Documentation
### Setup
DailyExercise requires Python 3 to run.

To run DailyExercise, first clone the repository with ```git clone https://github.com/radiantbutterfly/DailyExercise```.

Then navigate into the folder containing DailyExercise and run setup.sh. This will create a virtual environment to run the program in and install the required packages.
### Running DailyExercise
Once setup has been completed, you will be able to run DailyExercise with ./dailyexercise.sh

### Requirements
Python 3

attrs 22.1.0

exceptiongroup 1.0.4

iniconfig 1.1.1

numpy 1.23.5

packaging 22.0

pandas 1.5.2

pluggy 1.0.0

pytest 7.2.0

python-dateutil 2.8.2

pytz 2022.6

six 1.16.0

tomli 2.0.1
## Testing
Testing can be done with pytest, which will find and execute run_test.py. Before testing, it is necessary to run generate_test_files.py to generate mock data for testing. The tests will fail if performed on blank log files or real user data. Run ./test_setup.sh to generate the test files. Or, to prepare for tests manually, run python3 generate_test_files.py, rename the existing streakconditions.csv file to backup_streakconditions.csv, and rename test_streakconditions.csv to streakconditions.csv.

To return the app to normal operation after the test, run ./test_cleanup.sh. Or manually delete test_log.csv and streakconditions.csv and rename backup_streakconditions.csv to streakconditions.csv.

The tests test the following things:

TEST 1- A test of the "Streaks" feature, which tests that the find_current_streak_length function returns the correct number of days in the following scenarios:
1. 70 day streak with "every day" condition.
2. 70 day streak with "3 times a week" condition.
3. 70 day streak with "once a week" condition.
4. 70 day streak with "every second day" condition.
5. Test for "every day" streak when no streak exists (returns 0 days).

TEST 2- A test of the "History" feature, which tests that the find_total_reps function returns the correct number of reps or minutes in the following scenarios:
1. 1 min per day every day for 70 days (returns 70 mins).
2. 1 min per day 5 times a week for 10 weeks (returns 50 mins).
3. An exercise for which there are no recorded workouts (returns 0 mins).