# 2. Multiprocessing (CPU-bound tasks)

# Question:
# You need to calculate the factorial of a large list of numbers, which is CPU-intensive.

# numbers = [50000, 60000, 55000, 45000, 70000]

# Write Python code to:
# 1. Use multiprocessing to calculate the factorial of each number in parallel.
# 2. Print the factorial of each number.
# 3. Measure and compare the total time taken using multiprocessing versus sequential computation.
# Hint: Use multiprocessing.Pool or Process and the math.factorial function.






import math
import time
import multiprocessing


# Function to calculate factorial
def calculate_factorial(number):
    return math.factorial(number)


# Function to calculate number of digits in factorial
def factorial_digit_count(n):
    if n == 0 or n == 1:
        return 1
    return int(sum(math.log10(i) for i in range(1, n + 1))) + 1


if __name__ == "__main__":

    numbers = [50000, 60000, 55000, 45000, 70000]

    # 1. Sequential Computation
    start_time_seq = time.time()

    sequential_results = []
    for num in numbers:
        result = calculate_factorial(num)
        sequential_results.append(result)

        print(f"Sequential: Factorial of {num} calculated")
        print(f"Number of digits: {factorial_digit_count(num)}\n")

    sequential_time = time.time() - start_time_seq
    print(f"Time taken (Sequential): {sequential_time:.4f} seconds\n")

    # 2. Multiprocessing Computation
    start_time_mp = time.time()

    with multiprocessing.Pool() as pool:
        multiprocessing_results = pool.map(calculate_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial of {num} calculated")
        print(f"Number of digits: {factorial_digit_count(num)}\n")

    multiprocessing_time = time.time() - start_time_mp

    # 3. Performance Comparison
    print("Performance Comparison:")
    print(f"Sequential Time      : {sequential_time:.4f} seconds")
    print(f"Multiprocessing Time : {multiprocessing_time:.4f} seconds")

