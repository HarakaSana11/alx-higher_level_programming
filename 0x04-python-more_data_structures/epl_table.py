#!/usr/bin/python3

def search_replace(epl_table, search, replace):
    return list(map(lambda x: replace if x is search else x, epl_table))

def display_table(teams):
    print("EPL Table:")
    print("--------------------------------------------------------------------------------------------")
    print(f"| {'Team':<20} | {'MP':>2} | {'W':>2} | {'D':>2} | {'L':>2} | {'GF':>2} | {'GA':>2} | {'GD':>3} | {'Pts':>3} |")
    print("--------------------------------------------------------------------------------------------")
    for team, stats in teams.items():
        print(f"| {team:<20} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['GF']:>2} | {stats['GA']:>2} | {stats['GD']:>3} | {stats['Pts']:>3} |")
    print("--------------------------------------------------------------------------------------------")

def search_team(teams):
    team = input("Enter the team name to search: ")
    if team in teams:
        stats = teams[team]
        print(f"{team} has {stats['Pts']} points with {stats['W']} wins, {stats['D']} draws, and {stats['L']} losses.")
        print(f"Goals scored: {stats['GF']}, Goals conceded: {stats['GA']}, Goal difference: {stats['GD']}.")
    else:
        print(f"{team} not found in the table.")

def update_results(teams):
    team = input("Enter the team name to update: ")
    if team in teams:
        new_points = int(input(f"Enter the new points for {team}: "))
        teams[team]['Pts'] = new_points
        print(f"{team}'s points updated to {new_points}.")
    else:
        print(f"{team} not found in the table.")
