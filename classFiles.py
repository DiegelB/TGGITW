

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

  def __init__(self, attack=0, defense=0, health=100, name="Bad Guy"):
    self.attack = attack
    self.defense = defense
    self.health = health
    self.name = name

  def chooseEnemy():
    randNum = random.randint(1,5)
    if randNum == 1:
      return "Goblin"
    elif randNum == 2:
      return "Skeleton"
    elif randNum == 3:
      return "Ghost"
    elif randNum == 4:
      return "Cyclops"
    elif randNum == 5:
      return "Godzilla"








