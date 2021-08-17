from Core import *


balance = 0
total_invested = 0
your_packs = list()


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def adjust_balance(value):
    """Adjust the balance value each time a payment is made."""
    global balance
    balance = int(value)
    return balance


# This function get the pack chosen by the user.
def get_initial_pack(nbr):
    """get the initial investment pack"""
    try:
        nbr = int(nbr)
    except ValueError:
        print(f"{nbr} is not a valid entry. Please enter an integer (example:6).")
    else:
        for idx in range(len(packs_list)):
            if idx == int(nbr) - 1:
                pack_chosen = packs_list[idx]
                balance_value = interest[idx]
                adjust_balance(balance_value)
                print(f'You chose {pack_chosen}.')
                return pack_chosen


# This function buys packs
def buy_pack(x):
    """Buy the highest pack with the available balance"""
    for package, amount in packs_0.items():
        while x - amount >= 0:
            your_packs.append(package)
            amount_added = 0
            amount_added += amount
            print(f"You bough {package} : ${amount}!")
            plus = amount_added
            return plus


while balance >= 0:
    added = buy_pack(balance)
    total_invested = total_invested + added
    balance = balance - added
    print(f" Your remaining balance is: Balance = ${balance}")
    print(f"Your packs list: {your_packs}")
    print(f" Total Invested = ${total_invested}")
# This function list all packs bought


def list_pack_bought():
    """Displays all packs bought"""
