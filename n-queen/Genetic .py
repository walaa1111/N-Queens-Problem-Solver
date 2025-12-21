import numpy as np
import random

def generate_population(population_size, N):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, N - 1) for _ in range(N)]
        population.append(chromosome)
    return np.array(population)

def calc_fitness(population, N):
    fitness_values = []

    for chromosome in population:
        conflicts = 0
        for i in range(N):
            for j in range(i + 1, N):
                if chromosome[i] == chromosome[j]:
                    conflicts += 1
                if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                    conflicts += 1

        fitness_values.append(-conflicts)

    return np.array(fitness_values)

def selection(population, fitness_values):
    probs = fitness_values.copy()
    probs += abs(probs.min()) + 1
    probs = probs / probs.sum()

    indices = np.arange(len(population))
    selected_indices = np.random.choice(indices, size=len(population), p=probs)
    return population[selected_indices]

def crossover(parent1, parent2, pc, N):
    if np.random.random() < pc:
        point = np.random.randint(1, N)
        child1 = np.concatenate([parent1[:point], parent2[point:]])
        child2 = np.concatenate([parent2[:point], parent1[point:]])
    else:
        child1 = parent1.copy()
        child2 = parent2.copy()

    return child1, child2

def mutation(individual, pm, N):
    if np.random.random() < pm:
        gene = np.random.randint(N)
        individual[gene] = np.random.randint(N)
    return individual

def crossover_mutation(selected_population, pc, pm, N):
    n = len(selected_population)
    new_population = np.empty((n, N), dtype=int)

    for i in range(0, n, 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]

        child1, child2 = crossover(parent1, parent2, pc, N)
        new_population[i] = child1
        new_population[i + 1] = child2

    for i in range(n):
        mutation(new_population[i], pm, N)

    return new_population

def n_queens_GA(pop_size, max_generations, N, pc=0.7, pm=0.03):
    population = generate_population(pop_size, N)
    best_fitness_overall = None

    for generation in range(max_generations):
        fitness_values = calc_fitness(population, N)
        best_index = fitness_values.argmax()
        best_fitness = fitness_values[best_index]

        if best_fitness_overall is None or best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            best_solution = population[best_index]

        print(
            f"\rGeneration {generation:04} | Conflicts = {-best_fitness_overall}",
            end=""
        )

        if best_fitness == 0:
            print("\n Optimal Solution Found!")
            break

        selected_population = selection(population, fitness_values)
        population = crossover_mutation(selected_population, pc, pm, N)

    print("\nBest Solution:")
    print(best_solution)
    return best_solution

if __name__ == "__main__":
    random.seed(1)
    np.random.seed(1)

    N = int(input("Enter N for N-Queens: "))
    pop_size = 20
    max_generations = 50

    n_queens_GA(
        pop_size=pop_size,
        max_generations=max_generations,
        N=N,
        pc=0.8,
        pm=0.05
    )
