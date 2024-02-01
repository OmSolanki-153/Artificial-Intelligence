import random

# Define the objective function to be optimized
def objective_function(x):
    return -x**2  # Example: maximizing the negative of a quadratic function

# Define the hill climbing algorithm
def hill_climbing(max_iter=1000, step_size=0.1):
    # Start with a random initial solution
    current_solution = random.uniform(-10, 10)  # Example: starting solution between -10 and 10
    current_value = objective_function(current_solution)
    
    # Iterate until reaching the maximum number of iterations
    for _ in range(max_iter):
        # Generate a new solution by adding a random value to the current solution
        new_solution = current_solution + random.uniform(-step_size, step_size)
        new_value = objective_function(new_solution)
        
        # If the new value is better, update the current solution
        if new_value > current_value:
            current_solution = new_solution
            current_value = new_value
    
    return current_solution, current_value

# Main function to run the hill climbing algorithm
def main():
    max_iter = 1000  # Maximum number of iterations
    step_size = 0.1  # Step size for generating neighboring solutions
    best_solution, best_value = hill_climbing(max_iter, step_size)
    print(f"Best Solution: {best_solution}, Best Value: {best_value}")

if __name__ == "__main__":
    main()
