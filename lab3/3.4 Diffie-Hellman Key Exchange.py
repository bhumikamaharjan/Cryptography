def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p <= 1:
        return False
    if p == 2:
        return True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


def primitive_check(g, p):
    # Checks if the entered number is a primitive root or not
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set


while True:
    P = int(input("Enter a prime number: "))
    if not prime_checker(P):
        print("Number is not prime, please enter again!")
        continue
    break

while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if not primitive_check(G, P):
        print(f"Number is not a primitive root of {P}, please try again!")
        continue
    break

# Private Keys
while True:
    x1 = int(input("Enter the private key of Alice: "))
    x2 = int(input("Enter the private key of Bob: "))
    if x1 >= P or x2 >= P:
        print(f"Private key of both users should be less than {P}!")
        continue
    break

# Calculate Public Keys
y1 = pow(G, x1, P)
y2 = pow(G, x2, P)

# Generate Secret Keys
k1 = pow(y2, x1, P)
k2 = pow(y1, x2, P)

print(f"\nSecret key for Alice is {k1}\nSecret key for Bob is {k2}\n")

if k1 == k2:
    print("Keys have been exchanged successfully")
else:
    print("Keys have not been exchanged successfully")
