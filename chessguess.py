#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


print("""Welcome to the guessing chess board's colour training. 
A random coordinate will be randomly generated, please enter 'w' if you think the cell is white 
and 'b' if you think the cell is black.

To exit the game enter 'n'
at the end of the game you will be given a score
""")

ranklist = ['a','b','c', 'd', 'e', 'f', 'g', 'h']

guess = ''
op_count = 0
score_count = 0

while guess != 'n':
    file = str(random.randint(1,8))
    rank = random.choice(ranklist)
    rand = rank+file
    print(rand)
    guess = input('guess: ')

    ans = ''

    if rand in ('a1', 'c1', 'e1', 'g1', 'b2', 'd2', 'f2', 'h2', 'a3', 'c3', 'e3', 'g3', 'b4', 'd4', 'f4', 'h4', 'a5', 'c5', 'e5','g5', 'b6', 'd6', 'f6', 'h6', 'a7', 'c7', 'e7', 'g7', 'b8', 'd8', 'f8', 'h8'):
        ans = 'b'
    else:
        ans = 'w'
    op_count += 1
    if ans == guess:
        score_count += 1
        print('Yes!')
        
    elif ans == 'n':
        print('Thank you for playing')
    else:
        print('incorrect')

    print('-'*100)
percent = round(score_count/(op_count-1)*100, 2)
print("You scored {}/{} or ≃ {}%".format(score_count,op_count-1, percent))

input("type anything and press enter to close the program")

