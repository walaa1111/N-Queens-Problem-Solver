from src.problems.nqueens import NQueens
from src.algorithms.hill_climbing import HillClimbing
from src.algorithms.dfs_backstracking import DFSBacktracking
from src.algorithms.bfs import BFS
from src.algorithms.genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle

def save_board(state, filename, title="N-Queens Board"):
    if state is None:
        return

    n = len(state)

    board = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            board[i][j] = (i + j) % 2

    fig, ax = plt.subplots(figsize=(n, n))
    ax.imshow(board, cmap="gray")

    # Draw queens
    for row, col in enumerate(state):
        ax.text(
            col, row, "♛",
            ha="center",
            va="center",
            fontsize=30 if n <= 8 else 18,
            color="red"
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.axis("off")

    rect = Rectangle(
        (-0.5, -0.5), n, n, 
        linewidth=3, edgecolor="black", facecolor="none"
    )
    ax.add_patch(rect)

    os.makedirs("results", exist_ok=True)

    plt.savefig(f"results/{filename}", dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    n = int(input("Enter N for N-Queens (e.g., 4, 8, 12): "))
    problem = NQueens(n)

    initial_state = problem.random_state()
    print("Initial Random State (from NQueens):", initial_state)

    hc = HillClimbing(problem)
    result = hc.solve()

    dfs= DFSBacktracking(problem)
    res = dfs.solve()

    bfs = BFS(problem)
    result_bfs = bfs.solve()

    ga = GeneticAlgorithm(n, N=20,G=50, Pc=0.8, Pm=0.05)
    result_ga = ga.solve()
    

    print("Hill Climbing Result:")
    print("Solution:", result["solution"])
    print("Conflicts:", result["conflicts"])
    print("Execution Time:", result["time"])
    save_board(
    result["solution"],
    f"hill_climbing_n{n}.png",
    "Hill Climbing Solution"
    )


    print("\ndfs backstraking Result:")
    print("Solutions count:", res["solutions_count"])
    print("First Solution:", res["solution"])
    print("Execution Time:", res["time"])
    save_board(
    res["solution"],
    f"dfs_backtracking_n{n}.png",
    "DFS Backtracking – First Solution"
    )

    print("\nBFS Result:")
    print("First Solution:", result_bfs["solution"])
    print("Total Solutions:", result_bfs["solutions_count"])
    print("Execution Time:", result_bfs["time"])
    save_board(
    result_bfs["solution"],
    f"bfs_n{n}.png",
    "BFS – First Solution"
    )

    print("\nGenetic Result:")
    print("Best Solution:", result_ga["solution"])
    print("Fitness:", result_ga["fitness"])
    print("Generations:", result_ga["generations"])
    print("Execution Time:", result_ga["execution_time"])
    
    save_board(
    result_ga["solution"],
    f"genetic_algorithm_n{n}.png",
    "Genetic Algorithm Solution"
    )
  