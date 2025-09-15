import random

n = random.randint(1,100)
Guess = -1
totalNumeberOfGuess=1

while(Guess != n):
    Guess= (int )(input("Enter the number "))
    if(Guess< n):
     print(f"you have to guess the higher than number {Guess}")
     totalNumeberOfGuess +=1
    elif(Guess> n):
      print(f"you have to guess the lower than number {Guess}")
      totalNumeberOfGuess +=1
else:
      print(f"you have guessed the number {n} correct in {totalNumeberOfGuess} Guess")
      



