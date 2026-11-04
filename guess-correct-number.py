import random
j=random.randint(1,100)
g=int(input('guess a number 1 to 100 :'))
c=1
while g!=j:
      if g<j:
         print('guess higher')
      else:
         print('guess lower')
      g=int(input('guess again'))
      c=c+1
else:
  print('guess is  correct')
  print('attempts',c)
