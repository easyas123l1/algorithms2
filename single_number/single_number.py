'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import defaultdict


def single_number(arr):
    count = defaultdict(int)

    for i in arr:
        if count[i] == 1:
            count[i] -= 1
        else:
            count[i] += 1

    for key in count:
        if count[key] == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
