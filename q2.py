import time

def state_to_tuple(state):
    return tuple(int(digit)for digit in state)
def tuple_to_state(matrix):
    return "".join(map(str,matrix))
def get_moves(matrix):
    moves = []
    zero_index=matrix.index(0)
    row,col =divmod(zero_index,3)
    if row>0:
        new_matrix=list(matrix)
        new_matrix[zero_index],new_matrix[zero_index-3] =new_matrix[zero_index-3],new_matrix[zero_index]
        moves.append(tuple(new_matrix))
    if row<2:
        new_matrix=list(matrix)
        new_matrix[zero_index],new_matrix[zero_index+3] =new_matrix[zero_index+3],new_matrix[zero_index]
        moves.append(tuple(new_matrix))
    if col>0:
        new_matrix=list(matrix)
        new_matrix[zero_index],new_matrix[zero_index-1] =new_matrix[zero_index-1],new_matrix[zero_index]
        moves.append(tuple(new_matrix))
    if col<2:
        new_matrix=list(matrix)
        new_matrix[zero_index],new_matrix[zero_index+1] =new_matrix[zero_index+1],new_matrix[zero_index]
        moves.append(tuple(new_matrix))
    return moves
def dfs(start_state,goal_state):
    stack = [(start_state,[start_state])]
    visited = set()
    while stack:
        current_state,path= stack.pop()
        if current_state == goal_state:
            return path
        visited.add(current_state)
        for next_state in get_moves(current_state):
            if next_state not in visited:
                stack.append((next_state,path+[next_state]))
    return None
def main():
    start_state="120345678"
    goal_state="123456780"
    start_tuple = state_to_tuple(start_state)
    goal_tuple= state_to_tuple(goal_state)
    print("----------------")
    print("DFS ALGORITHM")
    print("----------------")
    start_time=time.time()
    solution_path=dfs(start_tuple,goal_tuple)
    end_time=time.time()
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path) + 1)
        for state in solution_path:
            print(tuple_to_state(state))
            print("-----")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
