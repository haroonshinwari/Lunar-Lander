'''HAROON SHINWARI - hshinw01
   This is a game by the name of Lunar Lander -
   in which the user is the pilot of a lunar lander about to land on the moon-
   and the aim of the game is to land safely on the moon -
   you do this by choosing how much fuel to burn -
   the game begins with you in the air being pulled towards the moon by gravity -
   and you decide every turn how much fuel to burn which slows down your speed-
   In order to land safely you have to burn the right amount of fuel at the right time-
   '''

print('Hi, welcome to my first game on Python, The Lunar Lander.\nThis is a fairly simple game. You are on a lunar lander about to land on the moon.\nYou start off 1000m of altitude above the moon with 1000 litres of fuel.\nGravity is a force that acts on you, increasing the velocity in the direction of the moon.\nYou must decide how much fuel to burn at each turn, which will slow down your velocity.\nThe aim of the game is to land safely on the moon without burning all your fuel.\nThis can only be done by reaching an altitude of 0 or less at a velocity of 10m/s or less. \nGOOD LUCK !!! ')  

def play():

    # setting up the initial variables
    altitude = 1000    #this is the altitude above the moon(distance from the moon in metres)
    velocity = 0       #the speed at which the lunar lander is moving(starts with 0, neither rising nor falling and can be negative)
    fuel = 1000        #this is the amount of fuel left in litres	
    burn = 0           #this is the amount the user has chosen to burn           
    OFFSET = 0.25      #this is the constant that determines how the fuel burnt affects the velocity 
    GRAVITY = 1.6      #this is the rate at which the force of gravity is pulling the lunar towards the moon  

    print('Starting altitude = 1000  starting velocity = 0 starting fuel = 1000')
    while altitude > 0:
        burn = int(input("Enter fuel to burn: "))
        if burn <= 0:
            burn = 0
        if burn > fuel:
            burn = fuel


        velocity += GRAVITY
        velocity -= OFFSET*burn
        altitude -= velocity
        fuel -= burn
        print('Altitude is: ' + str(altitude) + '  Velocity is: ' + str(velocity) + '  Fuel is: ' + str(fuel))

    if velocity <=10:
        altitude = 0
        print('Altitude is: ' + str(altitude) + '  Velocity is: ' + str(velocity) + '  Fuel is: ' + str(fuel))
        print('Safe Landing, Well done, YOU WIN!')
    else:
        print('Altitude is: ' + str(altitude) + '  Velocity is: ' + str(velocity) + '  Fuel is: ' + str(fuel))
        print('You blasted into the crater of the MOON! YOU LOSE!')
play()

#while loop requesting if the player wants to play again
while True:
    answer = input('Would you like to play again? (Please enter Y or y if yes and type N or n if no): >')
    if answer == 'Y' or answer == 'y':
        play()
    elif answer == 'N' or answer == 'n':
        print('Thank you for your time, I hope you enjoyed playing this game')
        break
    else:
        print('Please enter Y or y if you would like to play again or /n please enter N or n to stop playing')
