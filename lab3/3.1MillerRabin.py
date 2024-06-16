import random

def mulmod(a, b, mod):
    x = 0
    y = a % mod
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % mod
        y = (y * 2) % mod
        b //= 2
    return x % mod

def modulo(base, exp, mod):
    x = 1
    y = base
    while exp > 0:
        if exp % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        exp //= 2
    return x % mod

def miller_rabin(p, iteration):
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    s = p - 1
    while s % 2 == 0:
        s //= 2
    for _ in range(iteration):
        a = random.randint(1, p - 1)
        temp = s
        mod = modulo(a, temp, p)
        while temp != p - 1 and mod != 1 and mod != p - 1:
            mod = mulmod(mod, mod, p)
            temp *= 2
        if mod != p - 1 and temp % 2 == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter integer to test primality: "))
    iteration = 10
    if miller_rabin(num, iteration):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
