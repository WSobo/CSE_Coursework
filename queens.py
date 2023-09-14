# assignment: n-Queens

# author: Will Sobolewski
# date: Aug 2nd, 2023
# file: queens.py is a program that solves the n-queens puzzle
# input: number of queens
# output: number of solutions and all solutions
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def is_solution(perm):
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if abs(i - j) == abs(perm[i] - perm[j]):
                return False
    return True


def solve_queens(n):
    solutions = []
    for perm in all_perms(list(range(1, n + 1))):
        if is_solution(perm):
            solutions.append(perm)
    return solutions


if __name__ == '__main__':
    n = int(input('Enter a number of queens: \n'))
    solutions = solve_queens(n)
    print(f'The {n}-queens puzzle has {len(solutions)} solutions:')
    for solution in solutions:
        print(solution)
