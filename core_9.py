import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyinputplus import *
plt.rcParams['axes.facecolor'] = 'aquamarine'


class Package:
    """This is a representation of a package."""

    __slots__ = ['pack_nbr', 'pack_name', 'pack_value', 'pack_roi', 'pack_monthly_roi', 'pack_weekly_roi', 'pack_life']

    def __init__(self, pack_nbr, pack_name, pack_value, pack_roi, pack_monthly_roi, pack_weekly_roi, pack_life):
        # self.pack_id = pack_id
        self.pack_nbr = pack_nbr
        self.pack_name = pack_name
        self.pack_value = pack_value
        self.pack_roi = pack_roi
        self.pack_monthly_roi = pack_monthly_roi
        self.pack_weekly_roi = pack_weekly_roi
        self.pack_life = pack_life

    def __repr__(self):
        package = f"Pack number: {self.pack_nbr}, Pack name: {self.pack_name}, Pack value: ${self.pack_value}," \
                  f" Pack yearly ROI: ${self.pack_roi}, Pack monthly ROI: ${self.pack_monthly_roi}," \
                  f" Pack weekly ROI: ${self.pack_weekly_roi}, Pack life: {self.pack_life} weeks."
        return package

    @property
    def get_p_nbr(self):
        return self.pack_nbr

    @property
    def get_p_name(self):
        return self.pack_name

    @property
    def get_p_value(self):
        return self.pack_value

    @property
    def get_p_roi(self):
        return self.pack_roi

    @property
    def get_p_m_roi(self):
        return self.pack_monthly_roi

    @property
    def get_p_w_roi(self):
        return self.pack_weekly_roi

    @property
    def get_p_life(self):
        return self.pack_life

    def p_life_down_counter(self, life):
        self.pack_life -= life
        print(f'The remaining life for this pack is: {self.pack_life} weeks.')


P_list = {
    'pack_01': ('Porto-Novo', 200, 204, 17, 3.92, 52),
    'pack_02': ('Libreville', 400, 432, 36, 8.3, 52),
    'pack_03': ('Ndjamena', 800, 912, 76, 17.5, 52),
    'pack_04': ('Malabo', 1600, 1920, 160, 36.9, 52),
    'pack_05': ('Yaounde', 3200, 3936, 328, 76, 52),
    'pack_06': ('Pretoria', 6400, 8064, 672, 155, 52),
    'pack_07': ('Le Caire', 12_800, 16_512, 1376, 317.5, 52),
    'pack_08': ('Abuja', 25_600, 33_792, 2816, 649.9, 52),
    'pack_09': ('Dubai', 51_200, 68_608, 5717.3, 1319.4, 52),
    'pack_10': ('Ouaga', 100_000, 135_000, 11_250, 2596, 52),
    'pack_11': ('Yamoussoukro', 500_000, 680_000, 56_667, 13_077, 52),
    'pack_12': ('Bayiha Bernard', 1_000_000, 1_370_000, 114_167, 26_346.1, 52)}

P_list_ = list(P_list.keys())

packs = []
for k_, v in P_list.items():  # Generate a list of available stacking package.
    packs.append(Package(k_, *v))


my_packs = {P_list['pack_01'][0]: [], P_list['pack_02'][0]: [], P_list['pack_03'][0]: [], P_list['pack_04'][0]: [],
            P_list['pack_05'][0]: [], P_list['pack_06'][0]: [], P_list['pack_07'][0]: [], P_list['pack_08'][0]: [],
            P_list['pack_09'][0]: [], P_list['pack_10'][0]: [], P_list['pack_11'][0]: [], P_list['pack_12'][0]: []}

df = pd.DataFrame(columns=['Weeks', P_list['pack_01'][0], P_list['pack_02'][0], P_list['pack_03'][0],
                           P_list['pack_04'][0], P_list['pack_05'][0], P_list['pack_06'][0], P_list['pack_07'][0],
                           P_list['pack_08'][0], P_list['pack_09'][0], P_list['pack_10'][0], P_list['pack_11'][0],
                           P_list['pack_12'][0], 'Cash'])
