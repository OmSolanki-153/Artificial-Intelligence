import random
import numpy as np

class TravelingSalesmanProblem:
    def __init__(self, num_cities, distances):
        self.num_cities = num_cities
        self.distances = distances

    def generate_individual(self):
        return random.sample(range(self.num_cities), self.num_cities)

    def calculate_fitness(self, individual):
        total_distance = 0
        for i in range(self.num_cities - 1):
            city1 = individual[i]
            city2 = individual[i + 1]
            total_distance += self.distances[city1][city2]
        total_distance += self.distances[individual[-1]][individual[0]]  # Return to the starting city
        return 1 / total_distance  # Fitness is inversely proportional to the total distance

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.num_cities - 1)
        child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
        return child1, child2

    def mutate(self, individual):
        index1, index2 = random.sample(range(self.num_cities), 2)
        individual[index1], individual[index2] = individual[index2], individual[index1]
        return individual

    def evolve_population(self, population, elite_size, mutation_rate):
        next_generation = []

        # Keep the elite individuals from the previous generation
        elite = sorted(population, key=lambda individual: self.calculate_fitness(individual), reverse=True)[:elite_size]
        next_generation.extend(elite)

        # Generate offspring using crossover and mutation
        while len(next_generation) < len(population):
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = self.crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child1 = self.mutate(child1)
            if random.random() < mutation_rate:
                child2 = self.mutate(child2)
            next_generation.extend([child1, child2])

        return next_generation

    def solve(self, population_size=100, elite_size=10, mutation_rate=0.01, generations=100):
        # Initialize population
        population = [self.generate_individual() for _ in range(population_size)]

        # Evolve the population
        for _ in range(generations):
            population = self.evolve_population(population, elite_size, mutation_rate)

        # Return the best individual (route) from the final population
        return max(population, key=lambda individual: self.calculate_fitness(individual))

# Example usage:
if __name__ == "__main__":
    # Example of distances between cities (replace with your own data)
    num_cities = 5
    distances = np.array([[0, 10, 15, 20, 25],
                          [10, 0, 35, 25, 30],
                          [15, 35, 0, 30, 10],
                          [20, 25, 30, 0, 40],
                          [25, 30, 10, 40, 0]])

    tsp = TravelingSalesmanProblem(num_cities, distances)
    best_route = tsp.solve()
    print("Best route:", best_route)
