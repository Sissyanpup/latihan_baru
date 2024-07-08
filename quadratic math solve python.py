import math

# Input coefficients
a = float(input("masukkan nilai a1"))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant for the nature of roots
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Complex roots
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print(f"Root 1: {realPart} + {imaginaryPart}i")
    print(f"Root 2: {realPart} - {imaginaryPart}i")