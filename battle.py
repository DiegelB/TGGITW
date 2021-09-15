import random
from classFiles import Enemy

def battleFunc(player):
  enemy = Enemy()
  level = input("Welcome to the dungeon. Easy(1) Med(2) Hard(3)\n>>")
  enemy.createEnemy(level)
  while player.health != 0:
    choice = input("\nYou've just encountered a " + enemy.name + "! Their attack is " + str(enemy.attack) + 
                   "\nWhat do you do?" +
                   "\n1.Fight!" +
                   "\n>>")
    if choice == "1":
      print("\nYou're attack = " + str(player.attack) + "." +
            "\n" + enemy.name + "'s defense = " + str(enemy.defense) +
            "\n" + enemy.name + "'s health = " + str(enemy.health))
      enemyDamage = player.attack - enemy.defense
      enemy.health -= enemyDamage
      input(enemy.health)

  
  