
user_choice = input("Do you like to play the number guessing game? Type Y for yes, N for no: ").strip().upper()

if (user_choice == "Y"):
     print("                             ***Welcome to the Numeber Guessing Game***                             ")
     start_range = int(input("           Enter the starting range for the number:  "))
     end_range = int(input("           Enter the ending range for the number:  "))
   
     print(f"           You enterd the guessing range from  {start_range} to {end_range}.")

     import random
     import math

     guess_number = random.randint(start_range, end_range)
        # The minimum chance for guessing the number in the range is log base 2 of(endrange - start range + 1)
     total_chances = math.ceil(math.log(end_range - start_range + 1, 2))
     print("\n\t\t You have only", total_chances, " chances to guess the integer.")

     count = 0
     flag = False
     while  count < total_chances:
        count += 1
        user_number = int(input("           Enter your guessed number. "))
        if (guess_number == user_number):
            print("Hooray!! You guessed the number in ", count, "try.")
            flag = True
            break
        elif (guess_number > user_number):
            print("Try Again! You guessed too small.")
        elif (guess_number < user_number):
            print("Try Again! You guessed too large. ")        
     if not flag:
        print(f"\n\t\t The number is {guess_number}.")
        print("\n\t\t Better Luck Next Time!! ")   
else:
    print("Thank You for playing the game.")