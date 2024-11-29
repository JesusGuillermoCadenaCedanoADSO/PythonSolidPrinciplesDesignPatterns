import threading
import time
import random

class NumberGenerator:

    _instance = None
    # uso de bloque para proteger la variable sequence y hacer que sea segura
    # en entornos multihilo
    _lock = threading.Lock()

    def __new__(cls):
        # Implement the singleton pattern
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize an empty list
        if not hasattr(self, "sequence"):  # solo inicializa la lista si no existe
            self.sequence = 0

    def getnextnumber(self):
        with self._lock:
            last_number = self.sequence
            time.sleep(random.uniform(0.00001, 0.0001))
            self.sequence +=1
        return last_number


# sequence_1 = SingletonGenerator()
# n_1 = sequence_1.getnextnumber()
# print(n_1)
# n_2 = sequence_1.getnextnumber()
# print(n_2)

# Shared list to store the numbers generated by each thread
results = []

# Lock for thread-safe writing to the results list
results_lock = threading.Lock()

def generate_numbers():
    generator = NumberGenerator()
    for _ in range(1000):
        number = generator.getnextnumber()
        print(number)
        with results_lock:
            results.append(number)


if __name__ == "__main__":
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=generate_numbers)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

        # Check for duplicates and gaps in the sequence
    duplicates = set()
    gaps = []

    # Sort the results to easily check for gaps
    sorted_results = sorted(results)

    # Check for duplicates
    for i in range(1, len(sorted_results)):
        if sorted_results[i] == sorted_results[i - 1]:
            duplicates.add(sorted_results[i])

    # Check for gaps
    for i in range(1, len(sorted_results)):
        if sorted_results[i] != sorted_results[i - 1] + 1:
            gaps.append((sorted_results[i - 1], sorted_results[i]))

    # Output the results
    print(
        f"Generated numbers: {sorted_results[:50]} ... {sorted_results[-50:]}")  # Show first and last 50 numbers for brevity
    print(f"Duplicates: {duplicates}")
    print(f"Gaps: {gaps}")