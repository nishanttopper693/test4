import heapq

def heuristic(state):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    distance = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)

    return distance

def solve(start):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    queue = [(heuristic(start), 0, start, [])]
    visited = set()

    while queue:
        _, cost, state, path = heapq.heappop(queue)

        if state == goal:
            for board in path + [state]:
                print(board[:3])
                print(board[3:6])
                print(board[6:])
                print()
            print("Total moves:", cost)
            return

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if 0 <= new < 9 and not (
                move == -1 and zero % 3 == 0 or
                move == 1 and zero % 3 == 2
            ):
                next_state = state[:]
                next_state[zero], next_state[new] = next_state[new], next_state[zero]

                heapq.heappush(queue, (
                    cost + 1 + heuristic(next_state),
                    cost + 1,
                    next_state,
                    path + [state]
                ))

start = list(map(int, input("Enter initial state (0 for blank): ").split()))

if len(start) == 9 and sorted(start) == list(range(9)):
    solve(start)
else:
    print("Enter numbers 0 to 8 exactly once.")