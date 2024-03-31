from tkinter import END

# from main import *

# Just creating a default dictionary with random players
players = {
    "QB": [
        "Daniel Jones",
        "Dak Prescott",
        "Jalen Hurts",
        "Jacoby Brisset"
    ],

    "RB": [
        "Devin Singletary",
        "Saquan Barkley",
        "Austin Ekler",
        "Tony Pollard"
    ],

    "TE": [
        "Darren Waller",
        "Jake Ferguson",
        "Logan Thomas",
        "Dallas Goedert"
    ],

    "WR": [
        "Darius Slayton",
        "Wandale Moore",
        "Ceedee Lamb",
        "Brandin Cooks",
        "Terry McLaurin",
        "Jahon Dotson",
        "AJ Brown",
        "Devonta Smith"
    ],

    "DEF": [
        "Giants",
        "Cowboys",
        "Commanders",
        "Eagles"
    ]
}
# Creating a dictionary for the user team that drafted the players according to the position of the player
user_players = {
    "QB": "",
    "RB": "",
    "TE": "",
    "WR": "",
    "DEF": ""
}


# Creating functionality of a player being drafted to the empty dictionary of the users team
def drafted_player(listbox, user_listbox, user_players):
    # Checking if a player is selected
    if listbox.curselection():
        # Getting the index of the selected player
        index = listbox.curselection()[0]
        # Getting the slected players name
        player_entry = listbox.get(index)
        # format the string by splitting it
        position, player_name = player_entry.split(': ')
        # Removing the player from the listbox and add to the user_listbox
        listbox.delete(index)

        # Directly assign the player_name to the position key in user_players,
        # It will overwrite any existing entry.
        user_players[position] = player_name

        # Adding the player to the user_players dictionary
        #update the user_listbox to reflect the change, Finding the index for the position of user_listbox
        for i in range(user_listbox.size()):
            if user_listbox.get(i).startswith(position):
                # updating the entry with the new player
                user_listbox.delete(i)
                user_listbox.insert(i, f"{position}: {player_name}")
                break


# Need a function to update both list boxes when a player is chosen to be drafted
def update_listboxes(listbox, selected_position, players_data):
    listbox.delete(0, END)  # Clearing the existing entries
    for player in players_data.get(selected_position, []):
        listbox.insert(END, f"{selected_position}: {player}")  # Inserting the players for the position chosen
