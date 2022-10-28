#Python Adventures by Elwood, Eric, and Lakshay

#======INFRASTRUCTURE CODE======

#import le libraries
import random
import sys

#debug settings, remove on completion. allows selection of section, and bypassing RNG.

#cheatsEnabled: 0 = none, 1 = always win dice, 2 = always lose dice
cheatsEnabled = 1

#startingSect: Choose section to start in, from 1 to 6.
startingSect = 5


#return method for invalid options. saves time typing the same code over and over.
def invalid(method):
  print("Invalid option.")
  method()


#game over screen
def gameOver():
  hasDied = True
  choice = input("YOU DIED! Good job. Do you want to retry or quit? \n")
  if choice == "retry":
    oneStart()
  if choice == "quit":
    sys.exit()
  else:
    invalid(gameOver)
  return hasDied


#dice mechanics: takes input int as requirement to win (e.g. roll less than 10, return false, you die)
def dice(winReq):
  roll = random.randint(1, 20)
  if roll < winReq:
    diceResult = False
  if roll >= winReq:
    diceResult = True
  if cheatsEnabled == 1:
    diceResult = True
  if cheatsEnabled == 2:
    diceResult = False
  return roll, diceResult

  #win conditioning
  def endSection(section):
    completedSections = []
    completedSections.append(section)
    if len(completedSections) == 3:
      print(
        "You take your third piece of treasure back to the old man. He finally gives you the para glider."
      )
      if gameOver() == True:
        print(
          "He tells you to be careful out there. He winks and smiles at you. Suddenly, he fades away into mist like a ghost. You paraglide down the cliff into the forest to look for something to do.\n"
        )
        choice = input(
          "YOU WIN! Congratulations! Do you want to replay or quit?")
        if choice == "replay":
          oneStart()
        if choice == "quit":
          sys.exit()
        else:
          invalid(endSection)
      else:
        print(
          "He tells you he is the King of Hyrule, and tells you your name is Link.  He says the people you encountered were once your friends, and fought along with you in the war against Calamity Ganon. He put you up to these tests to let you regain the skill and knowledge you once had. Calamity Ganon has overtaken the kingdom, and the King's daughter, princess Zelda, has  been trapped inside Hyrule Castle fighting Ganon for a century. You feel the urge to go help her. You thank him, and paraglide down the cliff, into the unknown.\n"
        )
        choice = input(
          "YOU WIN! Congratulations! You also achieved the true ending of the game. Do you want to replay or quit?"
        )
        if choice == "replay":
          oneStart()
        if choice == "quit":
          sys.exit()
        else:
          invalid(endSection)


#inventory systems: can be edited or listed for various checks
# i = character id. matches with order of chars array. e.g. Link = 0
#due to pos. argument limitations, when listing, specify all irrelvant values as just 0. they will be ignored, but they will make the code run.
#chars = ["Link", "Old Man", "Urbosa", "Mipha", "Revali"]
weapon1 = ["", "", "", "", ""]
item1 = ["", "", "", "", ""]
item1Qty = [0, 0, 0, 0, 0]
weapon2 = ["", "", "", "", ""]
item2 = ["", "", "", "", ""]
item2Qty = [0, 0, 0, 0, 0]


def inv(i, funct, value, item, qty):
  if funct == "edit":
    if value == "weapon1":
      weapon1[i] = item
    if value == "weapon2":
      weapon2[i] = item
    if value == "item1":
      item1[i] = item
      item1Qty[i] = qty
    if value == "item2":
      item2[i] = item
      item2Qty[i] = qty
  if funct == "list":
    return weapon1[i], item1[i], item1Qty[i], weapon2[i], item2[i], item2Qty[i]


#hp system
health = [50, 40, 75, 65, 75]


def hp(i, funct, value):
  if funct == "list":
    return health[i]
  if funct == "edit":
    health[i] = health[i] + value
  if health[i] <= 0:
    gameOver()


#======SECTION ONE======


# start
def oneStart():
  choice = input(
    "You wake up in a pool of shallow water, inside a cave you've never explored. You get up and look around. There's a pedestal with a tablet that you take. There are chests around you. What do you do? chests, exit \n"
  )
  if choice == "chests":
    oneChests()
  if choice == "exit":
    oneExit()
  else:
    invalid(oneStart)


#open chests
def oneChests():
  inv(0, "edit", "item1", "apple", 3)
  hp(0, "edit", 10)
  print(
    "You find some worn out clothes and some apples. +10 HP, +3 Apples. \n")
  oneExit()


#exit cave
def oneExit():
  dir = input(
    "You are greeted with a cliff to the north, looking over lush forest. There is a familiar looking castle in the distance. Where do you go? north, east \n"
  )
  if dir == "north":
    oneNorthOne()
  if dir == "east":
    twoStart()
  else:
    print("Invalid option.")
    oneExit()


