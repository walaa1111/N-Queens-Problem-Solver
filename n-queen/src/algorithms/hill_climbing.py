import time

class HillClimbing:

    def __init__(self, problem):
        self.problem = problem

    def solve(self, start_state=None):
        start_time = time.time()
        current = start_state if start_state is not None else self.problem.random_state()
        current_h = self.problem.heuristic(current)

        while True:
            neighbors = self.problem.get_neighbors(current)

            best_neighbor = current
            best_h = current_h

            for neighbor in neighbors:
                h = self.problem.heuristic(neighbor)
                if h < best_h:
                    best_neighbor = neighbor
                    best_h = h

            if best_h >= current_h:
                break

            current = best_neighbor
            current_h = best_h

        end_time = time.time()
        
        return {
            "solution": current,
            "conflicts": current_h,
            "time": (end_time - start_time)
        }