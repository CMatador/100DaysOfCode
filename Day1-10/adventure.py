# Day 3 - Choose your own adventure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_right = input('''
You see two roads in front of you that go around a mountain, 
so there's no way to see what lies further ahead. The choice is yours... "left" or "right"?
''')

if left_right.lower() == 'left':
    swim_wait = input('''
On the other side of the mountain you reach a lake. 
You see a ferry in the distance heading your way.
No way to discern if they are friend or foe, you can either stick around to find out,
or you could try to swim to the distant island on your own.
"swim" or "wait", the choice is yours...
''')
    if swim_wait.lower() == 'wait':
        rby = input('''
The ferryman approaches and offers you passage in return for a small cut of your findings.
You hastily agree and hop on board.
After reaching the other side you descend into the cave and see three colored tunnels.
Any or all of them could contain treasure. 
"Red", "Blue", or "Yellow"... your choice as always.
''')
        if rby.lower() == 'red':
            print('''
Following the red tunnel you see a shiny Ruby at the tunnel end.
What you don't see is a dragon who doesn't look like he wants to share.
With a mighty breath you are burnt to a crisp, and no one will ever find out.
Game Over.
''')
        elif rby.lower() == 'blue':
            print('''
As you make your way down the blue tunnel, you begin to feel very cold.
A small sacrifice to make for the riches ahead.
The further you go the colder it gets, until you can't move a muscle.
You are destined to die here, frozen just mere feet away from the sapphire you came here for.
Game Over.
            ''')
        elif rby.lower() == 'yellow':
            print('''
Making your way through the yellow hall, you see the diamond at the end on a pedestal.
Your curious brain notices there's a boulder set to spring forth as soon as the gem is taken.
You decide to tell the ferryman about the treasure.
He grabs the diamond, and laughs saying he's going to keep the whole thing and that you are a fool.
WHAM!
The boulder crushes him, the diamond falling to the floor.
You pick it up and leave the island, sailing back on his ship and never telling anyone what happened that day.
You Win!
            ''')
        else:
            print('''
You indecision keeps you from choosing a tunnel, and you sit podering for eternity.
That is until a pack of hungry wolves find you in their cave.
Being someone's dinner is not the treasure you were hoping to find...
Game Over.
            ''')
    else:
        print('''
You jump into the water determined to reach the island with the treasure.
Now is a terrible time to realize you don't actually know how to swim...
You sink to the bottom of the lake and drown thinking of what could've been.
Game Over.
              ''')
else:
    print('''
You encounter a grue. What is a grue? I don't know but he looks hungry.
You are eaten by the grue.
Game Over.
    ''')