import random


def blue(graph, energy, game_over):
    while True:
        user_input = str(input("Select level of potency message for blue [1,2,3,4,5]: "))
        if user_input.isnumeric():
            user_input = int(user_input)
            if 0 < user_input < 6:
                break
        print("Enter valid input!")
        print("===============================================================================")
        continue

    choice = user_input / 100

    for node in graph:
        if node['vote'] == 1:
            node['certainty'] += 0.05
            energy -= int(user_input / 2)
            continue
        if node['red followers'] == 0 and blue_vote_change(node['certainty'], user_input):
            node['vote'] = 1
            node['certainty'] += 0.05

        node['certainty'] += choice
        if node['red followers'] == 0:
            node['certainty'] += choice
        certainty = node['certainty']

        if blue_vote_change(certainty, user_input) and node['vote'] != 1:
            node['vote'] = 1

        node['certainty'] = node_certainty_check(node['certainty'])
        energy -= user_input

        if energy <= 0:
            game_over = True
            break

    return graph, energy, game_over


def blue_grey(graph):
    choice = 0.05

    for node in graph:
        if node['vote'] == 1:
            node['certainty'] += 0.001
            continue
        if node['red followers'] == 0 and blue_vote_change(node['certainty'], 5):
            node['vote'] = 1
            node['certainty'] += 0.01

        node['certainty'] += choice
        if node['red followers'] == 0:
            node['certainty'] += choice
        certainty = node['certainty']

        if blue_vote_change(certainty, 5) and node['vote'] != 1:
            node['vote'] = 1

        node['certainty'] = node_certainty_check(node['certainty'])

    print("Grey did not use blue energy!")
    return graph


def random_uncertainty(choice):
    return random.uniform(0, choice)


def blue_vote_change(certainty, blue_message):
    vote_chance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    count = 0
    new_certainty = int(certainty * 10)
    if certainty > 0.5:
        count = random.sample(vote_chance, blue_message).count(1)
    else:
        count = random.sample(vote_chance, new_certainty).count(1)

    if count == 1:
        return True
    return False


def node_certainty_check(certainty):
    if certainty <= 0:
        return 0
    if certainty > 1:
        return 1
    return certainty


def blue_AI(graph, game_over, energy, total_votes, is_grey, grey_chosen):

    if ((len(graph) + 1) * 10)/2 > energy and grey_chosen == False:

        return graph, energy, game_over, 1, grey_chosen

    if total_votes > 70:
        user_input = 5

    elif total_votes > 60:
        user_input = 4

    elif total_votes > 50:
        user_input = 3

    elif total_votes > 40:
        user_input = 2

    else:
        user_input = 1

    choice = user_input / 100
    for node in graph:
        if node['vote'] == 1:
            node['certainty'] += 0.05
            energy -= int(user_input / 2)
            continue
        if node['red followers'] == 0 and blue_vote_change(node['certainty'], user_input):
            node['vote'] = 1
            node['certainty'] += 0.05

        node['certainty'] += choice
        if node['red followers'] == 0:
            node['certainty'] += choice
        certainty = node['certainty']

        if blue_vote_change(certainty, user_input) and node['vote'] != 1:
            node['vote'] = 1

        node['certainty'] = node_certainty_check(node['certainty'])
        energy -= user_input

        if energy <= 0:
            game_over = True
            break

    return graph, energy, game_over, is_grey, grey_chosen
