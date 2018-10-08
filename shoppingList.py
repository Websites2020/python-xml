#!/usr/bin/python

answer1 = 'y'
answer2 = 'y'

while answer1 == 'y' and answer2 == 'y':
    answer1 = raw_input("do you want to see your shopping list? (y or n) ")
    if (answer1 == 'y') :
        f = open("shoppingList.xml", "r")
        print(f.read())
    
        answer2 = raw_input("do you want to add an item to your shopping list? (y or n)")
        if (answer2 == 'y') :
            item = raw_input("enter item name: ")
            f = open("shoppingList.xml", "a")
            f.write(item)
        else:
            print("goodbye")
            break
        
    else:
        print("goodbye")
        break
