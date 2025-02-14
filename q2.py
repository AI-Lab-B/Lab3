import time
import copy

def state_to_tuple(state):
    outerList = []
    for i in range(3):
        innerList = []
        for j in range(3):
            innerList.append(state[i * 3 + j])
        outerList.append(innerList)
    return outerList

def tuple_to_state(matrix):
    stringState = ""
    for i in range(3):
        for j in range(3):
            stringState += matrix[i][j]
    return stringState

def get_moves(matrix):
    # Find index of empty position
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "0":
                emptyPositionI = i
                emptyPositionJ = j
    states = []
    # Up
    if emptyPositionI - 1 >= 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[emptyPositionI][emptyPositionJ], new_matrix[emptyPositionI - 1][emptyPositionJ] = new_matrix[emptyPositionI - 1][emptyPositionJ], new_matrix[emptyPositionI][emptyPositionJ]
        states.append(new_matrix)
    # Down
    if emptyPositionI + 1 < 3:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[emptyPositionI][emptyPositionJ], new_matrix[emptyPositionI + 1][emptyPositionJ] = new_matrix[emptyPositionI + 1][emptyPositionJ], new_matrix[emptyPositionI][emptyPositionJ]
        states.append(new_matrix)
    # Left
    if emptyPositionJ - 1 >= 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[emptyPositionI][emptyPositionJ], new_matrix[emptyPositionI][emptyPositionJ - 1] = new_matrix[emptyPositionI][emptyPositionJ - 1], new_matrix[emptyPositionI][emptyPositionJ]
        states.append(new_matrix)
    # Right
    if emptyPositionJ + 1 < 3:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[emptyPositionI][emptyPositionJ], new_matrix[emptyPositionI][emptyPositionJ + 1] = new_matrix[emptyPositionI][emptyPositionJ + 1], new_matrix[emptyPositionI][emptyPositionJ]
        states.append(new_matrix)
    
    return states

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path + [current_state]
        if current_state in visited:
            continue
        visited.add(current_state)
        print(visited)
        possibleStates = get_moves(state_to_tuple(current_state))
        for state in possibleStates:
            new_state = tuple_to_state(state)
            if new_state not in visited:
                stack.append((new_state, path + [current_state]))
    return []

def main():
    start_state = "321654087"
    goal_state = "123456780"
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")
    start_time = time.time()
    solution_path = dfs(tuple_to_state(start_tuple), tuple_to_state(goal_tuple))
    end_time = time.time()
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path))
        for state in solution_path:
            for row in state_to_tuple(state):
                print(' '.join(row))
            print("-----")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
