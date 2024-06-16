def gcd(a, b):
    """Function to return the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    """Function to calculate Euler's Totient Function for an integer n."""
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    result = euler_totient(num)
    print(f"Euler's Totient Function φ({num}) = {result}")
