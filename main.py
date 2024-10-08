import game
import graph_generation
import green_agent


def main():
    network, blue_energy, greyList, redAgents, player_selection = graph_generation.generate_graph()
    totalPeople = len(network)

    game.game(network, blue_energy, totalPeople, greyList, redAgents, player_selection)

main()