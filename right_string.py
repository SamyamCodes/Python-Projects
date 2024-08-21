'''
Please write a program which asks the user for a string and then prints it out so 
that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, 
the beginning of the line is filled in with * characters.

'''

st = input("Please type in a string:")

while True:
    if (len(st) > 20):
        break
    else:
        times_num = 20 - len(st)
        right_str = print(("*" * times_num)+st )
        break



