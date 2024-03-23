#!/usr/bin/python3
search_replace = __import__('epl_table').search_replace


epl_table = {
    "Manchester City": {"MP": 28, "W": 21, "D": 3, "L": 4, "GF": 65, "GA": 22, "GD": 43, "Pts": 66},
    "Liverpool": {"MP": 27, "W": 18, "D": 7, "L": 2, "GF": 61, "GA": 19, "GD": 42, "Pts": 61},
    "Chelsea": {"MP": 28, "W": 17, "D": 6, "L": 5, "GF": 55, "GA": 25, "GD": 30, "Pts": 57},
    "Manchester United": {"MP": 27, "W": 15, "D": 7, "L": 5, "GF": 49, "GA": 30, "GD": 19, "Pts": 52},
    "Arsenal": {"MP": 28, "W": 14, "D": 4, "L": 10, "GF": 44, "GA": 32, "GD": 12, "Pts": 46}
}

while True:
    print("\nMenu:")
    print("1. Display EPL Table")
    print("2. Search Team")
    print("3. Update Team Results")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_table(epl_table)
    elif choice == "2":
        search_team(epl_table)
    elif choice == "3":
        update_results(epl_table)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

# Example usage of search_replace function
new_table = {}
for team, stats in epl_table.items():
    new_stats = search_replace(list(stats.values()), 28, 30)  # Replace 28 with 30 in each statistic
    new_table[team] = {key: value for key, value in zip(stats.keys(), new_stats)}
print(new_table)
print(epl_table)
