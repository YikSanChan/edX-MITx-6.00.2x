import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    pRabbitRepro = 1 - CURRENTRABBITPOP / float(MAXRABBITPOP)
    newRabbit = sum([random.random() < pRabbitRepro for i in range(CURRENTRABBITPOP)])
    if CURRENTRABBITPOP + newRabbit > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    else:
        CURRENTRABBITPOP += newRabbit

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if CURRENTFOXPOP >= 10:
        pFoxEat = CURRENTRABBITPOP / float(MAXRABBITPOP)
        newFox = 0
        noHuntFox = 0
        checkedFox = 0
        while checkedFox < CURRENTFOXPOP and CURRENTRABBITPOP > 10:
            checkedFox += 1
            # succeed in hunting
            if random.random() < pFoxEat:
                CURRENTRABBITPOP -= 1
                # succeed in giving birth
                if random.choice([1,2,3]) == 1:
                    newFox += 1
            # fail hunting
            else:
                noHuntFox += 1
        # unchecked foxes are all nohunting foxes
        unCheckedFox = CURRENTFOXPOP - checkedFox
        mayDieFox = unCheckedFox + noHuntFox
        dieFox = sum([random.random() < 0.1 for i in range(mayDieFox)])
        finalFox = CURRENTFOXPOP + newFox - dieFox
        if finalFox < 10:
            finalFox = 10
        CURRENTFOXPOP = finalFox

    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit = []
    fox = []

    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit.append(CURRENTRABBITPOP)
        fox.append(CURRENTFOXPOP)

    return (rabbit, fox)

