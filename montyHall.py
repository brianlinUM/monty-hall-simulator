'''
Simulates the Monty Hall game and finds the success rate for the player
switching and not switching doors.
'''

from random import choice


# game parameters
NUM_DOORS = 3
TOTAL_NUM_GAMES = 100000


def randomDoors():
    winningDoor = choice(range(NUM_DOORS))
    losingDoors = [i for i in range(NUM_DOORS) if i != winningDoor]
    return winningDoor, losingDoors


def game(isSwitchFirstChoice):
    # initial game state
    winningDoor, losingDoors = randomDoors()

    # player randomly makes a choice
    playerFirstChoice = choice(range(NUM_DOORS))
    notChosenDoors = [i for i in range(NUM_DOORS) if i != playerFirstChoice]

    # host reveals any door that is not winning and not chosen by player
    hostRevealedDoor = choice(
        [door for door in notChosenDoors if door != winningDoor]
    )
    notChosenDoors.remove(hostRevealedDoor)
    remainingDoor = notChosenDoors[0]

    finalChoice = remainingDoor if isSwitchFirstChoice else playerFirstChoice
    return finalChoice == winningDoor


def playGames(alwaysSwitch):
    winCount = 0
    for i in range(TOTAL_NUM_GAMES):
        if game(alwaysSwitch):
            winCount += 1
    return winCount


neverSwitchWinRate = playGames(False) / TOTAL_NUM_GAMES
alwaysSwitchWinRate = playGames(True) / TOTAL_NUM_GAMES

print(f"Not switch success: {neverSwitchWinRate * 100}%")    
print(f"Switch success: {alwaysSwitchWinRate * 100}%")
