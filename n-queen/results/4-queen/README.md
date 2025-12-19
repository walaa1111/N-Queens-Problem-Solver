##  Results & Performance Analysis (N=4)

In this run with a $4 \times 4$ board, all algorithms successfully converged to a valid solution. Unlike larger boards, the state space for $N=4$ is small enough for even local search and genetic algorithms to find the global optimum almost instantly.


* **Hill Climbing (`hill_climbing_n4.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0s`
    * **Final Conflicts:** `0`
    * **Observation:** Started from a random state `[0, 2, 3, 3]` and quickly moved to a perfect solution `[2, 0, 3, 1]`.

* **Genetic Algorithm (`genetic_algorithm_n4.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0016s`
    * **Generations:** `1`
    * **Observation:** The solution was found in the very first generation, demonstrating high efficiency for small $N$.


* **DFS Backtracking (`dfs_backtracking_n4.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0s`
    * **Solutions Found:** `2`
    * **Observation:** Systematically found both possible solutions for the 4-Queens problem.

* **BFS (`bfs_n4.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0s`
    * **Solutions Found:** `2`
    * **Observation:** Identical to DFS in terms of solution count, exploring all levels of the search tree instantly.

---

##  Genetic Algorithm Configuration

* **Population Size:** `20`
* **Crossover Rate ($P_c$):** `0.8`
* **Mutation Rate ($P_m$):** `0.05`