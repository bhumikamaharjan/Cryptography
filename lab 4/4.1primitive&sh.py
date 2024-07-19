import os
import math


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primitive_roots(n):
    """Find all primitive roots of a given number n."""
    if not is_prime(n):
        return []

    required_set = set(num for num in range(1, n) if math.gcd(num, n) == 1)
    primitive_roots = []

    for g in range(1, n):
        actual_set = set(pow(g, powers, n) for powers in range(1, n))
        if required_set == actual_set:
            primitive_roots.append(g)

    return primitive_roots


def shutdown_system():
    """Shutdown the system."""
    os.system('shutdown /s /t 1')  # For Windows
    # os.system('shutdown now')  # For Linux/Unix


def main():
    try:
        number = int(input("Enter a number: "))

        if 1000 <= number <= 2000:
            print("The number is between 1000 and 2000. Shutting down the system...")
            shutdown_system()
        else:
            primitive_roots = find_primitive_roots(number)
            if primitive_roots:
                print(f"Primitive roots of {number} are: {primitive_roots}")
            else:
                print(f"{number} has no primitive roots or is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
