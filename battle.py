import random
from classFiles import Enemy


enemy = Enemy()
def battleFunc(player):
  enemyType = enemy.chooseEnemy()
  print(enemyType)