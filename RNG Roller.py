import random
import colorama
from colorama import Fore
import numpy as np
score = 0
target = 0
PL=input('Do you want to play? ')
if PL=='yes' or PL=='y':
  PA=input('If you are okay with partial gambling type okay ')
  while PA=='okay':
    
    letters = ['a','o','e','i']
    print('')
    print('This is the item rolling program')
    print(Fore.WHITE + "Normal objects are colored in white")
    print(Fore.GREEN + "Rare objects are colored in green")
    print(Fore.YELLOW + "Legendary objects are colored in yellow")
    print(Fore.CYAN + "Chromatic objects are colored in cyan")
    print(Fore.RED + "Ultrachromatic objects are colored in red")
    
    n = ['rock','apple','rubber','piece of paper','pencil']
    r = ['book','penny','pen','baseball cap','baguette']
    l = ['phone','bookshelf full of books','sweet treat','pair of new trainers']
    c = ['computer','diamond','gold bar','potted plant']
    uc = ['ring galaxy','Mona Lisa painting','rainbow eucalyptus','infinite capacity bag']
    items = [n,r,l,c,uc]
    
    a = int(input(Fore.BLUE + 'How many rolls do you want; [5] [10] [50] or [100] '))
    print('')
    if a==5:
      target=100
    elif a==10:
      target=400
    elif a==50:
      target=1500
    elif a==100:
      target=3000
    else:
      target=0
      
    while a>0:
      item_choice = random.choice(items)
      if item_choice == n and item_choice[1] == letters:
        print(Fore.WHITE + 'You got an ',random.choice(item_choice))
        score = score + 10
      elif item_choice == n and item_choice[1] != letters:
         print(Fore.WHITE + 'You got a ',random.choice(item_choice))
         score = score + 10
      elif item_choice == r:
        print(Fore.GREEN + 'You got a ',random.choice(item_choice))
        score = score + 20
      elif item_choice == l:
        print(Fore.YELLOW + 'You got a ',random.choice(item_choice))
        score = score + 30
      elif item_choice == c:
        print(Fore.CYAN + 'You got a ',random.choice(item_choice))
        score = score + 50
      elif item_choice == uc:
        print(Fore.RED + 'You got a ',random.choice(item_choice))
        score = score + 100
      elif item_choice == uc and item_choice[1] == letters:
        print(Fore.RED + 'You got an ',random.choice(item_choice))
        score = score + 100
      a-=1
    print(Fore.WHITE + 'In total you got a score of',score)
    
    if score>target:
      print('Good job, you reached your target of ',target,'!')
      print('')
      score=0
    elif score<target:
      print('Better luck next time on achieving your target of ',target,'!')
      print('')
      score=0
  else:
    print('See you around,_,')

elif PL=='no' or PL=='n':
  print('See you around,_,')
