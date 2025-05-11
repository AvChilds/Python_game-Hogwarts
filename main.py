
"""The following app represents the first level of a Hogwarts game where users can
build a wizard identity
"""

import requests
import time #time module - delay text appearing for better user experience
import random

print ("-------------------------------------------")
print ("Welcome to the Wizarding World of Hogwarts!")
print ("*******************************************")

print("""\nHere you will adventure into a magical world where you can create your very own wizard identity!\n
In this first level, you will get to: 
- create your very own wizard name,
- jump onto the Hogwarts Express and meet your best Wizard friend,
- learn your first spell.
""")

#creating new file and contents for new user
with open('new_wizard.txt', 'w+') as file:
    file.write("Here is a summary of your new wizard details:\n")

print ("Now let's give you a wizard name.\n")
# Creating username based on user's input
def create_name():
    name = input("What is your first name? ")
    fruit = input("What is your favourite fruit? ")
    colour = input ("What is your favourite colour? ")
    name_slice = name[:2]
    fruit_slice = fruit[:3]
    username = (name_slice + fruit_slice + colour).capitalize() #to make first letter upper caps
    print(f"\nYour new wizard name is {username}!")
    return username

#Using while loop, boolean and if statements - allows function to be repeated if user decides to retry this element.

keep_name = False

while keep_name == False:
    username = create_name()
    recall = input("Would you like to try a new name? (yes or no): ").lower()
    if recall == "no":
        keep_name = True
        print(f"\nWelcome {username}! Come on board the Hogwarts Express!")
        with open("new_wizard.txt",'a+') as file:   #saving new username in txt file
            file.write(f"Your wizard name is {username}.\n")
    elif recall == "yes":
        keep_name = False
    elif recall != "yes" or "no":
        print("Answer not recognised. Please try again. ")
        keep_name = False


time.sleep(1.0)

#Random selection of Hogwarts Carriage by simulating a dice roll - random chance pick of numbers 1 to 6

def random_carriage():
    print("""\nYou now need to roll the dice to select which carriage you are getting on. 
Whichever carriage you enter will determine a new friend you will make.""")
    print(input("\nPlease press ENTER to roll the dice - "))
    dice_roll= random.randint(1, 6)
    print ("Your dice is now rolling! ...")
    time.sleep(1.0)
    print ("Wait for it ...")
    time.sleep(1.0)
    print(f"You are getting on Carriage No.{dice_roll}!")
    return dice_roll

roll_result = random_carriage()

time.sleep(1.5)

#retrieving data from Harry Potter Api to extract data of specific student characters
def get_students():
    students_endpoint = 'https://hp-api.onrender.com/api/characters/students'
    students_response = requests.get(students_endpoint)
    students_data = students_response.json()
    return students_data

def character_bio(i):
    print("\nYou have made a new friend who will now become your best friend: ")
    char_spec = get_students()[i]
    char_dict = {'Name: ': char_spec['name'],
         'Date of Birth: ': char_spec['dateOfBirth'],
         'House: ': char_spec['house'],
         'Patronus: ' : char_spec['patronus'],
         }
    for key, value in char_dict.items():
        print(key,value)
    return char_dict


def friend_name(i):
    friend_fullname = get_students()[i]['name']
    with open("new_wizard.txt", 'a+') as friend_file:
        friend_file.write(f"Your best friend is {friend_fullname}.\n")  #saving full name result into .txt file
    friend_firstname = friend_fullname.split()[0]  #extracting only first name
    time.sleep(2.0)
    print(f"\n{friend_firstname} will now show you a new spell!\n")
    return friend_firstname


def new_friend():
    char_list = [0, 1, 2, 6, 7, 8]
    i = roll_result-1
    character_bio (char_list[i])
    friend_name(char_list[i])


new_friend()

#User learning new spell
#get spells data from Harry Potter Api

spells_endpoint = 'https://hp-api.onrender.com/api/spells'
spells_response = requests.get(spells_endpoint)
spells_list = spells_response.json()

#to find index of spell with the api list of spell to retrieve the description of the spell
def find_spell(spells_list, name):
    count = None
    for index, spell in enumerate(spells_list): #use the enumerate function to iterate over the list to find index
        if spell['name'] == name:
            count = index
    return count

#create list of spells for user to choose from
def learn_spell():
    print("These are basic spells you can learn:")
    selected_spells = ["Accio", "Expelliarmus", "Wingardium Leviosa"]
    for i, spell in enumerate(selected_spells):  #iterating and count over list
        spell_num = i + 1
        print ( f"{spell_num}. {spell}")

    spell_choice = int(input("Enter the number of the spell you wish to learn: "))

    if  spell_choice > 3 :
        print("\nThis number is invalid, please try again.")
        learn_spell()
    else:
        list_index = spell_choice -1
        name = selected_spells[list_index]

        spell_index = find_spell(spells_list, name)  #calling the function find_spell() from earlier
        spell_name = spells_list[spell_index]['name']
        spell_description = spells_list[spell_index]['description']
        print (f'\n{spell_name}: {spell_description}\n')
        with open("new_wizard.txt", 'a+') as spell_file:
            spell_file.write(f"Your first spell is {spell_name}.\n")

learn_spell()

print(input("Congratulations! You have now arrived at Hogwarts.\n"
            "You have completed Level 1."))

#End of assignment-2-python. Thank you participating.