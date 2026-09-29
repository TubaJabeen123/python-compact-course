# Task 1: sort a list of tuples by the last element of each tuple

def sort_by_last(tuples_list):
    return sorted(tuples_list, key=lambda t: t[-1])


if __name__ == "__main__":
    sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_by_last(sample))