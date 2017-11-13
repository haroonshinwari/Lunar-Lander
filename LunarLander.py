'''HAROON SHINWARI - hshinw01
   This is a game by the name of Lunar Lander -
   in which the user is the pilot of a lunar lander about to land on the moon-
   and the aim of the game is to land safely on the moon -
   you do this by choosing how much fuel to burn -
   the game begins with you in the air being pulled towards the moon by gravity -
   and you decide every turn how much fuel to burn which slows down your speed-
   In order to land safely you have to burn the right amount of fuel at the right time-
   Then your description of what the program does.'''
   
# setting up the initial variables
altitude = 1000    #this is the altitude above the moon(distance from the moon in metres)
velocity = 0       #the speed at which the lunar lander is moving(starts with 0, neither rising nor falling)
fuel = 1000		   #this is the amount of fuel left in litres	
burn = 0

while altitude > 0:
	burn = float(input("Enter fuel to burn (0 - 1000)?"))
  	if burn < 0:
        burn = 0
    if burn > 1000:
        burn = 1000
    if burn > fuel:
        burn = fuel


else: