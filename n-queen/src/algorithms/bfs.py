import time
from collections import deque

class BFS:
    def __init__(self, problem):
        self.problem = problem
        self.n = problem.n

    def solve(self):
        start_time = time.time()
        queue = deque()
        queue.append([])
        solutions = []
        first_solution = []

        while queue:
            state = queue.popleft()
            row = len(state)
            if row == self.n:
                solutions.append(state)
                if not first_solution:
                    first_solution = state
                continue
            for col in range(self.n):
                if self.problem.is_safe(state + [-1]*(self.n - row), row, col):
                    queue.append(state + [col])

        end_time = time.time()
        return {
            "solution": first_solution,
            "solutions_count": len(solutions),
            "time": end_time - start_time
        }
