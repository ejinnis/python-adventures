#Python Adventures by Elwood, Eric, and Lakshay

#======INFRASTRUCTURE CODE======

#import le libraries
import random
import sys
import time



#debug settings, remove on completion. allows selection of section, and bypassing RNG.

#cheatsEnabled: 0 = none, 1 = always win dice, 2 = always lose dice
cheatsEnabled = 1

#startingSect: Choose section to start in, from 1 to 6.
startingSect = 1


#return method for invalid options. saves time typing the same code over and over.
def invalid(method):
  print("Invalid option.")
  method()


hasDied = 0


#game over screen
def gameOver(section):
  hasDied = 1
  choice = input("YOU DIED! L bozo. Do you want to retry or quit? \n")
  if choice == "retry":
    section
  if choice == "quit":
    sys.exit()
  else:
    invalid(gameOver(section))
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

completedSections = []
#win conditioning
def sectComplete(section):
  completedSections.append(section)
  sorted = completedSections.sort()
  if len(completedSections) == 1:
    if completedSections[0] == 3:
      choice = input(
        "You take your treasure back to the old man. He accepts it with delight, and asks you to find two more. When you ask him why, he only says that it's for your own good. What direction do you travel next? east, south \n"
        )
      if choice == "east":
          fiveStart()
      if choice == "south":
          fourStart()
      else:
          invalid(sectComplete)
    if completedSections[0] == 4:
      choice = input(
          "You take your trasure back to the old man. He accepts it with delight, and asks you to find two more. When you ask him why, he only says that it's for your own good. What direction do you travel next? east, west \n"
        )
      if choice == "east":
        fiveStart()
      if choice == "west":
        threeStart()
      else:
        invalid(sectComplete)
    if completedSections[0] == 5:
      choice = input(
          "You take your trasure back to the old man. He accepts it with delight, and asks you to find two more. When you ask him why, he only says that it's for your own good. What direction do you travel next? west, south \n"
        )
      if choice == "west":
        threeStart()
      if choice == "south":
        fourStart()
      else:
        invalid(sectComplete)
  if len(completedSections) == 2:
    if sorted == [3, 4]:
      print(
          "You take your second treasure back to the old man. He sends you off again on your final quest, due east."
        )
      fiveStart()
    if sorted == [4, 5]:
      print(
          "You take your second treasure back to the old man. He sends you off again on your final quest, due west."
        )
      threeStart()
    if sorted == [3, 5]:
      print(
          "You take your second treasure back to the old man. He sends you off again on your final quest, due south."
        )
      fourStart()
    if len(completedSections) == 3:
      print(
        "You take your third piece of treasure back to the old man. He finally gives you the para glider."
      )
      if hasDied == 1:
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
          invalid(sectComplete)
      if hasDied == 0:
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
          invalid(sectComplete)
    return completedSections

sectComplete(3)
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
    gameOver(oneStart)


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
  gameOver(oneStart)


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
    gameOver(twoStart)
  if choice == "use branch":
    if (inv(0, "list", 0, 0, 0)[0] == "branch"):
      roll = dice(20)
      print(
        "You fight back with a tree branch. You must get 20 on the dice to survive. \n You rolled: "
        + str(roll[0]))
      if roll[1] == False:
        gameOver(twoStart)
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
      gameOver(twoStart)
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
  choice = input(
    "You travel westward into the desert plains. It is very hot. You come across an oasis serving water and food. Do you stop for a snack? yes, no \n"
  )
  if choice == "yes":
    hp(0, "edit", 10)
    inv(0, "edit", "weapon1", "sword", 0)
    print(
      "You have some water and berries. You also purchase a broadsword at the shoppe. +10 HP \n"
    )
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
  print(
    "You walk south until you reach a massive dust storm. You cannot see or breathe. You die. \n"
  )
  gameOver(threeStart)


