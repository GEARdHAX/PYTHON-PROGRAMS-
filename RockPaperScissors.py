import random

moves = [1, 2, 3]
tries = int(input(" ENTER TRIES : "))
your_points = 0
bot_points = 0

while tries > 0:
    print(" TRIES LEFT : ", tries)
    tries -= 1
    user_choice = int(input('''
    1 . Rock
    2. Paper
    3. Scissors => '''))
    if tries == 0:
        print("No More Try Left :(")
    chance = random.choice(moves)
    # print(chance, '<========DEMO=======>')
    if user_choice == chance:
        print('It"s a Tie 🔵')
        print("  ")
        continue
    elif (user_choice == 1 and chance == 3) or (user_choice == 2 and chance == 1) or (user_choice == 3 and chance == 2):
        print("You Win! 🟢")
        your_points +=1
        print("Your Poins : ",your_points)
        print(" ")
        continue
    elif user_choice not in moves:
        print(" Enter valid moves 🟡")
        print(" ")
        continue
    else:
        print("You Lose ❌, Try Again. ")
        bot_points +=1
        print("Bot Poins : ",bot_points)
        print(" ")
        continue
if your_points>bot_points:
    print("You Win! 💯", " Your Poins : ",your_points)
elif your_points==bot_points:
    print("It's a Tie ⚪")
else:
    print("You Lose! 💥", "Bot_points = ",bot_points)