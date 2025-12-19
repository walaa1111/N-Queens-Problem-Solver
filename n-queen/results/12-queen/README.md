##  Results & Performance Analysis (N=12)

The project compares four AI algorithms based on their ability to solve the $12$-Queens problem. Below is the visualization status and performance data for each:

* **Hill Climbing (`hill_climbing_n12.png`)**
    * **Status:** Stopped at a **Local Optimum**.
    * **Execution Time:** `0.0162s`
    * **Final Conflicts:** `2`
    * **Observation:** Extremely fast but got stuck in a local peak where no single move could further reduce the conflicts from the initial random state.

* **Genetic Algorithm (`genetic_algorithm_n12.png`)**
    * **Status:** **Evolving** (Close to Solution).
    * **Execution Time:** `0.0468s`
    * **Final Conflicts:** `2`
    * **Observation:** Improved the population over 50 generations but requires a higher generation limit or larger population to reach 0 conflicts for $N=12$.

* **DFS Backtracking (`dfs_backtracking_n12.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `8.6000s`
    * **Final Conflicts:** `0`
    * **Observation:** Found the first complete solution and identified all **14,200** possible solutions.

* **BFS (`bfs_n12.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `10.3309s`
    * **Final Conflicts:** `0`
    * **Observation:** Like DFS, it is exhaustive and guaranteed to find a solution, though it took slightly longer due to the nature of level-by-level exploration.

---

## Genetic Algorithm Configuration

The following parameters were used to control the evolutionary process in the Genetic Algorithm:

* **Population Size:** `20` 
* **Generations:** `50`
* **Crossover Rate (Pc):** `0.8` i
* **Mutation Rate (Pm):** `0.05`