def threeNorth():
  choice = input(
    "You encounter the ruins of an ancient building. It is guarded by monsters that look hungry. What do you do? run back, fight \n"
  )
  if choice == "run back":
    threeTree()
  if choice == "fight":
    if inv(0, "list", 0, 0, 0)[0] == "sword":
      roll = dice(5)
      print(
        "You decide to stay and fight. Good thing you bought that sword, because you only need more than 5 on the dice to win. You rolled: "
        + str(roll[0]))
      if roll[1] == True:
        print("You won! -15HP")
        hp(0, "edit", -15)
        threeIce()
      if roll[1] == False:
        gameOver(threeStart)
    if inv(0, "list", 0, 0, 0)[0] == "branch":
      roll = dice(15)
      print(
        "You decide to stay and fight. You only have a branch and your bow. You need more than 15 on the dice to win. You rolled: "
        + str(roll[0]))
      if roll[1] == True:
        print("You won! -30HP, -4 arrows")
        hp(0, "edit", -15)
        inv(0, "edit", "item2", "arrow", 8)
        threeIce()
      if roll[1] == False:
        gameOver(threeStart)
  else:
    invalid(threeNorth)


def threeIce():
  choice = input(
    "You come across an underground bunker with a small man selling ice.  You ask him where you can find some treasure. He laughs and directs you west to a town called Gerudo. Do you follow her advice? yes, no \n"
  )
  if choice == "no":
    print(
      "You walk south until you reach a massive dust storm. You cannot see or breathe. You die. \n"
    )
    gameOver(threeStart)
  if choice == "yes":
    threeGerudo()
  else:
    invalid(threeIce)


def threeGerudo():
  choice = input(
    "You come across a walled town called Gerudo. It's leader is sitting on a throne straight ahead from the entrance. She notices you and comes running, screaming \"LINK!! YOU'RE BACK!\". She gives you a big hug and asks where you've been. You don't know, and you ask her who she is. She says her name is Urbosa. You ask about the treasure and she asks you to follow her. Do you go with? yes, no \n"
  )
  if choice == "no":
    print(
      "You run away from the strange woman, back the way you came. You trip and fall into a pit of quicksand. You die. \n"
    )
    gameOver(threeStart)
  if choice == "yes":
    threeBats()
  else:
    invalid(threeGerudo)


def threeBats():
  choice = input(
    "You follow her into a room underground, and she turns on the lights. 10 massive bats hang from the ceiling, and start to get angry. Are you ready to fight? yes,no \n"
  )
  if choice == "yes":
    if inv(0, "list", 0, 0, 0)[0] == "sword":
      print(
        "Begin boss fight. The dice will roll repeatedly until you either win or die. There are 10 bats to kill, and you need more than 10 per roll to kill one. You currently have "
        + str(hp(0, "list", 0)) + " HP, and Urbosa currently has " +
        str(hp(2, "list", 0)) + " HP. \n")
      i = 10
      while hp(0, "list", 0) > 0:
        while i >= 0:
          roll = dice(10)
          print("You rolled " + str(roll[0]))
          if roll[1] == False:
            hp(0, "edit", -10)
            print("The bat lives! -10 HP")
          if roll[1] == True:
            print("The bat dies! Remaining bats: " + str(i))
            i = i - 1
        if hp(0, "list", 0) == 0:
          gameOver(threeStart)
        if i <= 0:
          print("YOU WIN! You took a total damage of " +
                str(hp(0, "list", 0)) + " HP.")
          print(
            "Urbosa leads you to a chest, and gives you a mysterious orb. She says to give it to the Old Man. You never told her about him, but whatever. You take the orb, and travel back to the old man. \n"
          )
          sectComplete(3)
  if choice == "no":
    print("You run back to the oasis to prepare.")
    threeStart()
  else:
    invalid(threeBats)

 # ======SECTION FIVE======

# Start of section 5


