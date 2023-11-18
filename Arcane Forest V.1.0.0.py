#Intro 

print("After over 600 lines of code...")
print("And hours of work...")
print("Smiley Games Presents")
print("The Arcane Forest: A text Adventure")
input("Press Enter to Continue")


#Merchant Items: 

#Apple: Restores 10 hunger. Cost: 10
#Health Pack: Restores 20 health. Cost: 20
#Old Knife: You take 20% less damage in battles. Cost: 30
#Sword: You take 50% less damage in battles. Cost: 50

#Reset Variables

import sys
my_hunger = 100
spend = 0
heal = 0
my_health = 100
my_money = 20
my_choice = 1
knife = False
sword = False
Apple = 0
merchant = 1
horse = False
flashlight = False
Map = False


#Introduction

print("Deep within a mysterious forest, secrets of an unimaginable power lie hidden. It is up to you to navigate thorugh enchanted lanscpaes, solve challenging puzzles, and face the creatures to uncover the power and use it for good... or for evil.")
input("Press Enter to continue")
print("You are an adventurous wanderer with a troubled past. Seeking solace and purpose, you stumble upon a cryptic map that leads you to the heart of the Arcane Forest. As you delve deeper into the forest's secrets, you discover that the ancient artifacts hidden within possess the power to rewrite history. Driven by a desire to change your own fate, you must confront the creatures, unravel the truth behind the forest's enchantments, and ultimately decide if possesing the power is worth the risk.")
name = input("What is your name?")
print("Your name is now " + name + "!")

#Choice 1

print("You are in the town square. Where would you like to go? 1. The Arcane Forest. 2. The Castle. 3. The merchant. 4. Stay where you are and explore.")
my_choice = input("Arcane forest = 1 Castle = 2 Merchant = 3. Explore = 4")
if my_choice == "1":
    print("You decide to start your journey to the forest")
elif my_choice == "2":
    print("You go to the castle but it is guarded and you can't get in. You decide to go to the forest")
elif my_choice == "3":
    print("You don't have any coins. Try again later. You decide to make your way to the forest")
elif my_choice == "4":
    print("You decide to explore the town square. You look around and decide to talk to somebody. They say that they live here and can't leave. It might be tricky to try to escape to get to the forest. The villager gives you an old knife")
    knife = True
else:
    exit("Invalid Choice")

#Choice 2

print("You find the exit but it is guarded. The guards refuse to let you leave because the king wants the treasure for himslef. What do you do?")
my_choice = input("Find a different exit = 1 Fight the guards = 2 Distract the guards = 3 Try to sneak past = 4")
if my_choice == "1":
    print("You decide to look for a different exit but you don't find one.")
    exit("Wasted...") 
elif my_choice == "2":
    print ("You decide to try and fight the guards. You don't have any good weapons so they defeat you")
    exit("Wasted...") 
elif my_choice == "3":
    print("You get another person to distract the guards and try to sneak past. It works but the doors are locked. They catch you")
    exit("Wasted...")
elif my_choice == "4":
    print("You wait for the guards to get distracted. You sneak past them but the doors are locked. You steal one of the guards keys and succesfuly get out")
else: 
    exit("Invalid Choice")

#Choice 3

print("The path to the forest is steep and you take many breaks. You loose 20 hunger. Your hunger is now")
my_hunger -= 20
print(my_hunger)
("You arrive to a crossroad. Which direction would you like to take?")
my_choice = input("Would you like to go left or go right?")
if my_choice == "left":
    print("You decide to go left. On the side of the road you find a chest. Inside is 20 coins. You now have")
    my_money += 20
    print(my_money)
elif my_choice == "right":
    print("You decide to go right. On the side of the road you see a chest. Inside is a health pack. Use it to heal yourself. Your health is now")
    print(my_health)
    heal = 1
else:
    exit("Invalid Choice")

#Choice 4

print("On your way to the forest, you see a wild boar")
my_choice = input("Would you like to attack it or walk away silently? Type 1 for attack and 2 for walking away")
if my_choice == "1":
    print("You attack the boar.")
    my_health -= 20
    my_money += 50
    print(my_health)
    print(my_money)
