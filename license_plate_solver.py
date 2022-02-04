#this program will take an input of three letters and return all English words which contain those three letters in the order they appear with any characters in between them

from nltk.corpus import words
word_list = words.words()
#word_list = ["mantlepiece", "orange", "milper", "marlamipacious", "miller", "mountain", "demand"]
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"

word_list_one = []
word_list_two = []
final_word_list = []

def check_plate_letters(plate):
    if len(plate) == 3:
        for letter in plate:
            if letter not in capital_letters and letter not in lower_letters:
                return False
        return True
    else:
        return False
        

plate_letters = input("Enter your three license plate letters: ")

while not check_plate_letters(plate_letters):
    plate_letters = input("Your input does not match the expected format. Please try again: ")

plate_letters_lowered = plate_letters.lower()
letter_one = plate_letters_lowered[0]
letter_two = plate_letters_lowered[1]
letter_three = plate_letters_lowered[2]



#adds words which contain letter_one to word_list_one
for word in word_list:
    if letter_one in word:
        word_list_one.append(word)

#adds words from word_list_one which have letter_two after letter_one to word_list_two
for word in word_list_one:
    word_after_first = word[word.find(letter_one)+1:]
    if letter_two in word_after_first:
        word_list_two.append(word)

#adds words from word_list_two which have letter_three after letter_two to word_list_two
for word in word_list_two:
    word_after_first = word[word.find(letter_one)+1:]
    word_after_second = word_after_first[word_after_first.find(letter_two)+1:]
    if letter_three in word_after_second:
        final_word_list.append(word)


for word in final_word_list:
    if word[0] in capital_letters:
        final_word_list.remove(word)


final_word_list.sort()
final_word_list.sort(key=len)
final_word_string = ""
for word in final_word_list:
    final_word_string += str(word) + " "

try:
    winning_word = final_word_list[0]
    print("The best winning word is " + winning_word)
    print("Here are the other words which match this license plate: " + final_word_string)
except:
    print("There are no words to match this license plate")
