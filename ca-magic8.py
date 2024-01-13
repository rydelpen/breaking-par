import random
# variables name and question can have strings
name = ""
question = ""

# leave answer blank for program to run properly
answer = ""

# if/elif statement if variable name is empty
if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)


random_number = random.randint(1, 12)

# uncommented print(random_number); did not want to see it run
# print(random_number)

# added if statement when question is empty so that when program runs,
# it doesn't give an answer that is assigned to random_number.

if question == "":
    answer = "Please ask a question. I can\'t do my job without it."
elif random_number == 1:
    answer = "Yes definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Are you sure about that?"
elif random_number == 11:
    answer = "Is the sky blue?"
elif random_number == 12:
    answer = "Can pigs fly?"
else:
    answer = "Error"

print("Magic 8-Ball\'s answer: " + answer)
