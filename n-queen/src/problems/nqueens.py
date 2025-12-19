import random

class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions_count = 0
    
    def reset(self):
        self.solutions_count = 0

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or abs(i - row) == abs(board[i] - col):
                return False
        return True

    def random_state(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def heuristic(self, state):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    conflicts += 1
        return conflicts

    def get_neighbors(self, state):
        neighbors = []
        for row in range(self.n):
            current_col = state[row]
            for col in range(self.n):
                if col != current_col:
                    new_state = state.copy()
                    new_state[row] = col
                    neighbors.append(new_state)
        return neighbors