cash = 0
total_payments = 0
total_withdraw = 0
total_nbr_of_pack = 0
capital_invested = 0
withdraw_count = 0
funding_decision = True
total_wkly_pay = []


# nbr_of_pack =


def cash_adjustment(b):
    """This function take in the value of a pack and subtract it from the cash balance when a pack is bought"""
    global cash
    cash -= b
    print(f'Your new balance is: ${cash}')


def congratulation(a, p):
    """This function print a congratulation message, and displays a set of every pack bought and their quantity."""

    print(f" Congratulation!!! You just bought {a}.")
    x = p.keys()
    s = p.values()
    d = list()
    for i in s:
        d.append(len(i))  # Append the length of the list values from the dictionary passed to the function to d.
    r = zip(x, d)
    global total_nbr_of_pack
    total_nbr_of_pack = sum(d)

    print(f"Here is the list of the packs you possess so far: {set(r)}")


def buy_packs(value):
    """This function buy the highest pack with the available cash = value"""
    if value < 200:
        pass
    else:
        global total_nbr_of_pack
        while value >= 200:
            if value >= 1_000_000:
                pack12 = Package(P_list_[-1], *P_list['pack_12'])
                my_packs["Bayiha Bernard"].append(pack12)
                congratulation(pack12.__repr__(), my_packs)
                cash_adjustment(pack12.get_p_value)
                value -= pack12.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue
            elif 1_000_000 > value >= 500_000:
                pack11 = Package(P_list_[-2], *P_list['pack_11'])
                my_packs["Yamoussoukro"].append(pack11)
                congratulation(pack11.__repr__(), my_packs)
                cash_adjustment(pack11.get_p_value)
                value -= pack11.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue
            elif 500_000 > value >= 100_000:
                pack10 = Package(P_list_[-3], *P_list['pack_10'])
                my_packs["Ouaga"].append(pack10)
                congratulation(pack10.__repr__(), my_packs)
                cash_adjustment(pack10.get_p_value)
                value -= pack10.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 100_000 > value >= 51_200:
                pack09 = Package(P_list_[-4], *P_list['pack_09'])
                my_packs["Dubai"].append(pack09)
                congratulation(pack09.__repr__(), my_packs)
                cash_adjustment(pack09.get_p_value)
                value -= pack09.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 51_200 > value >= 25_600:
                pack08 = Package(P_list_[-5], *P_list['pack_08'])
                my_packs["Abuja"].append(pack08)
                congratulation(pack08.__repr__(), my_packs)
                cash_adjustment(pack08.get_p_value)
                value -= pack08.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 25_600 > value >= 12_800:
                pack07 = Package(P_list_[-6], *P_list['pack_07'])
                my_packs["Le Caire"].append(pack07)
                congratulation(pack07.__repr__(), my_packs)
                cash_adjustment(pack07.get_p_value)
                value -= pack07.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 12_800 > value >= 6_400:
                pack06 = Package(P_list_[-7], *P_list['pack_06'])
                my_packs["Pretoria"].append(pack06)
                congratulation(pack06.__repr__(), my_packs)
                cash_adjustment(pack06.get_p_value)
                value -= pack06.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 6_400 > value >= 3_200:
                pack05 = Package(P_list_[-8], *P_list['pack_05'])
                my_packs["Yaounde"].append(pack05)
                congratulation(pack05.__repr__(), my_packs)
                cash_adjustment(pack05.get_p_value)
                value -= pack05.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 3_200 > value >= 1_600:
                pack04 = Package(P_list_[-9], *P_list['pack_04'])
                my_packs["Malabo"].append(pack04)
                congratulation(pack04.__repr__(), my_packs)
                cash_adjustment(pack04.get_p_value)
                value -= pack04.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 1_600 > value >= 800:
                pack03 = Package(P_list_[-10], *P_list['pack_03'])
                my_packs["Ndjamena"].append(pack03)
                congratulation(pack03.__repr__(), my_packs)
                cash_adjustment(pack03.get_p_value)
                value -= pack03.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            elif 800 > value >= 400:
                pack02 = Package(P_list_[-11], *P_list['pack_02'])
                my_packs["Libreville"].append(pack02)
                congratulation(pack02.__repr__(), my_packs)
                cash_adjustment(pack02.get_p_value)
                value -= pack02.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")
                continue

            else:
                pack01 = Package(P_list_[0], *P_list['pack_01'])
                my_packs["Porto-Novo"].append(pack01)
                congratulation(pack01.__repr__(), my_packs)
                cash_adjustment(pack01.get_p_value)
                value -= pack01.get_p_value
                print(f"You now have {total_nbr_of_pack} active packs!")


