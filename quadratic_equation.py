from math import sqrt


def get_roots(a, b, c):

    if a == 0:
        print("Not a quadratic equation")
        return None, None

    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        root = -b / (2 * a)
        return root, None

    elif discriminant < 0:
        return None, None

    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
