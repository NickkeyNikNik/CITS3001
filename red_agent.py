import random


def red(graph):
    while True:
        user_input = str(input("Select level of potency message for red [1,2,3,4,5]: "))
        if user_input.isnumeric():
            user_input = int(user_input)
            if 0 < user_input < 6:
                break
        print("Enter valid input!")
        print("===============================================================================")
        continue

    choice = user_input / 100

    for node in graph:
        if node['red followers'] == 0:
            if red_vote_change(node['certainty'], user_input):
                node['vote'] = 1
            continue
        if node['vote'] == 0:
            node['certainty'] += 0.05
            if remove_red_follower(choice * 10):
                node['red followers'] = 0
            continue

        node['certainty'] += choice
        certainty = node['certainty']

        if red_vote_change(certainty, user_input) and node['vote'] != 0:
            node['vote'] = 0

        node['certainty'] = node_certainty_check(node['certainty'])

        if remove_red_follower(choice * 10):
            node['red followers'] = 0
            node['certainty'] = 0.5
            if red_vote_change(node['certainty'], user_input):
                node['vote'] = 1
    return graph


def red_grey(graph):
    choice = 0.05

    for node in graph:
        if node['red followers'] == 0:
            if red_vote_change(node['certainty'], 5):
                node['vote'] = 1
            continue
        if node['vote'] == 0:
            node['certainty'] += 0.01
            continue

        node['certainty'] += choice
        certainty = node['certainty']

        if red_vote_change(0.5, 5) and node['vote'] != 0:
            node['vote'] = 0

        node['certainty'] = node_certainty_check(node['certainty'])

    return graph


def random_uncertainty(choice):
    return random.random()


def remove_red_follower(chance):
    if chance * 10 < 3:
        return False
    if random.uniform(chance, 1) > 0.85:
        return True
    return False


def red_vote_change(certainty, red_message):
    vote_chance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    count = 0
    new_certainty = int(certainty * 10)
    if certainty < 0.5:
        count = random.sample(vote_chance, red_message).count(1)
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

def red_AI(graph, total_votes):

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
        if node['red followers'] == 0:
            if red_vote_change(node['certainty'], user_input):
                node['vote'] = 1
            continue
        if node['vote'] == 0:
            node['certainty'] += 0.05
            if remove_red_follower(choice * 10):
                node['red followers'] = 0
            continue

        node['certainty'] += choice
        certainty = node['certainty']

        if red_vote_change(certainty, user_input) and node['vote'] != 0:
            node['vote'] = 0

        node['certainty'] = node_certainty_check(node['certainty'])

        if remove_red_follower(choice * 10):
            node['red followers'] = 0
            node['certainty'] = 0.5
            if red_vote_change(node['certainty'], user_input):
                node['vote'] = 1
    return graph
