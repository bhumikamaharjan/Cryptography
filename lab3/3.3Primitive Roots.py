def power(a, b, m):
    """
    Function to calculate (a^b) % m using modular exponentiation.
    """
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result

def gcd(a, b):
    """
    Function to find the greatest common divisor (GCD) of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def find_primitive_roots(n):
    """
    Function to find primitive roots of a given number n.
    """
    primitive_roots = []
    for r in range(2, n):
        if gcd(r, n) == 1:
            is_primitive_root = True
            for i in range(1, n - 1):
                if power(r, i, n) == 1:
                    is_primitive_root = False
                    break
            if is_primitive_root:
                primitive_roots.append(r)
    return primitive_roots

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    primitive_roots = find_primitive_roots(n)

    if not primitive_roots:
        print(f"No primitive roots found for {n}")
    else:
        print(f"Primitive roots of {n} are: {' '.join(map(str, primitive_roots))}")
