import math

# Function to simulate Alice's operation
def alice(n, g, x):
    a = pow(g, x, n)  # Efficient modular exponentiation
    return a

# Function to simulate Bob's operation
def bob(n, g, y):
    b = pow(g, y, n)  # Efficient modular exponentiation
    return b

def main():
    # Input values for n, g, x, and y
    n = int(input("Enter value of n: "))
    g = int(input("Enter value of g: "))
    x = int(input("Enter value of x (Soham's private key): "))
    y = int(input("Enter value of y (Dev's private key): "))

    # Step 1: Alice computes her public value a
    a = alice(n, g, x)
    print("\Soham's end value:", a)

    # Step 2: Bob computes his public value b
    b = bob(n, g, y)
    print("Dev's end value:", b)

    # Step 3: Both compute the shared secret key
    k1 = alice(n, b, x)  # Alice computes k1 using Bob's public value
    print("Value of k1 (Shared secret key from Soham's perspective):", k1)

    k2 = alice(n, a, y)  # Bob computes k2 using Alice's public value
    print("Value of k2 (Shared secret key from Dev's perspective):", k2)

if __name__ == "__main__":
    main()
