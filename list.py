def list_comprehension(A: list) -> list:
    return [A[i] + A[i+1] for i in range(len(A)-1)]


# if __name__ == '__main__':
#    print(list_comprehension([1, 3, 2, 4]))
