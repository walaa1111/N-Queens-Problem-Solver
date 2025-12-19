import time

class DFSBacktracking:
    def __init__(self, problem):
        self.problem = problem
    
    def solve(self):
        start_time = time.time()
        self.problem.reset()
        n = self.problem.n
        board = [-1] * n  
        first_solution = []
        self._backtrack(board, 0, n, first_solution)
        end_time = time.time()
        return {
            "solution": first_solution,
            "solutions_count": self.problem.solutions_count,
            "time": end_time - start_time
        }
    
    def _backtrack(self, board, row, n, first_solution):
        if row == n:
            self.problem.solutions_count += 1
            if not first_solution:
                first_solution.extend(board)
            return
        for col in range(n):
            if self.problem.is_safe(board, row, col):
                board[row] = col
                self._backtrack(board, row + 1, n, first_solution)
                board[row] = -1