#go north once
def oneNorthOne():
  inv(0, "edit", "weapon1", "branch", 1)
  dir = input(
    "You find an old tree branch on the ground. You pick it up and put it in your pocket. Where to next? \n"
  )
  if dir == "north":
    oneNorthTwo()
  if dir == "east":
    twoStart()
  else:
    invalid(oneNorthOne)


#go north twice
def oneNorthTwo():
  print("You fell off the cliff.")
  gameOver()


#======SECTION TWO======


#start
def twoStart():
  print(
    "You meet an old man. He asks you who you are, but you don't know. He gives you a bow, 10 arrows and a map leading somewhere. Old Man joins your party.\n"
  )
  inv(0, "edit", "weapon2", "bow", 1)
  inv(0, "edit", "item2", "arrow", 10)
  if (inv(0, "list", 0, 0, 0)[0] == "branch"):
    choice = input(
      "The Old Man leads you to an odd looking structure sprouting out of the ground. Before you can reach it, you are attacked by skeletons with bows. What do you do? run, use bow, use branch\n"
    )
  else:
    choice = input(
      "The Old Man leads you to an odd looking  structure sprouting out of the ground. Before you can reach it, you are attacked by skeletons with bows. What do you do? run, use bow\n"
    )
  if choice == "run":
    print(
      "You got distracted while running and ran right off the cliff. You die. L Bozo."
    )
    gameOver()
  if choice == "use branch":
    if (inv(0, "list", 0, 0, 0)[0] == "branch"):
      roll = dice(20)
      print(
        "You fight back with a tree branch. You must get 20 on the dice to survive. \n You rolled: "
        + str(roll[0]))
      if roll[1] == False:
        gameOver()
      if roll[1] == True:
        print("\nYou barely survived. -40HP, +10 arrows from their loot.")
        hp(0, "edit", -40)
        inv(0, "edit", "item2", "arrow", 20)
        twoTree()
  if choice == "use bow":
    roll = dice(5)
    print(
      "You fight back with your bow and arrows. You must get at least 5 on the dice to survive. \n You rolled: "
      + str(roll[0]))
    if roll[1] == False:
      gameOver()
    if roll[1] == True:
      print("\nYou survived! -20HP, -2 arrows.")
      hp(0, "edit", -20)
      inv(0, "edit", "item2", "arrow", 8)
      twoTree()
  else:
    invalid(twoStart)


def twoTree():
  choice = input(
    "You reach the structure and tap your tablet on a pedestal protruding from the side. A massive tower comes up from the ground, along with many others that look like it around the land. The Old Man says he will give you a paraglider to get down from the cliff and reach the other towers, if you can find him some treasure. What do you do next? inventory, east, west, south \n"
  )
  if choice == "inventory":
    if inv(0, "list", 0, 0, 0)[1] == "apple":
      print(
        "You check your backpack for those apples you got earlier. You eat them and gain 30 HP."
      )
      inv(0, "edit", "item1", "none", 0)
      hp(0, "edit", 30)
      twoTree()
    else:
      print("You check your backpack for food, but you find nothing there.")
      twoTree()
  if choice == "east":
    fiveStart()
  if choice == "south":
    fourStart()
  if choice == "west":
    threeStart()
  else:
    invalid(twoTree)


#======SECTION THREE======

def threeStart():
  choice = input("You travel westward into the desert plains. It is very hot. You come across an oasis serving water and food. Do you stop for a snack? yes, no \n")
  if choice == "yes":
    hp(0,"edit",10)
    inv(0,"edit", "weapon1", "sword", 0)
    print("You have some water and berries. You also purchase a broadsword at the shoppe. +10 HP \n")
    threeTree()
  if choice == "no":
    threeTree()
  else:
    invalid(threeStart)

def threeTree():
  choice = input("What direction shall you go next? north, east, south \n")
  if choice == "north":
    threeNorth()
  if choice == "south":
    threeSouth()
  if choice == "east":
    print("You head back the way you came. \n")
    twoTree()
  else:
    invalid(threeTree)

def threeSouth():
  print("You walk south until you reach a massive dust storm. You cannot see or breathe. You die. \n")
  gameOver()

def threeNorth():
  choice = input("You encounter the ruins of an ancient building. It is guarded by monsters that look hungry. What do you do? run back, fight \n")
  if choice == "run back":
    threeTree()
  if choice == "fight":
    if inv(0,"list",0,0,0)[0] == "sword":
      roll = dice(5)
      print("You decide to stay and fight. Good thing you bought that sword, because you only need more than 5 on the dice to win. You rolled: " + roll[0])
      if roll[1] == True:
        print("You won! -15HP")
        hp(0,"edit",-15)
        threeIce()
      if roll[1] == False:
        gameOver()
    if inv(0,"list",0,0,0)[0] == "branch":
      roll = dice(15)
      print("You decide to stay and fight. You only have a branch and your bow. You need more than 15 on the dice to win. You rolled: " + roll[0])
      if roll[1] == True:
        print("You won! -30HP, -4 arrows")
        hp(0,"edit",-15)
        inv(0,"edit","item2","arrow",8)
        threeIce()
      if roll[1] == False:
        gameOver()

