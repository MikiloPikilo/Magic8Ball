import random

name = input("What is your name? ")
question = input("What is your question? ")
answer = " "

random_number = random.randint(1,9)

print(name, "Asks:", question)

if random_number == 1:
  print("Magic 8-Ball's Anser: " + "Yes-Definitly")
elif random_number == 2:
  print("Magic 8-Ball's Anser: " + "It is decidedly so.")
elif random_number == 3:
  print("Magic 8-Ball's Anser: " + "Without a doubt.")
elif random_number == 4:
  print("Magic 8-Ball's Anser: " + "Reply hazy, try again.")
elif random_number == 5:
  print("Magic 8-Ball's Anser: " + "Ask again later.")
elif random_number == 6:
  print("Magic 8-Ball's Anser: " + "Better not tell you now.")
elif random_number == 7:
  print("Magic 8-Ball's Anser: " + "My sources say no.")
elif random_number == 8:
  print("Magic 8-Ball's Anser: " + "Outlook not so good.")
elif random_number == 9:
  print("Magic 8-Ball's Anser: " + "Very doubtful.")
else:
  answer == "error"