def fiveStart():
    path = input(
        "\nYou go east towards a large open field.  The air smells crisp and the grass is damp with dew. In the distance, you see a lake and cabin. The cabin seems to be abandoned. Where do you go?\n \n CABIN \n \n LAKE \n \n"
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
        "\n The cabin door seems to be boarded shut. The windows seem to be boarded shut too. What do you want to do?\n \n BREAK \n \n LEAVE"
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
    breakBoard = input(
        "\nBreak it with what?\n \n FIST \n \n WEAPON \n"
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
        elif "weapon" in breakBoard.lower():
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

# Part two of the cabin path


def cabinPathPartTwo():
    choosePath = input(
        "The atmosphere is damp and dusty. To the left is a door frame. On the table in front of you are three cans. You're not sure if they're expired or not. Taking them may or may not be a good idea.\n TAKE \n \n DON'T \n"
    )

    if "take" in choosePath.lower():
        print(
            "\n Taking the cans"
        )
        cans()
        cabinPathDoorFrame()
    elif "don't" in choosePath.lower():
        print(
            "\nNot taking the cans."
        )
        cabinPathDoorFrame()
    else:
        invalid(cabinPathPartTwo)

# Enter the door frame or not?


def cabinPathDoorFrame():
    enterDoor = input(
        "Are you going through the doorframe?\n YES \n \n NO \n"
    )
    if "yes" in enterDoor:
        print(
            "entering the door"
        )
        cabinPathEnd()
    elif "no" in enterDoor:
        print(
            "leaving the cabin")
        fiveStart()
    else:
        invalid(cabinPathDoorFrame)

# End of the cabin path


def cabinPathEnd():
    while True:
        itemList = ["KNIFE", "CLOTHES", "LEAVE"]
        print(itemList)
        print(
            "\nYou enter the doorway. The room seems to be a bedroom. It has a nice set of clothes laid out on the bed, like it was waiting for you. On top of the drawer is a knife. The knife has some strange symbols inscribed on it.\n"
        )
        itemGrab = input(
            "What do you grab? \n \n" +
            itemList[0] + "\n \n" + itemList[1] +
            "\n \n" + itemList[2] + "\n \n"
        )
        if "knife" in itemGrab.lower():
            print(
                "Grabbing the knife."
            )
            # Popping it out doesn't work, figure out why
            itemList.pop(0)
            continue
            # This works, but since it's a loop, the user can keep gaining more and more health, sooooo.
        elif "clothes" in itemGrab.lower():
            print(
                "Grabbing the clothes. \n \n + 15HP"
            )
            hp(0, "edit", 15)
            # Popping doesn't work
            itemList.pop(1)
            continue
        elif "leave" in itemGrab.lower():
            print(
                "\nYou leave the cabin. You go back west, coming back to the open field\n"
            )
            fiveStart()
        else:
            invalid(cabinPathEnd)

# Cans - They deal either -5 or +5 HP


def cans():
    print("Theses are the cans")


# Part one of the lake path
def lakePath():
    path = input(
        "\nIn front of you lay a beautiful disc of blue. The clouds above reflected just as well as the trees beside the lake. In the middle of the lake is a small raft, with something unknown on it. On the shore of the lake, is a small building. \nWhere do you go?\n \n LAKE \n \n BUILDING\n\n"
    )
    if "lake" in path.lower():
        print(
            "\nGoing swimming in the lake.\n"
        )
        swimmingPath()
    elif "building" in path.lower():
        print(
            "\nGoing to the building\n"
        )
        buildingPath()
    else:
        invalid(lakePath)

# Swimming path, dead end


def swimmingPath():
    path = input(
        "\nYou take a nice swim in the lake, the water feels cool and refreshing. You're feeling kind of tired, you should probably go back to shore.\n\n SWIM \n\n GO BACK"
    )
    if "swim" in path.lower():
        print(
            "\nDespite feeling tired, you kept swimming. You feel something touch your leg, when. Oh no! A cramp! You try your best to swim back to shore, sucking in more water and more water. You feel as if you're about to make it to shore when something wraps around your leg. You get pulled into the lake by an unknown entity. The last image you see is the water-distorted sky.\n"
        )
        gameOver()
    elif "go back" in path.lower():
        print(
            "\nGoing back\n"
        )
        lakePath()
    else:
        invalid(swimmingPath)

# Building path, this is a one way, no escape


def buildingPath():
    path = input(
        "\nInside the building, which is surprisingly clean, there's a table with a fishing rod. Beside the table is a large raft and paddle.\n\n GRAB FISHING ROD \n\n GRAB RAFT\n\n"
    )
    if "fishing rod" in path.lower():
        print(
            "\nWhat are you gonna do with a fishing rod, huh?\n"
        )
        buildingPath()
    elif "raft" in path.lower():
        print(
            "\nYou pull the raft out of the building, and put it on the shore\n"
        )
        buildingPathPartTwo()
    else:
        invalid(buildingPath)

# Fight the sea monster or not?


def buildingPathPartTwo():
    path = input(
        "\nYou use the raft and go to the other raft on the lake. Once you start to get closer, you see what looks like a person on the raft. The person is unconscious. You bring them on your raft. Waking the person up, you ask them their name. 'Mipha', they answer. You're about to ask Mipha something else, when suddenly, something brushes against your boat. A giant sea monster pops out of the lake! What do you do?\n\n FIGHT \n\n PADDLE AWAY \n\n"
    )
    if "fight" in path.lower():
        print(
            "\nYou decide to stand your ground and fight the monster\n"
        )
        fightSeaMonst()
    elif "paddle" in path.lower():
        print(
            "\nYou start paddling away, but the sea monster grabs you, tearing you both apart.\n"
        )
        gameOver()
    else:
        invalid(buildingPathPartTwo)

# Fighting the sea monster


def fightSeaMonst():
    seaMonst = 100
    mipha = 65
    round = 1
    print(
        "\nYou and mipha fight the sea monster\n"
    )
    print("\n\n======ROUND 1======\n\n")
    while True:
        roll = dice(10)
        # Link's attack
        if roll[0] >= 10:
            print(
                "\nYou rolled a staggering " +
                str(roll[0]) + ", That means you dealt 20 HP to the monster!\n"
            )
            seaMonst = seaMonst - int(roll[0])
        elif roll[0] >= 5:
            print(
                "\nYou rolled " +
                str(roll[0]) +
                ", That means you only dealt 10 HP to the monster!\n"
            )
            seaMonst = seaMonst - int(roll[0])
        elif roll[0] < 5:
            print(
                "\nYou rolled a measly " +
                str(roll[0]) +
                ", That means you didn't even touch the monster. Come on, man.\n"
            )

        # Mipha's attack
        rollTwo = dice(10)
        if rollTwo[0] >= 10:
            print(
                "\nMipha rolled a staggering " +
                str(rollTwo[0]) +
                ", That means she dealt 30 HP to the monster!\n"
            )
            seaMonst = seaMonst - int(rollTwo[0])
        elif rollTwo[0] >= 5:
            print(
                "\nMipha rolled " +
                str(rollTwo[0]) +
                ", That means she dealt 15 HP to the monster!\n"
            )
        elif rollTwo[0] < 5:
            print(
                "\nMipha rolled a measly " +
                str(rollTwo[0]) +
                ", That means she didn't even touch the monster.\n"
            )

        # Sea monsters attack
        rollThree = dice(15)

        # High dmg sea monster attack
        if rollThree[0] >= 15:
            print(
                "\nThe monster hit you both swiftly and hard. -15 HP to both\n"
            )
            hp(0, "edit", -15)
            if int(hp(0, "list", 0)) == 0:
                print(
                    "\nThe sea monster tore you both apart. Womp Womp.\n"
                )
            mipha = mipha - 15
            if mipha <= 0:
                print("Mipha is dying!!!!!")

            # Low dmg sea mosnter attack
        elif rollThree[0] < 15:
            print(
                "\nThe monster swings at you wildly, -5 HP to both.\n"
            )
            hp(0, "edit", -5)
            if int(hp(0, "list", 0)) == 0:
                print(
                    "\nThe sea monster tore you both apart. Womp Womp.\n"
                )
            mipha = mipha - 5
            if mipha <= 0:
                print("Mipha is dying!!!!!")

        round = round + 1
        print("\n\nNext round here we go!\n\n")
        time.sleep(5)
        print("MONSTER HEALTH = " + str(seaMonst))
        print("\n\n====== ROUND " + str(round) + " ======")

        # Ending of section 5, I would've put it in it's own function, but this is easier.
        if seaMonst <= 0:
            print(
                "\nThrashing wildly, the sea monster slithers back into the lake.\n"
            )
            if int(hp(0, "list", 0)) > 0:
                if mipha > 0:
                    print(
                        "\nAfter dealing one last blow to the monster, it finally shrinks back into the lake. You and Mipha both survive. 'Finally, I've been waiting to give you this', says Mipha. She gives you some treasure and some apples for good measure. You leave, and she decides to stay.\n"
                    )
                    sectComplete(5)
            elif int(hp(0, "list", 0)) > 0:
                if mipha <= 0:
                    print(
                        "\nYou're about to finally kill the sea monster, when it hits Mipha. You hit the sea monster one last time, making it finally slither back into the lake. Mipha, with her last dying breath, gives you the treasure. You leave her lifeless body on the raft.\n"
                    )
                    sectComplete(5)
        else:
            continue


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
