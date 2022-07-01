import random

def findOccurrences(s, ch):                                                                   #find more than one occurance
  pos=[]
  for i in range(0,len(s)):
    if ch==s[i]:
      pos.append(i)
  return pos

lives=6
right_guess=0
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", 'dog', 'bat']
ind = random.randrange(0,len(word_list), 1)                                                    #to pick a random word
chosen_word = word_list[ind]

blanks=['_']*len(chosen_word)                                                                  #generating blanks
print(blanks)
print(stages[-1])
while '_' in blanks:
  guess = input('Guess a letter! ').lower()
  if guess in chosen_word:
    results=findOccurrences(chosen_word,guess)
    for i in range(0,len(results)):
      blanks[results[i]]=guess
    right_guess+=1
    print(blanks)
    if '_' not in blanks:
      print('You won!')
      break
  else:
    print(stages[lives-1])
    lives-=1
    if lives==0:
      print('Game Over')
      break
