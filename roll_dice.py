import random


x = random.randint(1, 6)
y = random.randint(1,6)

enter = input("Press enter to roll the dice  ")

print(f"({x}, {y})")

a = lambda a, b : a + b
b = a(x,y)
print(f"SUM >>  {b}")
