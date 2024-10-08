import random


def grey(greyList, redAgents):
    greyPicked = random.choice(greyList)

    if greyPicked in redAgents:
        print("grey turns out to be a red spy!")
        greyList.remove(greyPicked)
        redAgents.remove(greyPicked)
        return "red"
    else:
        print("grey turns out to be a blue diplomat!")
        greyList.remove(greyPicked)
        return "blue"
