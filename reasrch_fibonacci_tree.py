import math

import numpy as np


def multiply_polynomials(p1, p2):
    """
    Multiply two polynomials represented as arrays of coefficients.
    """
    return np.polymul(p1, p2)


def add_polynomials(p1, p2):
    """
    Add two polynomials represented as arrays of coefficients.
    """
    return np.polyadd(p1, p2)


def independence_polynomial(p1, p2, p3, p4):
    """
    Calculate the independence polynomial I(r_n, z) using the recurrence relation.

    Parameters:
    p1, p2, p3, p4 (list): Coefficient arrays for polynomials I(r_n-1, z), I(r_n-2, z), I(r_n-3, z), and I(r_n-4, z).
    z (int or float): The scalar z used in the recurrence relation.

    Returns:
    list: The coefficient array of the resulting polynomial.
    """
    # First term: I(r_n-1, z) * I(r_n-2, z)
    term1 = multiply_polynomials(p1, p2)

    # Second term: z * I(r_n-2, z) * I(r_n-3, z)
    term2 = multiply_polynomials(p2, p3)
    term2 = multiply_polynomials(term2, p3)
    term2 = multiply_polynomials(term2, p4)
    term2 = [coef for coef in term2]  # Multiply the polynomial by z
    term2.insert(0, 0)
    term2 = np.array(term2)

    # term2 = [z * coef for coef in term2]  # Multiply the polynomial by z

    # Add all the terms together
    # print(term1)
    # print(term2)
    result = add_polynomials(term1, term2)
    # result = add_polynomials(result, term3)

    return result


def calculate_mode(polynomial_coefficients):
    """
    This function calculates the mode of the independence polynomial.

    Parameters:
    polynomial_coefficients (list): A list of coefficients of the independence polynomial,
                                    where the index corresponds to the degree of the term.

    Returns:
    int: The index of the mode (the index of the maximum coefficient).
    """
    # Find the maximum coefficient and its index
    polynomial_coefficients.reverse()
    mode_index = polynomial_coefficients.index(max(polynomial_coefficients))
    polynomial_coefficients.reverse()

    return mode_index


# Example usage:
p1 = [1, 2, 1]  # Example coefficient array for I(r_n-1, z)
p2 = [1, 1]  # Example coefficient array for I(r_n-2, z)
p3 = [1]  # Example coefficient array for I(r_n-3, z)
p4 = [1]  # Example coefficient array for I(r_n-4, z)
z = 1  # Example scalar value for z

result_polynomial = independence_polynomial(p1, p2, p3, p4)
# print("Resulting polynomial:", result_polynomial)
result_polynomial = [i for i in result_polynomial]
mode = calculate_mode(result_polynomial)
l = len(result_polynomial)


def generte_table():
    p4 = [1, 2]  # Example coefficient array for I(r_n-1, z)
    p3 = [1, 4, 3]  # Example coefficient array for I(r_n-2, z)
    p2 = [1, 7, 15, 11, 2]  # Example coefficient array for I(r_n-3, z)
    p1 = [1, 12, 55, 123, 142, 81, 18]  # Example coefficient array for I(r_n-4, z)
    for i in range(10):
        result_polynomial = independence_polynomial(p1, p2, p3, p4)
        # print("Resulting polynomial:", result_polynomial)
        # if i == 5:
            # print(result_polynomial)

        result_polynomial = [rr for rr in result_polynomial]

        l = len(result_polynomial) - 1
        mode = l - calculate_mode(result_polynomial)
        mt = math.floor(l / ((1 + math.sqrt(5)) / 2))

        print('deap', i + 5, 'alfa is:', l, 'mod:', mode, 'gusse mod:', mt)
        p4 = p3
        p3 = p2
        p2 = p1
        p1 = result_polynomial


generte_table()


# r=2, alpha=2 mode = 1
# r=3, alpha=4 mode = 2
# r=4, alpha=6 mode = 3
# r=5, alpha=10 mode = 6
# r=6, alpha=17 mode = 10
# r=7, alpha=27 mode = 16
# r=8, alpha=44 mode = 26
# r=9, alpha=72 mode = 42
# r=10, alpha=116 mode = 68
# r=11, alpha=188 mode = 111
# r=12, alpha=305 mode = 179
# r=13, alpha=493 mode = 290
# r=14, alpha=798 mode = 469
# r=15, alpha=1292 mode = 759
# r=16, alpha=2090 mode = 1229
# r=17, alpha=3382 mode = 1988
# r, alpha=2 mode = 1
# r=2, alpha=2 mode = 1