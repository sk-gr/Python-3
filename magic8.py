import random

name = "Crodie"
print("Sukhi says: Crodie turn me up")

question = ("Should I turn Sukhi up?")

answer = ""

random_number = random.randint(1,9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Ask again later"
elif random_number == 5:
  answer = "Better not tell you now"
elif random_number == 6:
  answer = " Outlook not so good"
elif random_number == 7:
  answer = "Very doubtful"
else:
  answer == "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
