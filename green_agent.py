def green(graph):
    for node in graph:
        # tmp = 0
        for neighbour in node['ajList']:
            if node['vote'] == graph[neighbour]['vote']:
                continue
            else:
                if node['certainty'] > graph[neighbour]['certainty']:
                    node['certainty'] -= 0.01
                    node['vote'] = graph[neighbour]['vote']
                    node['certainty'] = node_certainty_check(node['certainty'])

                else:
                    graph[neighbour]['certainty'] -= 0.01
                    graph[neighbour]['certainty'] = node_certainty_check(graph[neighbour]['certainty'])
        node['certainty'] = node_certainty_check(node['certainty'])

    return graph


def node_certainty_check(certainty):
    if certainty <= 0:
        return 0
    if certainty > 1:
        return 1
    return certainty
