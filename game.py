import time

import blue_agent
import green_agent
import grey_agent
import red_agent


def game(network, blue_energy, totalPeople, greyList, redAgent, player_selection):
    game_over = False
    grey_chosen = False
    grey_choice = ''
    grey_active = False
    is_grey = 0

    if player_selection == 'Y':
        count = 0
        while not game_over:
            total_votes = get_stats(network, 'vote')
            network = red_agent.red_AI(network, total_votes)
            time.sleep(1)
            print("Red just played!")
            network, blue_energy, game_over, is_grey, grey_chosen = blue_agent.blue_AI(network, game_over, blue_energy, total_votes, is_grey, grey_chosen)
            if is_grey == 1 and grey_chosen == False:
                grey = grey_agent.grey(greyList, redAgent)
                if grey == 'blue':
                    blue_agent.blue_grey(network)
                elif grey == 'red':
                    red_agent.red_grey(network)
                grey_chosen = True
            time.sleep(1)
            print("Blue just played!")
            network = green_agent.green(network)
            time.sleep(1)
            print("Green just played!")
            count += 1
        total_votes = get_stats(network, 'vote')
        total_non_votes = totalPeople - get_stats(network, 'vote')
        print("===============================================================================")
        print("Game is over! the winner is " + get_winner(total_non_votes, total_votes), "in", count, "turns")
        print("There are " + str(get_stats(network, 'vote')) + " out of " + str(
            totalPeople) + " voters")
        print("===============================================================================")



    print("===============================================================================")
    print("Currently, there are " + str(get_stats(network, 'vote')) + " out of " + str(
        totalPeople) + " voters after this round")
    print("Current blue energy is: ", blue_energy)
    print("Current Red Followers: " + str(get_stats(network, 'red followers')))
    print("===============================================================================")
    while not game_over:
        network = red_agent.red(network)
        while not grey_chosen:
            grey_choice = str(input("Do you wish to bring in a Grey agent? [Y/N]: ")).upper()
            if grey_choice != 'Y':
                if grey_choice != 'N':
                    print("Enter valid input!")
                    continue
                break
            else:
                grey_chosen = True
                break

        if grey_choice == 'Y' and grey_active == False:
            grey = grey_agent.grey(greyList,redAgent)
            if grey == 'blue':
                blue_agent.blue_grey(network)
            elif grey == 'red':
                red_agent.red_grey(network)
            grey_active = True
            network = green_agent.green(network)
            print("Green played!")
            print("===============================================================================")
            print("Currently, there are " + str(get_stats(network, 'vote')) + " out of " + str(
                totalPeople) + " voters after this round")
            print("Current blue energy is: ", blue_energy)
            print("Current Red Followers: " + str(get_stats(network, 'red followers')))
            print("===============================================================================")
            continue

        network, blue_energy, game_over = blue_agent.blue(network, blue_energy, game_over)
        network = green_agent.green(network)
        print("Green played!")
        print("===============================================================================")
        print("Currently, there are " + str(get_stats(network, 'vote')) + " out of " + str(
            totalPeople) + " voters after this round")
        print("Current blue energy is: ", blue_energy)
        print("Current Red Followers: " + str(get_stats(network, 'red followers')))
        print("===============================================================================")
    total_votes = get_stats(network, 'vote')
    total_non_votes = totalPeople - get_stats(network, 'vote')

    print("Game is over! the winner is " + get_winner(total_non_votes, total_votes))


def get_stats(network, key):
    count = 0
    for i, node in enumerate(network):
        if key == 'vote':
            if node[key] == 1:
                count += 1
        elif key == 'red followers':
            if node[key] == 1:
                count += 1
    return count


def get_winner(totalNonVotes, totalVotes):
    if totalVotes < totalNonVotes:
        return 'Red'
    return 'Blue'


def avg_uncertainty(network):
    total_nodes = len(network)
    tmp = 0
    for i, node in enumerate(network):
        tmp += node['certainty']
    return tmp / total_nodes
