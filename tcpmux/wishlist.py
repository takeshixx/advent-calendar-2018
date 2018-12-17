#!/usr/bin/env python3
import sys
import time
ascii_art = """                  _..._
                ,'     `.
               Y        |
               |      _/
               |
               |
           ,--'_`--.
           |_______|
        _.-'""   ""`-._
     ,-"               "-.
   ,'                     `,
  /                         \
 |                           |
|                             |
|  Santa's wishlist service!  |
|                             |
|                             |
 |                           |
  \                         /
   `.                     ,'
     `._               _,'
        `--.._____..--'
"""
print(ascii_art)
print('Welcome to Santa\'s wishlist service!')
print('A new wishlist has been created for you.')
print('Please add new items to your list, or write KKTHXBYE to finish your list:')
sys.stdout.flush()
wishlist = []
timeout = time.time() + 60 * 1
while True:
    if time.time() > timeout:
        break
    item = sys.stdin.readline().strip()
    if item == 'KKTHXBYE':
        break
    wishlist.append(item)
print('Santa received the following list:')
for i in wishlist:
    print('\t' + i)
print('Let\'s see what Santa can do for you, bye bye!')
print('x16oEoflwf7/hZCehWW3v/Vm22yOZfn3gI/o6M11G2uKSD9aISch3P16dPgD50I6')
sys.stdout.flush()
