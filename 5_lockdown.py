'''
PROBLEM 5. SECOND LOCKDOWN (October--December 2020)

Check out this COVID spread simulator[1] by the Washington Post.  Cool, right?
[1]https://www.washingtonpost.com/graphics/2020/world/corona-simulator/


Part 1. Viral spread under different lockdown policies

In this problem, you'll make your own simulator of viral spread with different
distancing guidelines.  Specifically, we'll consider the following policies:
- totally free movement
- restricted movement (only some of the population doesn't move)
- restricted movement (most of the population doesn't move)
Come find me and discuss what you notice.


Part 2. Viral spread with limited contageousness

Re-implement your solutions from Part 1 (in a new script) to account for limited
contageousness (`h`), as in Part 3 of PROBLEM 1.  How does this change the
spread?


Part 3. Expand and expound

There's a lot of room to build on this basic model.  Do something creative (but
do it in a new file, so I can still see your solutions to Parts 1 and 2).  Here
are some ideas for inspiration:
- Assume that transmission occurs only with some probability, even if two people
  do come in close contact.
- Assign each person in the population an age, and make those probabilities
  age-dependent.  What happens when you change the demographics of the
  population such that the average age is very young or very old?
- Shape the room (rectangular by default) in such a way as to minimize
  transmission.  Formalize (abstractly) what kind of room shape is best.
'''


import pygame   # to show people interacting


###
# CONSTANTS

WHITE = (255, 255, 255)     # colors
RED = (255, 0, 0)
GREEN = (0, 160, 0)
PURPLE = (95, 158, 160)

WIDTH = 600     # screen size
HEIGHT = 400
P_RADIUS = 4    # size of a person (circle) on the screen


###
# CLASSES

class World:

    def __init__(self, num_people, num_infected):
        '''
        - initialize `num_people` people at random positions (use
          `numpy.random.randint(high)` to get a random integer less than `high`,
          but remember to import the package `numpy` first)
        - start with `num_infected` people initially infected
        - store all the people in an instance variable
        '''
        pass

    def on_timestep(self):
        self.update_infection_statuses()

        self.update_positions()
        self.handle_interactions()
        '''
        anything else you want to do on each timestep
        '''

    def update_infection_statuses(self):
        '''
        - update everybody's infection status (i.e., mark the person as
          recovered if they've been sick for `h` days, as in 
        '''

    def update_positions(self):
        '''
        - update everybody's position at each timestep
        '''
        pass

    def handle_interactions(self):
        '''
        - handle virus-transmitting interactions, if there are any
        '''
        pass


class Person:

    def __init__(self):
        '''
        - position
        - velocity
        - infection status (healthy, infected, or recovered)
        '''
        pass
    
    def update_position(self):
        '''
        - increment position by velocity on each timestep
        - prevent from moving out of the screen
        - handle "collisions" (interactions) between people (specifically, if an
          infected person comes within `min_distance` meters of )
        '''
        pass
    
    # class methods
    def are_interacting(p1, p2, min_distance=8):
        '''
        return whether two people are close enough to transmit COVID (cf. your
        implementation of `are_they_properly_distanced(person1, person2,
        min_distance=2)` in the SOCIAL DISTANCING problem).

        n.b. that all the units here are in pixels, not meters (we could scale
        everything to make these values look the same, but then people would
        look too small, I think).  So `min_distance=8` 
        '''
        pass



###
# DISPLAY

# initialize the display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# initialize a world with 30 people, 3 of whom are infected
world = World(30, 3)

done = False
while not done:  # on each timestep:

    # handle ending the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # update everybody's position, check for 
    world.on_timestep()

    screen.fill(WHITE)

    # draw each `Person` in the `World` on the screen
    '''
    You'll want something like `pygame.draw.circle(...)` below, but you'll need
    to substitute real values for `COLOR` (indicating the person's infection
    status) and `(X, Y)` (a tuple carrying the person's position), both of which
    should be instance variables in `Person`. `screen` (the window that you're
    drawing to) and `P_RADIUS` (the size of the dot that represents each people)
    are already defined, so you can leave them alone.

    Your code should look something like this:
    '''
    # for person in world.people:
    #     pygame.draw.circle(screen, COLOR, (X, Y), P_RADIUS)




    # YOUR CODE HERE


    

    # refresh the display
    pygame.display.update()

    # do a 10ms delay
    pygame.time.wait(10)

# end the simulation after you've closed the window
pygame.quit()
