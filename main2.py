import time
def state_to_tuple(state):
    return tuple(state)
def tuple_to_state(matrix):
    return 
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
        if newRow >= 0 and newRow < 3 and newCol >= 0 and newCol < 3:
            newZeroIndex = newRow * 3 + newCol
            newMatrix = list(matrix)
            old = newMatrix[zeroIndex]
            newMatrix[zeroIndex] = newMatrix[newZeroIndex]
            newMatrix[newZeroIndex] = old
            moves.append(tuple(newMatrix))

    return moves

def dfs(start_state, goal_state):
    stack = []
    visited = set()
    stack.append((start_state, []))

    while stack:
        current, path = stack.pop()
        if current == goal_state:
            return path + []

        if current in visited:
            continue

        visited.add(current)
        for move in get_moves(current):
            stack.append((move, path + [move]))

    return None

def main():
    """Main function to take input and execute the DFS algorithm."""
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    # start_state = '120345678'
    # goal_state = '012345678'
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
            for row in state:
                print(' '.join(row))
                print("-----")
    else:
        print("No solution found.")
if __name__ == "__main__":
    main()