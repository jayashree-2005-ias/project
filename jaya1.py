import random
secret_number = random.randint(1,10)
num=int(input("enter a number:"))
while True:
    if num ==secret_number:
        print("play game")
        break
    elif num >=secret_number:
        print("the number is high")
        break
    elif num <=secret_number:
        print("the number is low")