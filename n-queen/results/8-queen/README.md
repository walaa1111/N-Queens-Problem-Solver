## Results & Performance Analysis (N=8)

The $8$-Queens puzzle is the most classic version of this problem. With $64$ squares and $92$ possible total solutions, the performance of each algorithm starts to show clear distinctions.



* **Hill Climbing (`hill_climbing_n8.png`)**
    * **Status:** Stopped at a **Local Optimum**.
    * **Execution Time:** `0.0146s`
    * **Final Conflicts:** `2`
    * **Observation:** Started from `[5, 3, 3, 6, 7, 2, 0, 6]` and got stuck. In local search, $N=8$ often requires "random restarts" to avoid these local traps.

* **Genetic Algorithm (`genetic_algorithm_n8.png`)**
    * **Status:** **Evolving** (Close to Solution).
    * **Execution Time:** `0.0405s`
    * **Final Conflicts:** `1` (Fitness: 1)
    * **Generations:** `50`
    * **Observation:** With a population of 20 and 50 generations, the algorithm reached a nearly perfect state (only 1 conflict).


* **DFS Backtracking (`dfs_backtracking_n8.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0015s`
    * **Solutions Found:** `92`
    * **Observation:** Extremely efficient for this size. It explored the tree and found all 92 valid configurations in less than 2 milliseconds.

* **BFS (`bfs_n8.png`)**
    * **Status:** **Success** (Global Optimum Found).
    * **Execution Time:** `0.0235s`
    * **Solutions Found:** `92`
    * **Observation:** Found all solutions, but was slower than DFS due to the overhead of managing the frontier queue in a breadth-first manner.

---
## Genetic Algorithm Configuration

* **Population Size:** `20`
* **Generations:** `50`
* **Crossover Rate ($P_c$):** `0.8`
* **Mutation Rate ($P_m$):** `0.05`