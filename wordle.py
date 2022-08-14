import random

print("The Game Wordle Is Not Case Sensitive")


def to_start(start):

    if start == "WORDLE":
        print(f"Hello User! Welcome To Wordle! Wordle Is a Really Easy Game. "
              "You'll Get 5 chances To Get The Matching Letters From The Generated Word. " 
              "Finally You Just Have To Guess The Word With The Matching Letters. ")

        def difficulty_level(difficulty):
            new_word = ''
            if difficulty == "NOOB":
                print ("You've Selected The First Difficulty Level. ")
                three_letter_dic = ['INK', 'PET', 'RUB', 'SIT', 'TAG', 'URN', 'VAN', 'WAR', 'YES', 'ZIP']
                new_word += random.choice(three_letter_dic)
                temp = []
                for i in range(1, 6):
                    user_input = input(f"Word number {i}. here: ").upper()
                    temp.append(user_input)
                string1 = ''
                final = []
                for k in temp:
                    string1 += k
                for check in string1:
                    if check in new_word:
                        final.append(check)

                print(final)
                user_input2 = input("Enter The final word here: ").upper()
                if user_input2 == new_word:
                    print("Congratulations! You Won. ")
                else:
                    print(f"The answer is {new_word}")
                    print("Nice Try! ;>). Better Luck Next Time!")
                #print(new_word)

            elif difficulty == "PRO":
                print ("You've Selected The Second Difficulty Level. ")
                four_letter_dic = ['ALSO', 'ABLE', 'BLUE', 'BIRD', 'BILL', 'CALL', 'CALM', 'COOL', 'DOLL']
                new_word += random.choice(four_letter_dic)
                temp = []
                for i in range(1, 6):
                    user_input = input(f"Word number {i}. here: ").upper()
                    temp.append(user_input)
                string1 = ''
                final = []
                for k in temp:
                    string1 += k
                for check in string1:
                    if check in new_word:
                        final.append(check)

                print(final)
                user_input2 = input("Enter The final word here: ").upper()
                if user_input2 == new_word:
                    print("Congratulations! You Won. ")
                else:
                    print(f"The answer is {new_word}")
                    print("Nice Try! ;>). Better Luck Next Time!")

                #print(new_word)
            elif difficulty == "WORDLORD":
                print("You've Selected The Third Difficulty Level")
                five_letter_dic = ['ENTER', 'FAITH', 'FIBER', 'BUILD', 'BRUTE', 'BREAD', 'BUNNY']
                new_word += random.choice(five_letter_dic)
                temp = []
                for i in range(1, 6):
                    user_input = input(f"Word number {i}. here: ").upper()
                    temp.append(user_input)
                string1 = ''
                final = []
                for k in temp:
                    string1 += k
                for check in string1:
                    if check in new_word:
                        final.append(check)

                print(final)
                user_input2 = input("Enter The final word here: ").upper()
                if user_input2 == new_word:
                    print("Congratulations! You Won. ")
                else:
                    print(f"The answer is {new_word}.")
                    print("Nice Try! ;>). Better Luck Next Time!")

                #print(new_word)
            else:
                print("Such Difficulty Doesn't Exist")

        difficulty_level(input(f"There are three difficulty levels in this game. 1. NOOB 2. PRO. 3. WORDLORD . "
                               f" Enter the difficulty level here: ").upper())

    else:
        print("Sorry Wrong Input. ")


to_start(input("Press 'WORDLE' to enter the game:  ").upper())
