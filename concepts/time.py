import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print("Time taken: {}".format(end - start))
        return value

    return wrapper
