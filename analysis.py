from timeit import Timer, timeit, repeat
import random
from matplotlib import pyplot as plt


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def analyze(fxn, data):
    if fxn == 'bubbleSort':
        func = bubbleSort
    elif fxn == 'mergeSort':
        func = mergeSort
    else:
        raise ValueError(
            "Invalid function name. Supported functions are 'bubbleSort' and 'mergeSort'.")

    times = []
    for d in data:
        # Measure the execution time 5 times and take the minimum
        time_taken = min(repeat(lambda: func(d), number=1, repeat=5))
        times.append(time_taken)
    return times


if __name__ == '__main__':

    # generate lists of random numbers from 0 to 500
    d1 = random.sample(range(0, 500), 10)
    d2 = random.sample(range(0, 500), 20)
    d3 = random.sample(range(0, 500), 50)
    d4 = random.sample(range(0, 500), 100)
    d5 = random.sample(range(0, 500), 200)

    # use random lists as input
    data = [d1, d2, d3, d4, d5]
    time = analyze('bubbleSort', data)
    plt.plot([len(i) for i in data], time, 'r', label='bubbleSort')

    time = analyze('mergeSort', data)
    plt.plot([len(i) for i in data], time, 'b', label='mergeSort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()
