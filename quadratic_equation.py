from math import sqrt


def get_negative_root(a, b, discriminant):
    root = (-b - sqrt(discriminant)) / (2 * a)
    return root


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a == 0 | discriminant < 0:
        return None, None

    if discriminant == 0:
        return get_negative_root(a, b, discriminant), None

    else:
        root1 = get_negative_root(a, b, discriminant)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
