import math
import time
from multiprocessing import Pool, cpu_count

numbers = [5000, 6000, 5500, 4500, 7000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    # Sequential Execution
    starttime1 = time.time()
    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
    seqtime = time.time() - starttime1
    print(f"Sequential time: {seqtime}")

    # Parallel Execution
    starttime2 = time.time()
    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)
    paralleltime = time.time() - starttime2
    print(f"Parallel time: {paralleltime}")
