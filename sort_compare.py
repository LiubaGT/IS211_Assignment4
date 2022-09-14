import time
import random

LIST_NUM = 1
ITEMS_IN_LIST = [500, 1000, 10000]


def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end_time = time.time()
    exec_time = end_time - start_time
    insertion_execution_time = '{:f}'.format(exec_time)
    return insertion_execution_time


def shell_sort(alist):
    start_time = time.time()
    sublist_count = len(alist)//2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = time.time()
    exec_time = end_time - start_time
    shel_sort_execution_time = '{:f}'.format(exec_time)
    return shel_sort_execution_time


def gap_insertion_sort(nlist, start, gap):
    for i in range(start+gap, len(nlist), gap):

        current_value = nlist[i]
        position = i

        while position >= gap and nlist[position-gap] > current_value:
            nlist[position] = nlist[position-gap]
            position = position-gap

        nlist[position] = current_value


nlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(nlist)


def python_sort():
    random_num_of_list_length = random.choice(ITEMS_IN_LIST)
    generate_random_list = random.sample(
        range(10000),
        random_num_of_list_length
    )
    insertion_sort_execution_time = insertion_sort(generate_random_list)
    generate_random_list_2 = random.sample(
        range(10000),
        random_num_of_list_length
    )
    shell_sort_execution_time = shell_sort(generate_random_list_2)
    execution_time = float(insertion_sort_execution_time) + float(
        shell_sort_execution_time)
    insertion_percent = float(insertion_sort_execution_time)*100/execution_time
    print("Insertion sort took %{} seconds to run, on average".format(
        insertion_percent))
    shell_sort_percentage = 100 - float(insertion_percent)
    print("Shell sort took %{} seconds to run, on average".format(
        shell_sort_percentage))


python_sort()
