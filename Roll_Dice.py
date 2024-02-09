import random
min = 1
max = 6

roll = input("How many dices would you like to roll? Max 3")

if roll == "1" or roll == "one" or roll == "en" :
    print ("Rolling the dice...")
    print ("The value is....")
    print (random.randint(min, max))
    
    roll_again1 = (input("Roll the dice again?"))

    while roll_again1 == "yes" or roll_again1 == "y" or roll_again1 == "ja":
        print ("Rolling the dice...")
        print ("The value is....")
        print (random.randint(min, max))
        roll_again1 == (input("Roll the dice again?"))

    if roll_again1 == "no" or roll_again1 == "nei" :
        print ("Goodbye")   
  
if roll == "2" or roll == "two" or roll == "to" :
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    
    roll_again2 = (input("Roll the dices again?"))

    while roll_again2 == "yes" or roll_again2 == "y" or roll_again2 == "ja":
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(min, max))
        print (random.randint(min, max))
        roll_again2 = (input("Roll the dices again?"))

    if roll_again2 == "no" or roll_again2 == "nei" : 
        print ("Goodbye")
        
if roll == "3" or roll == "three" or roll == "tre" :
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    print (random.randint(min, max))
    
    roll_again3 = (input("Roll the dices again?"))

    while roll_again3 == "yes" or roll_again3 == "y" or roll_again3 == "ja":
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(min, max))
        print (random.randint(min, max))
        print (random.randint(min, max))
        roll_again3 = (input("Roll the dices again?"))

    if roll_again3 == "no" or roll_again3 == "nei" : 
        print ("Goodbye")