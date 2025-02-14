import time
from collections import deque

def state_to_tuple(state):
    return tuple(state)

def tuple_to_state(matrix):
    return ''.join(matrix)

def get_moves(matrix):
    moves = []

    zeroIndex = matrix.index('0')
    row = zeroIndex // 3
    col = zeroIndex % 3
    # down, right, up, left
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        newRow = row + direction[0]
        newCol = col + direction[1]
        if 0 <= newRow < 3 and 0 <= newCol < 3:
            newZeroIndex = newRow * 3 + newCol
            newMatrix = list(matrix)
            newMatrix[zeroIndex], newMatrix[newZeroIndex] = newMatrix[newZeroIndex], newMatrix[zeroIndex]
            moves.append(tuple(newMatrix))

    return moves

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path
        if current_state not in visited:
            visited.add(current_state)
            for move in get_moves(current_state):
                stack.append((move, path + [move]))
    return None

def main():
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")
    start_time = time.time()       
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path) + 1)
        for state in solution_path:
            for i in range(0, 9, 3):
                print(' '.join(state[i:i+3]))
            print("------")
    else:
        print("No solution found.")