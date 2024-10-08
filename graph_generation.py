from igraph import Graph
import random


def generate_graph():
    numOfVertices = int(input("number of vertices: "))
    energy = numOfVertices * 10
    numbersGenerator = []
    count = 0
    while count < numOfVertices:
        numbersGenerator.append(count)
        count += 1

    connections = int(input("probability of connections out of 100: "))
    chance = connections

    edgesList = []
    for x in numbersGenerator:
        for y in numbersGenerator:
            if y > x:
                if random.randint(1, 100) > chance:
                    edgesList.append([x, y])

    graph = Graph(n=0)
    graph.add_vertices(numbersGenerator)
    graph.add_edges(edgesList)
    adjList = graph.get_adjlist()

    network = []
    bottom_range = float(input("bottom range of certainty [0-1]: "))
    top_range = float(input("top range of certainty [0-1]: "))
    for i, neighbours in enumerate(adjList):
        if i % 2 == 0:
            network.append({'ajList': neighbours, 'certainty': random.uniform(bottom_range, top_range), 'vote': 0, 'red followers': 1})
        else:
            network.append({'ajList': neighbours, 'certainty': random.uniform(bottom_range, top_range), 'vote': 1, 'red followers': 1})

    numOfGrey = int(input("number of grey agents: "))
    numOfGreySpies = int(input("number of grey red spies: "))
    greyList = []

    for i in range(numOfGrey):
        greyList.append(i)

    redAgents = random.sample(greyList, numOfGreySpies)

    while True:
        player_selection = str(input("Do you want to run a simulation?[Y/N]: ")).upper()
        if player_selection != 'Y':
            if player_selection != 'N':
                print("Enter valid input!")
                continue
            break
        break

    while True and player_selection == 'N':
        player_selection = str(input("Do you want to play as Red or Blue?[R/B]: ")).upper()
        if player_selection != 'R':
            if player_selection != 'B':
                print("Enter valid input!")
                continue
            break
        break

    print("Game initialisation done, start!\n")
    print(player_selection)

    return network, energy, greyList, redAgents, player_selection
