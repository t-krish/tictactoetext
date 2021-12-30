import random
print('You are player 1')
open_spaces=['?', '!', '$', '&','^','*','(','#',')']
while True:
  botmove=random.randint(0,len(open_spaces)-1)
  playermove=input('Enter the box no. you would like to play in. Count from left to right, top to bottom.  ')
  playermove=int(playermove)
  open_spaces[playermove-1]= '1'
  if playermove == botmove:
    botmove=random.randint(0,len(open_spaces)-1)
  elif open_spaces[botmove-1]=='1':
    botmove=random.randint(0,len(open_spaces)-1)
  else:
    print('Valid')
  open_spaces[botmove-1]='0'
  print('\n')
  print(open_spaces[0:3])
  print(open_spaces[3:6])
  print(open_spaces[6:9])
  print('\n')
  if open_spaces[0] == open_spaces[1]:
    if open_spaces[1] == open_spaces[2]:
      if open_spaces[2] == '1':
        print('Congrats. You won.')
      elif open_spaces[2] == '0':
        print('Bot won.')
      break
  if open_spaces[3] == open_spaces[4]:
      if open_spaces[4] == open_spaces[5]:
        if open_spaces[4] == '1':
          print('Congrats. You won.')
        elif open_spaces[4] == '0':
          print('Bot won.')
        break
  if open_spaces[6] == open_spaces[7]:
    if open_spaces[7] == open_spaces[8]:
      if open_spaces[8] == '1':
        print('Congrats. You won.')
      elif open_spaces[4] == '0':
        print('Bot won.')
      break
    