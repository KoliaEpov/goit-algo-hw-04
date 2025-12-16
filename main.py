import random
import timeit
from insertion import insertion
from merge import merge_sort


def insertion_test(N):
    insertion([random.randint(0, 100) for _ in range(N)])


def merge_test(N):
    merge_sort([random.randint(0, 100) for _ in range(N)])


def timsort_test(N):
    arr = [random.randint(0, 100) for _ in range(N)]
    arr.sort()


def main():
    # print("Start insertion 10")
    # print(timeit.timeit(lambda: insertion_test(10), number=1))
    # print("End insertion 10")

    # print("Start insertion 50")
    # print(timeit.timeit(lambda: insertion_test(50), number=1))
    # print("End insertion 50")

    # print("Start insertion 100")
    # print(timeit.timeit(lambda: insertion_test(100), number=1))
    # print("End insertion 100")

    # print("Start insertion 200")
    # print(timeit.timeit(lambda: insertion_test(200), number=1))
    # print("End insertion 200")

    # print("Start insertion 400")
    # print(timeit.timeit(lambda: insertion_test(400), number=1))
    # print("End insertion 400")

    # print("Start insertion 800")
    # print(timeit.timeit(lambda: insertion_test(800), number=1))
    # print("End insertion 800")

    # print("Start merge 10")
    # print(timeit.timeit(lambda: merge_test(10), number=1))
    # print("End merge 10")

    # print("Start merge 50")
    # print(timeit.timeit(lambda: merge_test(50), number=1))
    # print("End merge 50")

    # print("Start merge 100")
    # print(timeit.timeit(lambda: merge_test(100), number=1))
    # print("End merge 100")

    # print("Start merge 200")
    # print(timeit.timeit(lambda: merge_test(200), number=1))
    # print("End merge 200")

    # print("Start merge 400")
    # print(timeit.timeit(lambda: merge_test(400), number=1))
    # print("End merge 400")

    # print("Start merge 800")
    # print(timeit.timeit(lambda: merge_test(800), number=1))
    # print("End merge 800")

    print("Start timsort 10")
    print(timeit.timeit(lambda: timsort_test(10), number=1))
    print("End timsort 10")

    print("Start timsort 50")
    print(timeit.timeit(lambda: timsort_test(50), number=1))
    print("End timsort 50")

    print("Start timsort 100")
    print(timeit.timeit(lambda: timsort_test(100), number=1))
    print("End timsort 100")

    print("Start timsort 200")
    print(timeit.timeit(lambda: timsort_test(200), number=1))
    print("End timsort 200")

    print("Start timsort 400")
    print(timeit.timeit(lambda: timsort_test(400), number=1))
    print("End timsort 400")

    print("Start timsort 800")
    print(timeit.timeit(lambda: timsort_test(800), number=1))
    print("End timsort 800")


if __name__ == "__main__":
    main()
