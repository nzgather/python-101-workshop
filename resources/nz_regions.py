capitals_dict = {
    'Auckland': 'Auckland',
    'Bay of Plenty': 'Whakatane',
    'Canterbury': 'Christchurch',
    'Chatham Islands': 'Waitangi',
    'Gisborne': 'Gisborne',
    'Hawke\'s Bay': 'Napier',
    'Manawatu-Wanganui': 'Palmerston North',
    'Marlborough': 'Blenheim',
    'Nelson': 'Nelson',
    'Northland': 'Whangarei',
    'Otago': 'Dunedin',
    'Southland': 'Invercargill',
    'Taranaki': 'Stratford',
    'Tasman': 'Richmond',
    'Waikato': 'Hamilton',
    'Wellington': 'Wellington',
    'West Coast': 'Greymouth',
}

import random

while True:
    region = random.choice(capitals_dict.keys())
    capital = capitals_dict[region]
    capital_guess = raw_input("What is the capital of " + region + "? ")
    if capital_guess == "Exit":
        print "Goodbye"
        break

    if capital_guess == capital:
        print "Correct! Nice job."
    else:
        print "Incorrect. The capital of " + region + " is " + capital + "."
