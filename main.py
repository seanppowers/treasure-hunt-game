print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

INVALID_CHOICE = "Not a valid choice. Try again."
PLAYER_DIES_SKULL = '''
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
'''


def crossroads():
    print("You're at a crossroads. Would you like to go left or right?")
    player_choice = input().lower()
    if player_choice == 'right':
        print(
            '''
            You fall into a hole like a complete fool. You shatter the bones in your legs and die from internal bleeding.
            G A M E  O V E R
            ''')
        print(PLAYER_DIES_SKULL)
        exit()
    elif player_choice == 'left':
        sink_or_swim()
    else:
        print(INVALID_CHOICE)
        crossroads()


def sink_or_swim():
    print(
        '''
        You\'ve found a calm and pristine lake. A gentle breeze blows through the distant pine trees. 
        A small boat is tethered to a dock not far from your location. Fish, many unusually large in size, 
        produce swells on the surface that spiral and smooth away into the inky emerald darkness of the water. 
        Would you like to swim to the boat, or wait on the shore a moment?
        ''')
    player_choice = input().lower()
    if player_choice == 'swim':
        print(
            '''
            You begin to swim toward the boat. As you draw closer to the boat, you feel a large object brush by your legs. 
            Suddenly, you are jerked violently underwater. Pain explodes in your mind as you feel something bite hard 
            into your legs, the bones cracking. You begin to black out as water fills your nostrils and lungs. 
            The last thing you see is the flash of a body of an enormous fish, which tints red as your blood pools 
            the water around you.
            G A M E  O V E R
            ''')
        print(PLAYER_DIES_SKULL)
        exit()
    elif player_choice == 'wait':
        choose_door()
    else:
        print(INVALID_CHOICE)
        sink_or_swim()


def choose_door():
    print(
        '''
        You wait on the shore, breathing in the fresh air listening to the wind blow through the distant pines. 
        The swirls of the fish are now much, much larger. You can tell this is no normal lake, and that the fish in it 
        must be unusually large. 
        You're glad you didn't risk a swim. You should be able to walk around the lake to get to the other side, 
        but it will take much longer. 
        As you begin to walk, you hear a strange sound behind you. Turning around, you see two doors: a blue door and a red door. 
        The red door seems to pulse with a dull light, like flame. You can feel heat resonating from it.
        The blue door is a deep, royal blue in color.
        What color door do you choose?
        ''')
    player_choice = input().lower()
    if player_choice == 'red':
        print('''As you turn the red door knob, you can feel that it's very hot. There is a rushing sound of air
            and light explodes in your eyes as a great gust of flame engulfs you, and pulls you inside the doorway into
            an infernal landscape of fire, heat and lava. You feel your skin bubble and char as you spin into an infinite
            void of fire, light and pain. You black out quickly and die.
            G A M E  O V E R
        ''')
        print(PLAYER_DIES_SKULL)
        exit()
    elif player_choice == 'blue':
        print(
            '''
            You open the door and see a gigantic treasure chest brimming with gold.
            Y O U  W O N ! ! !
            ''')
        exit()
    else:
        print(INVALID_CHOICE)
        choose_door()


crossroads()
