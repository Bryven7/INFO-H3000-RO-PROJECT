import csv
import random

# Load data from CSV file
data = []
with open('instance.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    data = [[int(cell) for cell in row] for row in reader]

# Define the weights w1, w2, w3 (random values in the range [0, 1])
w1, w2, w3 = random.random(), random.random(), random.random()

# Calculate the processing times for each machine
processing_times = [[sum(row[2:i+3]) for i in range(len(row)-2)] for row in data]

# Function to calculate the makespan of a solution
def calculate_makespan(solution):
    return max(sum(processing_times[piece-1][i] for i, piece in enumerate(machine_order)) for machine_order in solution)

# Function to calculate the total weighted tardiness of a solution
def calculate_total_tardiness(solution):
    total_tardiness = 0
    for piece_order in solution:
        time_so_far = 0
        for i, piece in enumerate(piece_order):
            time_so_far += processing_times[piece-1][i]
            tardiness = max(0, time_so_far - data[piece][1])
            total_tardiness += data[piece][0] * tardiness
    return total_tardiness

# Generate random solutions for demonstration
num_solutions = 10
random_solutions = [random.sample(range(1, len(data)), len(data) - 1) for _ in range(num_solutions)]

# Calculate maximum values for normalization
max_makespan = max(calculate_makespan(sol) for sol in random_solutions)
max_tardiness = max(calculate_total_tardiness(sol) for sol in random_solutions)

# Check if max_makespan or max_tardiness is zero
if max_makespan == 0:
    max_makespan = 1  # Set a default value of 1 if max_makespan is zero
if max_tardiness == 0:
    max_tardiness = 1  # Set a default value of 1 if max_tardiness is zero

# Evaluate each solution and calculate the score
scores = []
for solution in random_solutions:
    makespan = calculate_makespan([solution])
    total_tardiness = calculate_total_tardiness([solution])
    score = w1 * (makespan / max_makespan) + w2 * (total_tardiness / max_tardiness) + w3 * 0  # Placeholder for another objective if n
