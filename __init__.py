import random

number = random.randint(1, 999999)

for i in range(1,9999999): 
    if number > 99999:
        print(number)
        break
    
lotto = input("Lotto 3 : ")
lastlotto = random.randint(0,10)
print(lotto*10+lastlotto)

lotto2 = input("Lotto 4 : ")
lastlotto2 = random.randint(0,10)
print(lotto2*10+lastlotto2)

lotto3 = input("Lotto 1 : ")
lastlotto3 = random.randint(0,10)
print(lotto3*10+lastlotto3)


