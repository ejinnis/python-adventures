#Python Adventures by Elwood, Eric, and Lakshay

#======INFRASTRUCTURE CODE======

#import le libraries
import random
import sys

#debug settings, remove on completion. allows selection of section, and bypassing RNG.

#cheatsEnabled: 0 = none, 1 = always win dice, 2 = always lose dice
cheatsEnabled = 1

#startingSect: Choose section to start in, from 1 to 6.
startingSect = 1


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
