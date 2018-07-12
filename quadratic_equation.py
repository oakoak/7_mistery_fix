from math import sqrt


def linear_equation(a, b):           # ax + b = 0
    if a == 0:
        return None
    return -b/a


def get_roots(a: float, b: float, c: float):
    try:
        discriminant = b ** 2 - 4 * a * c
    except TypeError:
        return None
    if a == 0:           #the solution of the degenerate equation
        return linear_equation(b, c), None
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2


if __name__ == "__main__":
    print("Enter the constants for a quadratic equation of the form:\n"
          "ax^2 + bx + c = 0")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        exit("Incorrect type data")

    print(get_roots(a, b, c))