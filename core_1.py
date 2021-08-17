# Main program

from Core import packs
from Core import totaux


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


somme = list(totaux.values())
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm']
pays = dict()
for idx in range(len(letters)):
    pays[letters[idx]] = truncate((somme[idx]/52), 2)
print(packs)
print(totaux)
print(pays)

pack_numbers = list(packs.keys())
interests = list(pays.values())
starting_pack = input("Enter the pack number you would like to start with: ")
pack_chosen = ''
for idx in range(len(pack_numbers)):
    if idx == int(starting_pack):
        cash = interests[idx-1]
        pack_chosen = pack_numbers[idx - 1]
        print(f"\nYou chose {pack_chosen}.")
        print(cash)

print(pack_numbers)
