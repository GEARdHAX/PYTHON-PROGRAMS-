import random
bot = 0
Human = 0
#points = int(input("Number of points till you wanna play? => "))
name = input("\nWelcome To Rock,Paper,Scissors! What's Your Name => ")
print('\n')
print('''1. Rock \n2. Paper \n3. Scissors''')
print('\n')
while True:
  toss = random.randrange(1,4) 
  x = int(input("ENTER CHOICE : "))
  if x!=toss:
    if bot==4:
      print('You lose!')
      print("BOT have",bot+1,'points')
      break
    bot +=1
    print("BOT points => ",bot)
  elif x==toss:
    if Human==4:
      print("You Win! You Got",Human+1,'points')
      break
    Human+=1
    print(name,'points =>',Human)