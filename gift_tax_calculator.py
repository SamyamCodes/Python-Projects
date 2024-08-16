'''
Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

When the gift is received from a close relative or a family member, 
the amount of tax to be paid is determined by the following table, 

Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
5 000 — 25 000	        100	                8
25 000 — 55 000	        1 700	            10
55 000 — 200 000	    4 700	            12
200 000 — 1 000 000	    22 100	            15
1 000 000 —         	142 100	            17
'''
# Write your solution here
gift = int(input("Value of gift:"))
if (gift < 5000):
    print("No tax!")
elif(gift >=5000 and gift < 25000):
    amount = 100 + ((gift - 5000)*0.08)
    print(f"Amount of tax: {amount} euros")

elif(gift >= 25000 and gift < 55000):
    amount = 1700 + ((gift - 25000)*0.10)
    print(f"Amount of tax: {amount} euros")

elif(gift >=55000 and gift < 200000):
    amount = 4700 + ((gift - 55000)*0.12)
    print(f"Amount of tax: {amount} euros")

elif(gift >=200000 and gift < 1000000):
    amount = 22100 + ((gift - 200000)*0.15)
    print(f"Amount of tax: {amount} euros")
    
elif(gift >=1000000 ):
    amount = 142100 + ((gift - 1000000)*0.17)
    print(f"Amount of tax: {amount} euros")
    
    