elif my_choice == 2: 
    print("You walk away silently")
else: 
    exit("Invalid Choice") 
my_choice = input("Would you like to heal yourself? (Yes / No)")
if my_choice == "Yes":
    if heal == 1:
        print("You heal yourself")
        my_health += 20
        print(my_health)
        heal = False
    if heal == 0:
        print("You don't have a health pack")
elif my_choice == "No":
    print("You decide not to heal yourself")
else: 
    exit("Invalid Choice")

#Choice 5

print("You continue down the path. You see an old man asking for money.")
my_choice = input("Would you like to give him some? (Yes / No") 
if my_choice == "Yes":
    if my_money > 4:
        print("You give the man 5 coins. The man thanks you for your donation. Your coins are now")
        my_money -= 5
        print(my_money)
    elif my_money < 4:
        print("You don't have enough money")
 
elif my_choice == "No":
    print("You ignore the man and give him no money")
else:
    exit("Invalid Choice") 
print ("You continue your journey. The path is rough and not always paved. You loose 20 hunger. Your hunger is now")
my_hunger -= 20
print(my_hunger)

#Merchant

print("You see a merchant stall. Would you like to stop and buy some inventory.")
my_choice = input("See your inventory = 1 Visit the merchant = 2 Do nothing = 3")
if my_choice == "1":
    if knife == True:
        print("You have an old knife")
    if heal == True:
        print("You have a health pack")
    print(my_money)
elif my_choice == "2":
    print("You decide to visit the merchant.")
    print("Apple restores 10 hunger but costs 10 coins. Health Pack restores 20 health but costs 20 coins. Old knife takes 20% less damage during fights but costs 30 coins. Sword takes 50% less damage during fights but costs 50 coins.")
    my_choice = input("Would you like to buy something? (Yes / No")
    if my_choice == "Yes":
        merchant = input("Apple = 1 Health pack = 2 Old knife = 3 Sword = 4")
        if merchant == "1" and my_money > 9:
            print("You buy one apple. Your money is")
            my_money -= 10
            print(my_money)
            Apple += 1
        elif merchant == "2" and my_money > 19:
            print("You buy one health pack. Your money is")
            my_money -= 20
            print(my_money)
            heal += 1
        elif merchant == "3" and my_money > 29:
            print ("You buy one old knife. Your money is")
            my_money -= 30
            print(my_money)
            knife = True
        elif merchant == "4" and my_money > 49:
            print("You buy an old sword. Your money is")
            money -= 50
            print("my_money")
            sword = True
        else:
            exit("Invalid Choice")
    elif my_choice == "No":
        print("You decide not to buy anything")
    else:
        exit("Invalid Choice")
elif my_choice == "3":
    print("You decide to do nothing")

#Display Stats

print("Here are your current stats. Your hunger is")
print(my_hunger)
print("Your health packs are")
print(heal)
print("Your health is")
print(my_health)
print("Your coins are")
print(my_money)
print("Your number of apples are")
print(Apple)


#Next Choice

print("In the distance, you can see the Arcane Forest. You are one of the only people of your time to try and attempt it because of the king's orders and because of how dangerous it is. There will be many challenges, some of which you may not survive. Rumour has it that there are creatures that guard the forest, stooping anyone and anything trying to get to the heart of the forest where the treasure is kept. The quest will be dangerous, but the reward unimaginable power. This will be your last chance to turn back before it is too late. Choose wisely.")
my_choice = input("Do you wish to continue(Yes / No)")
if my_choice == "Yes":
    print("Proceed at your own risk. And good luck.")
elif my_choice == "No": 
    print("That is a wise choice. You head back to the village to live th rest of your days peacefully...")
    exit("Quest Failed...")
else:
    exit("Invalid Choice") 

#Next choice

print("Your hunger is")
print(my_hunger)
print("Your health is")
print(my_health)
print("Would you like to use your health pack or apple? A health pack restores 20 health and an apple restores 10 hunger.")
my_choice = input("Would you like to eat an apple? (Yes / No)")
if my_choice == "Yes":
    if Apple > 0:
        print("You eat an apple. Your hunger is")
        my_hunger += 10
        Apple -= 1
        print(my_hunger)
    else:
        print("You do not have any apples!")
