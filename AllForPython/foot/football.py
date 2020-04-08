import os
import sys
import pandas as pd
import numpy as np

flag = 1

pd.set_option("display.max_rows", 3000)
pd.set_option("display.max_columns", 30)

def show_table():
    cols = ['place', 'name', 'games played', 'wins', 'draws', 'losses', ' Goal difference', 'Points']
    info = []

    super_set = set(buff.loc[:, 'Home'].values) | set(buff.loc[:, 'Away'].values)
    for team in super_set:

        game_count = 0
        points = 0
        losses = 0
        wins = 0
        draws = 0
        goal_dif = 0

        for i in range(len(buff.index)):
            if (team == buff.iloc[i,5]):
                game_count += 1
                goal_dif += (buff.iloc[i,7] - buff.iloc[i,8])
                if buff.iloc[i,9] == 'A':
                    losses += 1
                elif buff.iloc[i,9] == 'H':
                    wins += 1
                    points += 2
                else:
                    draws += 1
                    points += 1
            if (team == buff.iloc[i,6]):
                game_count += 1
                goal_dif += (-buff.iloc[i,7] + buff.iloc[i,8])
                if buff.iloc[i,9] == 'A':
                    wins += 1
                    points += 2
                elif buff.iloc[i,9] == 'H':
                    losses += 1
                else:
                    draws += 1
                    points += 1
        info.append([0, team, game_count, wins, draws, losses, goal_dif, points])

    df = pd.DataFrame(info, columns=cols)
    df.sort_values(by=['Points'], inplace=True, ascending=False)
    for k, i in enumerate(range(len(df.index))):
        df.iloc[i,0] = k+1
    df.set_index('place', inplace=True)
    print(df)
    return

def show_all_for_team():
    super_list = list(set(buff.loc[:, 'Home'].values) | set(buff.loc[:, 'Away'].values))
    print('Choose team from the following list: ')
    for k, i in enumerate(super_list):
        print(str(k+1) + '.', i)
    number_of_team = int(input('Input number of team: '))

    team = super_list[number_of_team-1]

    cols = ['Date', 'Home', 'Away', 'Home result', 'Away result']
    info = []

    for i in range(len(buff.index)):

        date = ''
        home = ''
        away = ''
        home_res = ''
        away_res = ''

        if (team == buff.iloc[i,5]) or (team == buff.iloc[i,6]):
            home_res = buff.iloc[i,7]
            away_res = buff.iloc[i,8]
            home = buff.iloc[i,5]
            away = buff.iloc[i,6]
            date = buff.iloc[i,3]
            info.append([date, home, away, home_res, away_res])


    df = pd.DataFrame(info, columns=cols)
    df.set_index('Date', inplace=True)
    print(df)

    return

def show_all_for_date():
    super_list = list(set(buff.loc[:, 'Date'].values))
    print('Choose date from the following list: ')
    for k, i in enumerate(super_list):
        print(str(k+1) + '.', i)
    number_of_date = int(input('Input number of date: '))

    user_date = super_list[number_of_date-1]

    cols = ['Date', 'Home', 'Away', 'Home result', 'Away result']
    info = []

    for i in range(len(buff.index)):

        date = ''
        home = ''
        away = ''
        home_res = ''
        away_res = ''

        if (user_date == buff.iloc[i,3]):
            home_res = buff.iloc[i,7]
            away_res = buff.iloc[i,8]
            home = buff.iloc[i,5]
            away = buff.iloc[i,6]
            date = buff.iloc[i,3]
            info.append([date, home, away, home_res, away_res])


    df = pd.DataFrame(info, columns=cols)
    df.set_index('Date', inplace=True)
    print(df)
    return

def prev_menu():
    return

current_path = os.getcwd()
list_of_leagues = []
league = ''
functions_list = [show_all_for_team, show_all_for_date, show_table, prev_menu]

def show_menu():
    print('Choose one option from the list:\n1) Show all matches of a given team\n2) Show matches played on a given date\n3) Show the ranking table\n4) Go to menu of league choose')
    n = int(input())
    if n == 4:
        return 0
    else:
        functions_list[n-1]()
        return 1

while 1:
    flag = 1
    print('Choose league from the following list: ')
    n = 0
    for file in os.listdir(current_path):
        if file.endswith('.csv'):
            n += 1
            print(n, file[:len(file)-4])
            list_of_leagues.append(file)

    number_of_league = int(input('Input number of league (or 0 for exit): '))
    if not number_of_league:
        sys.exit()
    while flag:
        buff = pd.read_csv(list_of_leagues[number_of_league-1])
        flag = show_menu()
