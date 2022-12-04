#!/usr/bin/env python3

# Needed to pipe file in command line.
def split_and_int(task):
    return [int(subtask) for subtask in task.split('-')]

def check_subset(first, second):
    return set(range(first[0], first[1] + 1)).issubset(range(second[0], second[1] + 1))

def load_tasks():
    is_subset = []
    while True:
        try:
            task = input()
        except EOFError:
            break
        first, second = task.strip().split(',')
        first, second = split_and_int(first), split_and_int(second)
        is_subset.append(check_subset(first, second) or check_subset(second, first))
    return is_subset

# Task 1
# print(sum(load_tasks())) >> 453

def has_intersection(first, second):
    return len(set(range(first[0], first[1] + 1)).intersection(range(second[0], second[1] + 1))) > 0

def load_tasks2():
    intersections = []
    while True:
        try:
            task = input()
        except EOFError:
            break
        first, second = task.strip().split(',')
        first, second = split_and_int(first), split_and_int(second)
        intersections.append(has_intersection(first, second))
    return intersections

print(sum(load_tasks2()))
