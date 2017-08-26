# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

from csv import *

with open('football.csv') as f:
    csv_reader = reader(f, delimiter=',')
    next(csv_reader, None)

    min_diff = float('inf')
    min_team = ''

    for row in csv_reader:
        goals_for = int(row[5])
        goals_against = int(row[6])
        diff = abs(goals_for - goals_against)
        if diff < min_diff:
            min_team = row[0]
            min_diff = diff

    print(min_team, min_diff)
