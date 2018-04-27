import random
state=("проиграли", "победили")
score= random.randint(4,20)
scoreBot= random.randint(4,20)
class Game:
 isWin = 0
 def getCard(self):
  return random.randint(2,10)
 def AI(self):
  if scoreBot<19: scoreBot+=getCard()
 def getResult(self):
  if score>scoreBot: isWin=1
  else: isWin=0
  if score>21: isWin=0
  print("У противника ",scoreBot," очков, у вас ", score)
  print("Вы ", state[isWin])
  print("-------------")
game=Game()
choose =''
while choose !='e':
 if score>21:  game.getResult()
 print("У вас ", score," очков.")
 choose=input("взять карту? (+)")
 if choose=='+':
  score+=game.getCard()
 else:
  game.getResult()
  score=random.randint(4, 20)
  scoreBot=random.randint(4, 20)
