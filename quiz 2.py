def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


# Calculate the 10th term
tenth_term = factorial(10)

print("The 10th term is:", tenth_term)
