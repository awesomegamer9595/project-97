import random 
print("Number guessing game") 
# randint function to generate the random number between 1 to 9 number = 
number=random.randint(1, 9)
chances=0
while chances < 5:
    guess =input("guess the number:")
    if number == int(guess):
        print("Congratulations, you win and I think I spelled it wrong lol")
        break
    else:
        print("WRONG ANSWER ")
        chances += 1
    if chances == 5:
        print("thats it,you lose so HAVE A GREAT DAY" ,"the number is ",number)
        break