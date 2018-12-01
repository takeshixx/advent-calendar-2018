#!/usr/bin/env python3
import sys
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
|  Santa's wichlist service!  |
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
while True:
    item = sys.stdin.readline().strip()
    if item == 'KKTHXBYE':
        break
    wishlist.append(item)
print('Santa received the following list:')
for i in wishlist:
    print('\t' + i)
print('Let\'s see what Santa can do for you, bye bye!')
sys.stdout.flush()
