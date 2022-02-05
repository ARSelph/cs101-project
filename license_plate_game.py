import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
# num_players = input("How many people are playing?")

license_plate = ""
for n in range(3):
    added_letter = lower_letters[random.randrange(26)]
    license_plate += added_letter

print(license_plate)