else:
    print("You do not eat an apple.")
my_choice = input("Would you like to use a health pack? (Yes / No)")
if my_choice == "Yes":
    print("You use a health pack. Your health is")
    my_health += 20
    print(health) 
else:
    print("You do not use a health pack.")
print("On a hill, you see a wild horse. You can try to tame it using an apple or leave it alone.")
my_choice = input("1 = Try to tame it 2 = Leave it alone")
if my_choice == "1":
    if Apple > 0:
        print("You try to tame it with an apple. Success! You now have a horse.")
        horse = True
        Apple -= 1
    else:
        print("You do not have any apples!")

elif my_choice == "2":
    print("You leave it alone")
else:
    exit("Invalid Choice")
if horse == True:
    print("Now that you have a horse, the journey will be a lot faster. You will have to feed your horse an apple once in a while if you want to keep it tame.")
my_choice = input("Would you like to buy some apples? (Yes / No)")
if my_choice == "Yes":
    if my_money > 9:
        print("You bought one apple. You money is now")
        Apple += 1
        my_money -=10
        print(my_money)
        print("Your apples are now")
        print(Apple)
    else: 
        print("You do not have enough money!")
elif my_choice == "No":
    print("You do not buy any apples")
else:
    exit("Invalid Choice")
print("You continue down the path. Up ahead are a bunch of boulders blocking your path. You could climb them but that would be dangerous. Or you could look for an alternative route.")
my_choice = input("1 = Climb the boulders 2 = Go around them")
if my_choice == "1":
    print("You decide to climb the boulders")
    print("On the way up, you scrape your hand. Eventually you make it to the top. You loose 10 health. Your health is now")
    my_health -= 10
    print (my_health)
    if horse == True:
        print("Your horse cannot climb the boulders. You will have to continue without it.")
        horse = False 
    if my_health < 1:
        print("You ran out of health and died.")
        exit("Wasted...")
elif my_choice == "2":
    print("You decide to go around them")
    if horse == True:
        print("Thanks to your horse, you get around the boulders and back on track quickly.")
    else:
        print("The journey is slow. You loose 10 hunger.")
        if my_hunger < 1:
            print("You ran out of food.")
            exit("Wasted...")
        print("After a while, the boulders start to get less steep and you can easily climb around them. Eventually, you get back to the path.")
else:
    exit("Invalid Choice")
print("It is starting to get dark oustide. You are going to have to find a place to spend the night. You could try to build a shelter using wood that you find buy it will take a while. Or you could stay in a hotel that is not too far away but it will be more expensive.The hotel will cost you 30 coins. Your coins are")
print(my_money) 
my_choice = input("1 = Shelter out of wood 2 = Hotel (30 coins)")
if my_choice == "1":
    print("You decide to build a shelter out of wood. You look around and realize that the only wood is in the Arcane Forest and that is too far away. Looks like you will have to sleep outside tonight.")
    my_health -= 50
    if my_health > 1:
        print ("You survived the night. Your health is")
        print(health)
    else:
        print("You died during the night")
        exit("Wasted...")
elif my_choice == "2":
    if my_money > 29:
        print("You deicde to stay the night in a hotel. Your coins are")
        my_money -= 30
        print(my_money)
    else: 
        print("You do not have enough money. Looks like you will have to spend the night outside.")
        my_health -= 50
        if health > 1:
            print ("You survived the night. Your health is")
            print(health)
        else:
            print("You died during the night")
            exit("Wasted...")
else:
    exit("Invalid Choice") 
if horse == True:
    print("Your horse also survived!")
    
#Display Stats

print("Here are your current stats. Your hunger is")
print(my_hunger)
print("Your health packs are")
print(heal)
print("Your health is")
print(my_health)
print("Your coins are")
print(my_money)
print("Your number of apples are")
print(Apple) 


#Apple / Health Pack 

print("Would you like to use your health pack or apple? A health pack restores 20 health and an apple restores 10 hunger.")
my_choice = input("Would you like to eat an apple? (Yes / No)")
if my_choice == "Yes":
    if Apple > 0:
        print("You eat an apple. Your hunger is")
        my_hunger += 10
        Apple -= 1
        print(my_hunger)
    else:
        print("You do not have any apples!")