def get_pack(value):
    if value < 200:
        global funding_decision, cash, capital_invested
        while funding_decision:
            print("You don't have enough money yet to buy a pack!\n"
                  " Fund your account, or continue without additional funds. ")
            print("(1) Add fund to my account.\n"
                  "(2) Continue without funding.\n"
                  "(3) Do not ask again.\n"
                  "(4) Exit simulation")
            decision = inputNum('> ')
            if decision == 4:
                sys.exit()
            elif decision == 3:
                funding_decision = False
            elif decision == 2:
                break
            elif decision == 1:
                print("How much do you want to fund?")
                print(f"The minimum amount needed to buy a pack right now is ${200 - cash}.")
                while True:
                    fund = inputNum()
                    if fund <= 0:
                        print("Enter a value greater than 0.")
                        continue
                    else:
                        cash += fund
                        buy_packs(cash)
                        capital_invested += fund
                        break

            else:
                print(f"{decision} is not a valid entry. Chose from 1 to 4.")
                continue
    else:
        buy_packs(value)


def get_paid(a_dict):
    """This function pays the user the corresponding amount
    of any pack bough. The function takes in a dictionary containing a list of packages. """
    t_0 = 0
    for p, packs_ in a_dict.items():
        if not packs_:
            pass
    else:
        global cash, total_payments, total_nbr_of_pack, total_wkly_pay
        for p, packs_ in a_dict.items():
            for pack in reversed(packs_):
                cash += pack.get_p_w_roi
                t_0 += pack.get_p_w_roi
                total_payments += pack.get_p_w_roi
                print(f"Great news!!! You just earned the amount of: ${pack.get_p_w_roi}"
                      f"\nYour new Balance is: ${cash}.")
                pack.p_life_down_counter(1)
                if pack.get_p_life > 0:
                    continue
                else:
                    print(f"The life span of the pack: {p}: {packs_.index(pack)} has expired; "
                          f"therefore, is no longer active and has been removed.")
                    packs_.remove(pack)
                    total_nbr_of_pack -= 1
                    print(f"You now have {total_nbr_of_pack} active packs remaining!")
        total_wkly_pay.append(t_0)


def make_withdraw(frequency, withdraw_amount, w_e):
    """This function operates withdraws according to the frequency, and the amount provided by the user;
    w_e represent the number of weeks elapsed. The function also count the number of withdrawals made"""

    global cash, total_withdraw, withdraw_count
    if frequency != 0 and w_e % frequency == 0 and cash >= withdraw_amount:
        cash -= withdraw_amount
        total_withdraw += withdraw_amount
        withdraw_count += 1

        print(f"Hooray!!! A withdraw of ${withdraw_amount} has been made!"
              f" You made {withdraw_count} withdraws so far, totaling ${total_withdraw}.")
        print(f"Your new balance is ${cash}.")
    else:
        pass


