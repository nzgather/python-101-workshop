capitals_dict = {
    "Auckland": "Auckland",
    "Bay of Plenty": "Whakatane",
    "Canterbury": "Christchurch",
    "Chatham Islands": "Waitangi",
    "Gisborne": "Gisborne",
    "Hawke's Bay": "Napier",
    "Manawatu-Wanganui": "Palmerston North",
    "Marlborough": "Blenheim",
    "Nelson": "Nelson",
    "Northland": "Whangarei",
    "Otago": "Dunedin",
    "Southland": "Invercargill",
    "Taranaki": "Stratford",
    "Tasman": "Richmond",
    "Waikato": "Hamilton",
    "Wellington": "Wellington",
    "West Coast": "Greymouth",
}

import random

states = capitals_dict.keys()
for i in range(5):
    region = random.choice(list(capitals_dict.keys()))
    capital = capitals_dict[region]
    capital_guess = input("What is the capital of " + region + "? ")

    if capital_guess == capital:
        print("Correct! Nice job.")
    else:
        print("Sorry, the capital of " + region + " is " + capital + ".")

print("All done")