else:
    print("You do not eat an apple.")
my_choice = input("Would you like to use a health pack? (Yes / No)")
if my_choice == "Yes":
    print("You use a health pack. Your health is")
    my_health += 20
    print(health) 
else:
    print("You do not use a health pack.") 

#Feed the horse apples to keep it tamed 

if horse == True:
    print("You need to feed your horse an apple to keep it tamed. Would you like to feed it one? (Yes / No)")
    if my_choice == "Yes":
        if Apple > 0:
            print ("You feed your horse an apple. Your apples are")
            print(Apple)
        else:
            print("You have no apples!")
    elif my_choice == "No":
        print("You do not feed your horse an apple. Your horse runs away.")
        horse = False
    else:
        exit("Invalid Choice")

#Riddle

print("You see a man blocking the path. You ask him to move. He says that you can only pass if you answer his riddle correctly. Otherwise you die. Make sure to answer the riddle in full captials like THIS. The answer is one word. Example: If the answer is a dog type DOG")
my_choice = input("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
if my_choice == "ECHO":
    print("Correct! The man lets you move on.")
if my_choice != "ECHO":
    print("Incorrect! You die")
    exit("Wasted...")


#Merchant

print("You see a merchant stall. Would you like to stop and buy some inventory.")
my_choice = input("See your inventory = 1 Visit the merchant = 2 Do nothing = 3")
if my_choice == "1":
    if knife == True:
        print("You have an old knife")
    if heal == True:
        print("You have a health pack")
    print(my_money)
elif my_choice == "2":
    print("You decide to visit the merchant.")
    print("Apple restores 10 hunger but costs 10 coins. Health Pack restores 20 health but costs 20 coins. Old knife takes 20% less damage during fights but costs 30 coins. Sword takes 50% less damage during fights but costs 50 coins.")
    my_choice = input("Would you like to buy something? (Yes / No")
    if my_choice == "Yes":
        merchant = input("Apple = 1 Health pack = 2 Old knife = 3 Sword = 4")
        if merchant == "1" and my_money > 9:
            print("You buy one apple. Your money is")
            my_money -= 10
            print(my_money)
            Apple += 1
        elif merchant == "2" and my_money > 19:
            print("You buy one health pack. Your money is")
            my_money -= 20
            print(my_money)
            heal += 1
        elif merchant == "3" and my_money > 29:
            print ("You buy one old knife. Your money is")
            my_money -= 30
            print(my_money)
            knife = True
        elif merchant == "4" and my_money > 49:
            print("You buy an old sword. Your money is")
            money -= 50
            print("my_money")
            sword = True
        else:
            exit("Invalid Choice")
    elif my_choice == "No":
        print("You decide not to buy anything")
    else:
        exit("Invalid Choice")
elif my_choice == "3":
    print("You decide to do nothing")
    
#Display Stats

print("Here are your current stats. Your hunger is")
print(my_hunger)
print("Your health packs are")
print(heal)
print("Your health is")
print(my_health)
print("Your coins are")
print(my_money)
print("Your number of apples are")
print(Apple) 


print("Would you like to use your health pack or apple? A health pack restores 20 health and an apple restores 10 hunger.")
my_choice = input("Would you like to eat an apple? (Yes / No)")
if my_choice == "Yes":
    if Apple > 0:
        print("You eat an apple. Your hunger is")
        my_hunger += 10
        Apple -= 1
        print(my_hunger)
    else:
        print("You do not have any apples!")
else:
    print("You do not eat an apple.")
my_choice = input("Would you like to use a health pack? (Yes / No)")
if my_choice == "Yes":
    print("You use a health pack. Your health is")
    my_health += 20
    print(health) 
else:
    print("You do not use a health pack.")
    

#Arcane Forest
#Bridge Choice

print("You have finally arived at the Arcane Forest! The descisions will get harder and you will have to make some tough choices. The Arcane Forest, as its name suggests, is a realm of enigma and peril. It is a sprawling expanse of towering trees, their gnarled branches reaching out like skeletal hands, shrouded in an ever-present, eerie mist. The forest floor is a labyrinth of undergrowth, where shadows dance and whisper secrets of the ancient power that pulses beneath the surface. The air is heavy with the scent of damp earth and the faint, unsettling hint of something else - something otherworldly. The silence is punctuated by the occasional rustle of leaves or the distant hoot of an owl, creating an atmosphere of suspense that keeps intruders on their toes. The forest is alive, not just with flora and fauna, but with an energy that hums and crackles, a raw, untamed power that seems to seep from the very soil. It is said that this power can be harnessed, but only by those brave or foolish enough to venture deep into the heart of the forest. The Arcane Forest is not a place for the faint-hearted. It is a place of danger and mystery, where every step could lead to discovery or disaster. It is a place that holds an unimaginable power, waiting to be unlocked by those daring enough to seek it. A river is blocking your path. There is also a sign pointing to go West to reach the heart of the forest. How convenient...")
print("There are many entrances to the forest. The closest one is to the left, but you will have to walk through a stream. Or, you could use the farther one to the right, but there is a bridge.")
my_choice = input("Make a choice. (Left / Right)")
if my_choice == "Left":
    print("You decide to go left and cross the stream. When you get there, you walk across the stream. You sucesfully cross the stream but now you are cold. You loose 10 health. Your health is now")
    my_health -= 10
    print(my_health)
    if my_health < 1:
        print("You ran out of health!")
        exit("Wasted...")
elif my_choice == "Right":
    print("You decide to go right and use the bridge. It takes a long time but you finally cross the bridge. You loose 10 hunger from walking. Your hunger is now")
    my_hunger -= 10
    print(my_hunger)
    if my_hunger < 1:
        print("You ran out of hunger!")
        exit("Wasted...")
else:
    exit("Invalid Choice")

#Eat dead food choice

print("You are now in the forest. After a while, you see an animal carcass with some meat on it. You wonder how it died. Your hunger is")
print(my_hunger)
my_choice = input("Would you like to eat it? (Yes / No)")
if my_choice == "Yes":
    print("You decide to eat the carcass. Unfortunately, it is raw and you get sick. You loose 50 health. Your health is now")
    my_health -= 50
    print(my_health)
    if my_health < 1:
        print("You ran out of health!")
        exit("Wasted")
elif my_choice == "No":
    print("You decide not to eat the carcass")
else:
    exit("Invalid Choice")
print("You hear a howl. The sound that the creatures make when they are near you...")
print("You better hide if you don't want to die. You can hide in a bush or hide in a tree.")
my_choice = input("1 = bush 2 = tree")
if my_choice == "1":
    print("You decide to hide in a nearby bush. The screeching gets louder as it comes closer. Suddenly it stops...")
    my_choice = input("What do you do? Do you come out or stay hidden?. 1 = Come out 2 = Stay hidden")
    if my_choice == "1":
        print("You decide to come out. You don't see anything. Suddenly, you get knocked to the ground and everything goes black.")
        exit("Wasted...")
    elif my_choice == "2":
        print("You decide to stay hidden. After a while, you hear footstpes walking away. You think it is safe to come out.")
    else:
        exit("Invalid Choice")
elif my_choice == "2":
    print("You decide to hide in a nearby tree.")
    if horse == True:
        print("You left your horse behind. A dark figure comes towards your horse. Before you can see what will happen to it, it jumps up towrds you. Everything goes black.")
        exit("Wasted...")
    print("The screeching gets louder as it comes closer. Suddenly it stops...")
    my_choice = input("What do you do? Do you come out or stay hidden?. 1 = Come out 2 = Stay hidden")
    if my_choice == "1":
        print("You decide to come out. You don't see anything. Suddenly, you get knocked to the ground and everything goes black.")
        exit("Wasted...")
    elif my_choice == "2":
        print("You decide to stay hidden. After a while, you hear footstpes walking away. You think it is safe to come out.")
    else:
        exit("Invalid Choice") 
print("You decide to continue your journey.")
print("You aren't sure exactly where you should go. You remember that there was a sign saying to go in a specific direction before you entered but you can't remember which. ")
my_choice = input("Type North or East or South or West to make a choice") 
if my_choice == "North":
    print("You decide to go North. After a while, you get lost and try to go back but get confused. As you try to find your way back, you catch a glimpse of a creature and it is all over for you.")
    exit("Wasted...")
elif my_choice == "East":
    print("You decide to go East. After a while, you get lost and try to go back but get confused. As you try to find your way back, you catch a glimpse of a creature and it is all over for you.")
elif my_choice == "South":
    print("You decide to go South. After a while, you get lost and try to go back but get confused. As you try to find your way back, you catch a glimpse of a creature and it is all over for you.")
elif my_choice == "West":
    print("You decide to go West. You know you are going in the right direction because the trees are getting thicker and everything is darker.")
else:
    exit("Invalid Choice...")
print("As you go further, it gets harder and harder to see.")
print("Would you like to buy a flashlight from the merchant for 20 coins? Your coins are")
print(my_money)
my_choice = input("Yes / No")
if my_choice == "Yes":
    if my_money > 19:
        print("You decide to buy a flashlight")
        flashlight = True
    else:
        print("You do not have enough coins!")
elif my_choice == "No":
    print("You decide to not buy a flashlight.")
else:
    exit("Invalid Choice")
if flashlight == True:
    print("Thanks to the flashlight, you can see a lot better now. Up ahead is an old cabin made of wood. It looks like it hasn't been used in ages.")
else:
    ("It is getting to dark to see. You stumble upon a structure that is made of wood. You think that it is a cabin.")
my_choice = input("Do you want to look for an entrance and go in? (Yes / No)")
if my_choice == "Yes":
    print("You decide to look for an entrance")
    if flashlight == True:
        print("Thanks to your flashligh, you find the entrance. You enter the structure. It is old and has a musty smell. Thr windows are boarded up and the door barely budged. This place hasn't been used for a long time. You decide to look around.")
        print("You find a map. Inside is also a chest with 25 coins. Your coins are now")
        Map = True
        my_money += 20
        print(my_money)
        print("You go back outside.")
    else:
        print("You cannot find the entrance because it is too dark. If only you had a flashlight...")
elif my_choice == "No":
    print("You decide to continue on and ignore the structure")
else:
    exit("Invalid Choice") 
if flashlight == True:
    print("Suddenly your flashlight dies. You are in the dark now.")
    flashlight = False
print("You arrive at yet another crossroad. At least that is what you think it is.")
if Map == True:
    print("Your map tells you to go right")
my_choice = input("Do you want to go left or right?")
if my_choice == "left":
    print("You decide to go left. You stumble into a cave. This is it you think. You notice a pair of red eyes staring back at you. You die before you can run.")
    exit("Wasted...")
elif my_choice == "right":
    print("You decide to go right.")
else:
    exit("Invalid Choice")
print("The path leads you into a cave. In the middle is a glowing chest. Blocking it is a glowing creature. You will have to fight it.")
print("Your health is")
print(my_health)
print("Select your weapon")
my_choice = input("1 = Bare hands 2 = Knife = 3")
if my_choice == "1":
    print("You decide to use your bare hands. Unfortunately, you stand no chance.")
    exit("Wasted...")
elif my_choice == "2":
    if knife == True:
        print("You use your knife. The battle is intense. Finally, one of you falls to the ground.")
        print("That person is you.")
        exit("Wasted...")
    else:
        print("You do not have a knife. You take too long and the creature kills you.")
        exit("Wasted...")
elif my_choice == "3":
    if sword == True:
        print("You use your sword. The battle is intense. Finally, one of you falls to the ground.")
        print("That person is the creature.")
    else:
        print("You do not have a sword. You take too long and the creature kills you.")
        exit("Wasted...")
else:
    exit("Invalid Choice")
print("You beat the creature! The treasure is now yours. The question is, what will you do with it?")
print("GAME OVER. YOU WON.")
print("Thank you for playing this game and congratulations for completing it. Play again for different choices and endings.")
print("This is a Smiley Games production")
print("This game was made possible with Python")
print("Credit to Andrew Lavoie, Beta Tester")
print("Stay tuned for another Choose your own adventure game")
print("V.1.0.0")
exit("Success!")





        
    
        


    
        









