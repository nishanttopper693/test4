# pip install networkx matplotlib
import networkx as nx
import matplotlib.pyplot as plt

states = {
    'Maharashtra': ['Gujarat', 'Madhya Pradesh', 'Telangana', 'Karnataka', 'Goa'],
    'Gujarat': ['Rajasthan', 'Madhya Pradesh'],
    'Rajasthan': ['Madhya Pradesh'],
    'Madhya Pradesh': ['Telangana'],
    'Goa': ['Karnataka'],
    'Karnataka': ['Telangana'],
    'Telangana': []
}

colors = ['red', 'green', 'blue']
result = {}

def solve(index=0):
    names = list(states.keys())

    if index == len(names):
        return True

    state = names[index]

    for color in colors:
        safe = True

        for neighbour in states[state]:
            if result.get(neighbour) == color:
                safe = False
                break

        # Also check states that list this state as a neighbour
        for neighbour, adjacent in states.items():
            if state in adjacent and result.get(neighbour) == color:
                safe = False
                break

        if safe:
            result[state] = color

            if solve(index + 1):
                return True

            del result[state]

    return False

if solve():
    print("Map Coloring Solution:")
    for state, color in result.items():
        print(state, ":", color)

    graph = nx.Graph()

    for state, neighbours in states.items():
        for neighbour in neighbours:
            graph.add_edge(state, neighbour)

    pos = {
        'Rajasthan': (0, 2),
        'Gujarat': (0, 1),
        'Madhya Pradesh': (1.5, 1.7),
        'Maharashtra': (1.5, 0.6),
        'Goa': (1, -0.5),
        'Karnataka': (2.2, -0.5),
        'Telangana': (3, 0.7)
    }

    node_colors = [result[state] for state in graph.nodes()]

    nx.draw(
        graph, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=3000,
        font_size=8,
        edgecolors='black'
    )

    plt.title("Indian State Map Coloring using CSP")
    plt.axis('off')
    plt.show()

else:
    print("No solution found")
