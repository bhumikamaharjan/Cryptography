import random

def exhaust_memory():
    try:
        large_list = []
        while True:
            # Append a large number of random floats to the list
            large_list.extend([random.random() for _ in range(10**6)])
    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    exhaust_memory()
