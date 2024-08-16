# Write your solution here
attempts = 0

while True:
    pin = int(input("PIN:"))   #Correct pin is 4321
    attempts += 1
    if(pin == 4321 and attempts == 1):
        print("Correct! It only took you one single attempt!")
        break
    if(pin == 4321):
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")