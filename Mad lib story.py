
print("This is a madlib generator coded by Chandan S Gowda")

color = input("Give me a colour >>  ").capitalize()
pnoun = input("Give me a plural noun  >>  ").capitalize()
gender = input("Your gender  [male/female/other] >>  ").lower()


if gender == "male" :
      print("Bold man! ")
      celeb = input("Your favorite celebrity  >>   ").capitalize()

elif gender == "female" :
      print("Hello Beauty !")
      celeb = input("Your favourite celebrity  >>  ").capitalize()

elif gender == "other" :
      print("Greetings !")
      celeb = input("Your favourite celebrity >>   ").capitalize()

else :
      print("You entered a wrong value.Try again !")

print(f"Roses are {color}")
print(f"{pnoun} are Blue")
print("I love you")
print(celeb)
