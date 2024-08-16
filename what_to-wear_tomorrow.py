'''
 A program which asks for tomorrow's weather forecast and then suggests 
 weather-appropriate clothing.
The suggestion changes if the temperature (measured in degrees Celsius) is
over 20, 10 or 5 degrees,
and also if there is rain on the radar.

'''

print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain_chance = input("Will it rain (yes/no): ")

if temp > 20:
    print("Wear jeans and a T-shirt")
    if rain_chance == "yes":
        print("Don't forget your umbrella!")

elif temp == 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    if rain_chance == "yes":
        print("Don't forget your umbrella!")

elif 10 < temp < 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    if rain_chance == "yes":
        print("Don't forget your umbrella!")


elif 5 < temp <= 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    if rain_chance == "yes":
        print("Don't forget your umbrella!")

elif temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    if rain_chance == "yes":
        print("Don't forget your umbrella!")
