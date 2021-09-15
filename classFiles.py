import random

class Player():

  def __init__(self,
               name='User',
               attack=10,
               defense=5,
               health=100,
               coins=0):
    self.name = name
    self.attack = attack
    self.defense = defense
    self.health = health
    self.coins = coins

  def getName(self):
    playerInput = 'n'
    while(playerInput == 'n'):
      print("Hello adventurer, what is thy name?")
      self.name = input(">>")
      print("You said " + self.name + " is that correct? Y/N")
      playerInput = input(">>")
      playerInput = playerInput.lower()

  def checkStats(self):
    print("--Your stats my lord--")
    print("Name: " + self.name +
          "\nAttack: " + str(self.attack) +
          "\nDefense: " + str(self.defense) +
          "\nHealth: " + str(self.health) +
          "\nCoins: " + str(self.coins))
    input("Enter to continue")

class Enemy():

  def __init__(self, name="Bad Guy", attack=0, defense=0, health=100):
    self.attack = attack
    self.defense = defense
    self.health = health
    self.name = name

  def createEnemy(self, level):
    enemyNames = ["Goblin", "Skeleton", "Ghost", "Cyclops", "Zombie"]
    self.name = random.choice(enemyNames)
    if level == "1":
      self.attack = random.randint(1,3)
      self.defense = random.randint(1,3)
      self.health = 30
    elif level == "2":
      self.attack = random.randint(3,5)
      self.defense = random.randint(3,5)
      self.heatlh = 50
    elif level == "3":
      self.attack == random.randint(5,10)
      self.defense == random.randint(5,8)
      self.heatlh == 100


    

    









