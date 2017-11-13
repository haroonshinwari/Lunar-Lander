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
fuel = 1000        #this is the amount of fuel left in litres	
burn = 0
OFFSET = 0.15
GRAVITY = 1.6

while altitude > 0:
    burn = int(input("Enter fuel to burn: "))
    if burn < 0:
        burn = 0
    if burn > fuel:
        burn = fuel
    if burn < fuel:
        burn = fuel

    velocity += GRAVITY
    velocity -= OFFSET*fuel
    altitude -= velocity
    fuel -= burn
    print('Altitude is:' + int(altitude), 'Velocity is: ' + int(velocity) + 'Fuel is: ' + int(fuel))

if velocity <=10:
    print('Safe Landing, Well done, YOU WIN!')
else:
    print('You blasted into the crater of the MOON! YOU LOSE!')
