import json


def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from '{file_name}'.")
        return None


def search_player_stats(data, player_name):
    for player in data:
        if player["name"].lower() == player_name.lower():
            formatted_line = f"{player['name']:<22}{player['team'][-3:]:<8}{player['assists']:<8} + {player['goals']:<5} = {player['assists'] + player['goals']:<5}"
            print(formatted_line)
            return player
    print(f"Player '{player_name}' not found.")
    return None


def search_by_team(data, team_name):
    players_found = False

    for player in data:
        if player["team"].lower() == team_name.lower():
            formatted_line = f"{player['name']:<22}{player['team'][-3:]:<8}{player['assists']:<8} + {player['goals']:<5} = {player['assists'] + player['goals']:<5}"
            print(formatted_line)
            players_found = True

    if not players_found:
        print(f"No players found in team '{team_name}'.")


def search_by_nationality(data, nationality):
    players_found = False

    for player in data:
        if player["nationality"].lower() == nationality.lower():
            formatted_line = f"{player['name']:<22}{player['team'][-3:]:<8}{player['assists']:<8} + {player['goals']:<5} = {player['assists'] + player['goals']:<5}"
            print(formatted_line)
            players_found = True

    if not players_found:
        print(f"No players found with nationality '{nationality}'.")


def list_top_players_by_points(data, n):
    n = int(n)

    sorted_players = sorted(
        data,
        key=lambda player: (  # sorting first by points, then by goals, then by games played
            player["assists"] + player["goals"],
            player["goals"],
            -player["games"],
        ),
        reverse=True,
    )[:n]

    if not sorted_players:
        print("No players found.")
        return

    print(f"Top {n} Players by Points:")

    for player in sorted_players:
        formatted_line = f"{player['name']:<22}{player['team'][-3:]:<8}{player['assists']:<8} + {player['goals']:<5} = {player['assists'] + player['goals']:<5}"
        print(formatted_line)


def list_top_players_by_goals(data, n):
    n = int(n)

    sorted_players = sorted(  # sorting first by goals, then the least games played
        data,
        key=lambda player: (player["goals"], player["games"]),
        reverse=True,
    )[:n]

    if not sorted_players:
        print("No players found.")
        return

    print(f"Top {n} Players by Points:")

    for player in sorted_players:
        formatted_line = f"{player['name']:<22}{player['team'][-3:]:<8}{player['assists']:<8} + {player['goals']:<5} = {player['assists'] + player['goals']:<5}"
        print(formatted_line)


def list_team_players_by_points(data, team):
    team_players = [player for player in data if player["team"] == team]
    list_top_players_by_points(team_players, len(team_players))


def list_country_players_by_points(data, country):
    country_players = [player for player in data if player["nationality"] == country]
    list_top_players_by_points(country_players, len(country_players))


def list_team_abbreviations(data):
    team_abbreviations = sorted(set(player["team"] for player in data))
    print("Team Abbreviations (Alphabetical Order):")
    for abbreviation in team_abbreviations:
        print(abbreviation)


def list_country_abbreviations(data):
    country_abbreviations = sorted(set(player["nationality"] for player in data))
    print("Country Abbreviations (Alphabetical Order):")
    for abbreviation in country_abbreviations:
        print(abbreviation)


def main():
    file_name = input("Enter the name of the JSON file: ")
    data = load_data(file_name)

    if data:
        while True:
            print("\nOptions:")
            print("1. Search player by name")
            print("2. List team abbreviations")
            print("3. List country abbreviations")
            print("4. Search players by team")
            print("5. Search players by nationality")
            print("6. Find the selected amount of player(s) with the most points")
            print("7. Find the selected amount of player(s) with the most goals")
            print("8. Rank the players in a team based on points")
            print("9. Rank the players from a country based on points")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == "1":
                player_name = input("Enter the player's name: ")
                search_player_stats(data, player_name)

            elif choice == "2":
                list_team_abbreviations(data)

            elif choice == "3":
                list_country_abbreviations(data)

            elif choice == "4":
                team_name = input("Enter team abbreviation: ")
                search_by_team(data, team_name)

            elif choice == "5":
                nationality = input("Enter country abbreviation:")
                search_by_nationality(data, nationality)

            elif choice == "6":
                n = input("Enter the amount of top points players you want to see:")
                list_top_players_by_points(data, n)

            elif choice == "7":
                n = input(
                    "Enter the amount of players with the most goals you want to see:"
                )
                list_top_players_by_goals(data, n)

            elif choice == "8":
                team_name = input("Enter team abbreviation: ")
                list_team_players_by_points(data, team_name)

            elif choice == "9":
                nationality = input("Enter country abbreviation:")
                list_country_players_by_points(data, nationality)

            elif choice == "10":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
