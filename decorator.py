import time

#############################################


def calculate_time(func):
    def wrap(n):
        start = time.time()
        result = func(n)
        stop = time.time()
        elapsed = stop - start
        print(f"It took {elapsed} sec.")
        return result
    return wrap
#############################################


@calculate_time
def sum1(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


if __name__ == '__main__':
    n = 1000000
    s = sum1(n)
    print(f'The sum of numbers from 1 to {n} is {s}.')
