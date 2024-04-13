place = input("Choose a place: forest or cave? ")

if place == "forest":
    print('climb a tree!')

torch = input("you have chosen cave: light a torch or proceed in the dark? ")

if torch == "light a torch":
    print('you found hidden treasure!')
elif torch == 'proceed in the dark':
    print('you tripped and fell')
else:
    print('cross the river')