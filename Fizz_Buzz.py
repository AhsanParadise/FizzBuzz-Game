
# ----------- F i z z B u z z  G a m e ----------#
+++

FizzBuzz = input('Type a number: ')

if (float(FizzBuzz) % 3 == 0) and (float(FizzBuzz) % 5 == 0):
    print('F i z z B u z z')
elif float(FizzBuzz) % 3 == 0:
    print('F i z z')
elif float(FizzBuzz) % 5 == 0:
    print('B u z z')
else:
    print(''' 
 z
  zz
   zzz
    zzzz
     zzzzz
      zzzzzz
       zzzzzzz
Sorry invalid number. Try 5, 6, 15, 20, 25, -15..........
Thanks for playing this hilarious game. This game is very important for you.

    ''')