def threeIce():
  choice = input("You come across an underground bunker with a small man selling ice.  You ask him where you can find some treasure. He laughs and directs you west to a town called Gerudo. Do you follow her advice? yes, no \n")
  if choice == "no":
    print("You walk south until you reach a massive dust storm. You cannot see or breathe. You die. \n")
    gameOver()
  if choice == "yes":
    threeGerudo()
  else:
    invalid(threeIce)

def threeGerudo():
  choice = i
  

#======SECTION FIVE======

# Start of section 5
def fiveStart():
  path = input(
    "\nYou go east towards a large open field.  The air smells crisp and the grass is damp with dew. In the distance, you see a lake and cabin. The cabin seems to be abandoned. Where do you go?\n"
              )
  if path.lower() == "cabin":
    print(
      "\nGoing to the cabin.\n"
          )  
    cabinPath()
  elif path.lower() == "lake":
    print(
      "\nGoing to the lake.\n"
          )
    lakePath()
  else:
    invalid(fiveStart)

# Cabin path part uno
def cabinPath():
  path = input(
    "\n The cabin door seems to be boarded shut. The windows seem to be boarded shut too. What do you want to do?\n"
              )
  if "break" in path.lower():
    breakBoards()
  elif "leave" in path.lower():
    print(
      "\nLeaving the cabin\n"
    )
    fiveStart()
  else:
    invalid(cabinPath)

def breakBoards():
  # Change "otherweapon"
  breakBoard = input(
    "\nBreak it with what?\n FIST \n \n OTHERWEAPON \n"
  )
  if "fist" in breakBoard.lower():
                        roll = dice(15)
                        if roll[1] == True:
                            print(
                                "The boards have been broken. \n You have rolled: " + str(roll[0]))
                            print(
                              "\nEntering the cabin\n"
                            )
                            cabinPathPartTwo()
                          
                        elif roll[1] == False:
                            print(
                                "The boards haven't been broken. Try again. \n You have rolled: " + str(roll[0]))
                            print("-1 HP")
                            rollTwo = dice(20)
                            if rollTwo[1] == True:
                                print("You hit your " + breakBoard.lower(
                                ) + " too hard, which cut it and broke it. You slowly bled to death. Come on man.")
                                gameOver()
                            breakBoards()
                    # !!! make sure to change "otherweapon" !!!
                        elif "otherweapon" in breakBoard.lower():
                          roll = dice(10)
                          if roll[1] == True:
                            print(
                                "The boards have been broken. \n You have rolled: " + str(roll[0]))
                            print(
                              "\nEntering the cabin.\n"
                            )
                            cabinPathPartTwo()
                        elif roll[1] == False:
                            print(
                                "The boards haven't been broken, try again. \n You have rolled: " + str(roll[0]))
                            breakBoards()
  else:
    invalid(breakBoards)
                          
### FIX CABIN PATH PART TWO
def cabinPathPartTwo():
  while True:
    path = True
    if path == False:
      print(
        "Path is done")
      break
    elif path == True:
      while True:
        choosePath = input(
        "The atmosphere is damp and dusty. To the left is a door frame. On the table in front of you are three cans. You're not sure if they're expired or not. Taking them may or may not be a good idea.\n TAKE \n \n DON'T \n")
        if choosePath == "break":
          break
        elif "take" in choosePath.lower():
          print(
            "\n Taking the cans")
          cans()
        elif "don't" in choosePath.lower():
          enterDoor = input(
            "\nNot taking the cans.")
        else:
          choosePath == "break"
          print("Invalid option \n")
          break
        while True:
          if path == True:
            enterDoor = input(
            "Are you going through the doorframe?\n YES \n \n NO \n")
            if "yes" in enterDoor:
              print(
               "entering the door")
              path = False
              return True
            elif "no" in enterDoor:
              path = False
              print(
                "leaving the cabin")
              return False
            else:
              invalid()
              continue
        else:
          break
    else:
      continue

# Cans - They deal either -5 or +5 HP
def cans():
  print("Theses are the cans, make them later")


# Lake Path

        
      
#oneStart() <<< what will actually be called in production

if startingSect == 1:
  oneStart()
if startingSect == 2:
  twoStart()
if startingSect == 3:
  threeStart()
if startingSect == 4:
  fourStart()
if startingSect == 5:
  fiveStart()
if startingSect == 6:
  sixStart()
