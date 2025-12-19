import random
import time

class GeneticAlgorithm:
    def __init__(self, n, N=100, G=500, Pc=0.8, Pm=0.05):
        self.n = n         
        self.N = N           
        self.G = G            
        self.Pc = Pc        
        self.Pm = Pm         

    def fitness(self, state):
        conflicts = 0
        diag1 = {}
        diag2 = {}

        for r in range(self.n):
            d1 = r - state[r]
            d2 = r + state[r]
            diag1[d1] = diag1.get(d1, 0) + 1
            diag2[d2] = diag2.get(d2, 0) + 1

        for v in diag1.values():
            if v > 1:
                conflicts += v * (v - 1) // 2
        for v in diag2.values():
            if v > 1:
                conflicts += v * (v - 1) // 2

        return conflicts

    def make_random(self):
        state = list(range(self.n))
        random.shuffle(state)
        return state

  
    def crossover(self, parent1, parent2):
        cut = random.randint(1, self.n - 2)
        child = parent1[:cut]
        for gene in parent2:
            if gene not in child:
                child.append(gene)
        return child

    
    def mutation(self, chromosome):
        r = random.random()
        if r < self.Pm:
            i, j = random.sample(range(len(chromosome)), 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]


    def solve(self):
        start_time = time.time()

        population = [self.make_random() for _ in range(self.N)]
        best = min(population, key=self.fitness)
        best_fit = self.fitness(best)
        fitness_history = [best_fit]
        for generation in range(self.G):
            new_population = []
          
            new_population.append(best.copy())

            while len(new_population) < self.N:
                parent1 = min(random.sample(population, 5), key=self.fitness)
                parent2 = min(random.sample(population, 5), key=self.fitness)

                r = random.random()
                if r < self.Pc:
                    child = self.crossover(parent1, parent2)
                else:
                    child = parent1.copy()

           
                self.mutation(child)

                new_population.append(child)

            population = new_population
            fitness_history.append(best_fit)
            current_best = min(population, key=self.fitness)
            current_fit = self.fitness(current_best)

            if current_fit < best_fit:
                best = current_best
                best_fit = current_fit

            if best_fit == 0:
                break

        end_time = time.time()

        return {
            "solution": best,
            "fitness": best_fit,
            "generations": generation + 1,
            "execution_time": end_time - start_time,
        }
