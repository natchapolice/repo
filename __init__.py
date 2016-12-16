import random

number = random.randint(1, 999999)

for i in range(1,9999999): 
    if number > 99999:
        print(number)
        break