def reset_data():
    """This function set all globals variables of the program."""
    global df, total_payments, total_withdraw, total_nbr_of_pack, capital_invested, withdraw_count, funding_decision, \
        total_wkly_pay

    df = pd.DataFrame(columns=['Weeks', P_list['pack_01'][0], P_list['pack_02'][0], P_list['pack_03'][0],
                               P_list['pack_04'][0], P_list['pack_05'][0], P_list['pack_06'][0], P_list['pack_07'][0],
                               P_list['pack_08'][0], P_list['pack_09'][0], P_list['pack_10'][0], P_list['pack_11'][0],
                               P_list['pack_12'][0], 'Cash'])
    total_payments = 0
    total_withdraw = 0
    total_nbr_of_pack = 0
    capital_invested = 0
    withdraw_count = 0
    funding_decision = True
    total_wkly_pay = []


def data_collection(week_nbr, data_info):
    """This function collects data generated and structures them as a Data Frame."""
    global df, cash
    df = df.append({'Weeks': int(week_nbr), P_list['pack_01'][0]: len(data_info['Porto-Novo']) * P_list['pack_01'][4],
                    P_list['pack_02'][0]: len(data_info['Libreville']) * P_list['pack_02'][4],
                    P_list['pack_03'][0]: len(data_info['Ndjamena']) * P_list['pack_03'][4],
                    P_list['pack_04'][0]: len(data_info['Malabo']) * P_list['pack_04'][4],
                    P_list['pack_05'][0]: len(data_info['Yaounde']) * P_list['pack_05'][4],
                    P_list['pack_06'][0]: len(data_info['Pretoria']) * P_list['pack_06'][4],
                    P_list['pack_07'][0]: len(data_info['Le Caire']) * P_list['pack_07'][4],
                    P_list['pack_08'][0]: len(data_info['Abuja']) * P_list['pack_08'][4],
                    P_list['pack_09'][0]: len(data_info['Dubai']) * P_list['pack_09'][4],
                    P_list['pack_10'][0]: len(data_info['Ouaga']) * P_list['pack_10'][4],
                    P_list['pack_11'][0]: len(data_info['Yamoussoukro']) * P_list['pack_11'][4],
                    P_list['pack_12'][0]: len(data_info['Bayiha Bernard']) * P_list['pack_12'][4],
                    'Cash': cash}, ignore_index=True)


def plotting(d_f):
    """This function displays custom charts."""
    col = {P_list['pack_01'][0]: ['Black', '-.'], P_list['pack_02'][0]: ['Green', '-.'],
           P_list['pack_03'][0]: ['Orange', '-.'], P_list['pack_04'][0]: ['Blue', '--'],
           P_list['pack_05'][0]: ['Red', '--'], P_list['pack_06'][0]: ['Purple', '--'],
           P_list['pack_07'][0]: ['Black', ':'], P_list['pack_08'][0]: ['Green', 'solid'],
           P_list['pack_09'][0]: ['Orange', '--'], P_list['pack_10'][0]: ['Blue', '-.'],
           P_list['pack_11'][0]: ['Red', '-.'], P_list['pack_12'][0]: ['Purple', '-.'],
           'Total': ['Magenta', '-'], 'Cash': ['Yellow', 'solid']}

    for p in d_f.columns:
        if p == 'Weeks':
            pass
        else:
            d_f[p].plot(x=d_f['Weeks'], c=col[p][0], ls=col[p][1], ms=7, label=p)
            plt.legend(loc='best')
    d_f.plot(x='Weeks', subplots=True, figsize=(6, 50))
    plt.show()


