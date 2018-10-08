#!/usr/bin/python

#  shoppingList.py
#  This is a complex Python program that reads a shopping list from an xml file and allows the user to add items to their shopping list.  I also added the ability for the user to delete all the items off their shopping list, which I did not have in the complex Perl program.  I'm very happy at how this turned out.
#  Created by Daniel on 10/14/18
#  The purpose of this program was to demonstrate the differences and similarites between Perl and Python by writing the same program written in Perl, but in Python.
#  To run this program simply type "python shoppingList.py" and then follow the prompts.


# Declare variables

answer1 = 'y'
answer2 = 'y'
delete = 'y'

# While loop with if else statements.  Using the while loop allowed me to keep this program DRY and remove a lot of unnessesary code that I had in my complex Perl program.

while answer1 == 'y' and answer2 == 'y' and delete == 'y':
    answer1 = raw_input("do you want to see your shopping list? (y or n) ")
    if (answer1 == 'y') :
        
        # Read shoppingList.xml
        
        f = open("shoppingList.xml", "r")
        print(f.read())
    
        answer2 = raw_input("do you want to add an item to your shopping list? (y or n) ")
        if (answer2 == 'y') :
            item = raw_input("enter item name: ")
            
            # Add item to shoppingList.xml
            
            f = open("shoppingList.xml", "a")
            f.write(item + "\n")
        else:
            delete = raw_input("do you want to delete your shopping list? (y or n) ")
            if (delete == 'y') :
                
                # Overwrite everything in shoppingList.xml
                
                d = open("shoppingList.xml", "w")
                d.write("")
                print("Shopping List deleted.  Goodbye.")
            else:
                print("goodbye")
                break
    else:
        print("goodbye")
        break

# End program
