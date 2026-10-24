
import random

Q = [[0.0] * 4 for _ in range(16)]
goal = 15
actions = [-4, 4, -1, 1]

def valid_actions(state):
    valid = []
    for a in actions:
        new = state + a
        if 0 <= new < 16:
            if a == -1 and state % 4 == 0:
                continue
            if a == 1 and state % 4 == 3:
                continue
            valid.append(a)
    return valid

for episode in range(1000):
    state = 0

    for step in range(100):
        if state == goal:
            break

        valid = valid_actions(state)

        if random.random() < 0.2:
            action = random.choice(valid)
        else:
            action = max(valid, key=lambda a: Q[state][actions.index(a)])

        next_state = state + action
        reward = 100 if next_state == goal else -1

        if next_state == goal:
            best_next = 0
        else:
            next_actions = valid_actions(next_state)
            best_next = max(Q[next_state][actions.index(a)]
                            for a in next_actions)

        i = actions.index(action)
        Q[state][i] += 0.1 * (
            reward + 0.9 * best_next - Q[state][i]
        )

        state = next_state

print("Training completed!")
print("Learned path:")

state = 0
while state != goal:
    print(state, end=" -> ")
    valid = valid_actions(state)
    action = max(valid, key=lambda a: Q[state][actions.index(a)])
    state += action

print(goal, "\nGoal reached!")
