input_graph = {
    0: [1, 3, 5],
    1: [0, 7],
    2: [3, 4, 7],
    3: [0, 2],
    4: [2],
    5: [0, 7],
    6: [7],
    7: [1, 2, 5, 6]
}


def depth_first_search(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


if __name__ == "__main__":
    print(f'The visited order is {depth_first_search(input_graph, 0)}')
