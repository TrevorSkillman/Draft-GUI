from tkinter import *
from players import *

window = Tk()
window.title("Draft Practice")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)
radio_positions = StringVar(value="QB")

# Grid columns https://www.pythontutorial.net/tkinter/tkinter-grid/
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)

# Grid Rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

# Creating label above the list box of players
player_label = Label(text="Player List")
player_label.grid(column=0, row=1, sticky="nsew")
# Creating a label to go above the list box of users drafted players
user_label = Label(text="Drafted Players")
user_label.grid(column=4, row=1, sticky="nsew")

# Creating a button to draft the chosen player
draft_player = Button(window, text="Draft Chosen Player")
# Using 'columnspan' to ensure it expands across multiple columns to help center the button
draft_player.grid(column=1, row=2, columnspan=3, sticky="ew")

# Creating Radio buttons for each position being drafted and each position selected
qb_radio = Radiobutton(text="QB", variable=radio_positions, value="QB", command=lambda: update_listboxes())
qb_radio.grid(column=0, row=4)

rb_radio = Radiobutton(text="RB", variable=radio_positions, value="RB", command=lambda: update_listboxes())
rb_radio.grid(column=1, row=4)

wr_radio = Radiobutton(text="WR", variable=radio_positions, value="WR", command=lambda: update_listboxes())
wr_radio.grid(column=2, row=4)

te_radio = Radiobutton(text="TE", variable=radio_positions, value="TE", command=lambda: update_listboxes())
te_radio.grid(column=3, row=4)

def_radio = Radiobutton(text="DEF", variable=radio_positions, value="DEF", command=lambda: update_listboxes())
def_radio.grid(column=4, row=4)

# List box
listbox = Listbox(window, width=10)
listbox.grid(column=0, row=2, sticky="nsew")
# The i being the players name and value being the position
for i, value in players.items():
    listbox.insert(END, f"{i}: {value}")

# Create another List box for the players that were drafted to the users team
user_listbox = Listbox(window, width=10)
user_listbox.grid(column=4, row=2, sticky="nsew")
# the _ being the flag for the positions to be displayed
for _ in user_players:
    user_listbox.insert(END, f"{_}:")


def update_listboxes():
    listbox.delete(0, END)  # Clearing the existing entries
    position = radio_positions.get()  # GETTING THE SELECTED POSITION (QB, RB, WR, TE, K)
    for player in players.get(position, []):
        listbox.insert(END, player) # Inserting the players for the position chosen


update_listboxes()
window.mainloop()
