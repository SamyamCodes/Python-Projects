'''

In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
The game offers one of the following hints in response to your guess: “Pico” when your guess has a 
correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, 
and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.

'''

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''' 
          
 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
   When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.
  
For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getsecretNum()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guess to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses. ")
                print(f"The answer was {secretNum}.")

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
                break
    print("Thanks for playing")

def getsecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    if guess == secretNum:
        print("You got it!")
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ =="__main__":
    main()