def simulator():
    freq = 0  # freq is the frequency of the withdraw.
    withdraw_value = 0
    for pack in packs:
        print(pack.__repr__())
    print('\n')
    print("Enter the cash amount or the value of the pack you would like to start with!")
    global cash
    while True:  # Making sure the user enter a value greater or equal to 200.
        cash = inputNum()
        if cash < 200:
            print("The minimum amount is $200.")
            continue
        else:
            break

    print("Enter the length (IN YEARS) of the investment simulation you would like to run.")
    while True:  # Making sure the user enter a value greater or equal to 1.
        length_in_years = inputNum()
        if length_in_years < 1:
            print("The minimum investment year is 1.")
            continue
        else:
            break

    invest_length = int(length_in_years) * 52

    while True:
        print("Would you be making withdrawals? Y/N")
        response = input('> ')
        if response.lower() == 'n' or response.lower() == 'no':
            freq = 0
            break
        elif response.lower() == 'y' or response.lower() == 'yes':
            print("Enter the amount you would like to periodically withdraw.")
            while True:  # Making sure the user enter a positive value.
                withdraw_value = inputNum()
                if withdraw_value < 0:
                    print("The withdraw amount must be greater than 0!")
                    continue
                else:
                    break

            while True:
                print("Enter the frequency of your withdraw.\n"
                      "(1) Weekly.\n"
                      "(2) Biweekly.\n"
                      "(3) Monthly.\n"
                      "(4) Quarterly.\n"
                      "(5) Semi annually.\n"
                      "(6) Annually.\n"
                      "(7) Randomly.")

                message = inputNum('> ')  # Setup the withdrawal frequency.
                if message == 1:
                    freq = 1
                    break
                elif message == 2:
                    freq = 2
                    break
                elif message == 3:
                    freq = 4
                    break
                elif message == 4:
                    freq = 12
                    break
                elif message == 5:
                    freq = 24
                    break
                elif message == 6:
                    freq = 52
                    break
                elif message == 7:
                    freq = random.randint(1, 52)
                    break
                else:
                    print(
                        f"{message} is not a valid option. Chose from 1 to 7.")
                    continue
            break

        else:
            print(f"{response} is not a valid entry. Enter Y/N")
            continue

    while True:  # This is the main loop.
        # Buys packs with the cash provided:
        get_pack(cash)
        for k in range(invest_length):
            print(f'Week {k + 1}:')
            get_paid(my_packs)
            make_withdraw(freq, withdraw_value, k + 1)
            get_pack(cash)
            data_collection(k + 1, my_packs)
            print(f"Your Balance is: ${cash}\n")

        o = invest_length + 1
        for p_element in reversed(my_packs.values()):
            while p_element:
                print(f" Week {o}:")
                get_paid(my_packs)
                print(f"Your total payments is: {total_payments}")
                make_withdraw(freq, withdraw_value, o)
                data_collection(o, my_packs)
                o += 1
                print('\n')

        global df
        total = np.array(total_wkly_pay)
        df.insert(loc=13, column='Total', value=total)
        df = df.loc[:, (df != 0).any(axis=0)]
        df1 = df.set_index('Weeks')
        print(df1)
        # df.plot(x='Weeks', kind='line')
        # df.plot(x='Weeks', kind='line', subplots=True, figsize=(6, 50))
        # plt.legend(loc='best')

        print("Press 'S' to save your result as csv file, or anything else exit the simulation.")
        while True:
            dl = input('> ')
            if dl.lower() != 's':
                print('Thank you!')
                break
            else:
                df.to_csv('My_Data.csv')
                print('Thank You!')
                break
        plotting(df)
        break


def main():
    while True:
        print("""--Limo coin stacking system simulation--

           Purpose:
               This program helps the user simulate the stacking return of the Limo coin
               and displays the result. This part is the automated version.
               A manual version will be added to this program latter.""")

        print('\n')
        print("Select what you want to do:\n"
              "(1) Run a simulation.\n"
              "(2) Exit.")
        choice = inputNum('> ')
        if choice == 1:
            simulator()
            reset_data()
            continue
        elif choice == 2:
            sys.exit()
        else:
            print(f"{choice} is not a valid entry.")
            continue


# Let's run the program:
if __name__ == '__main__':
    main()
