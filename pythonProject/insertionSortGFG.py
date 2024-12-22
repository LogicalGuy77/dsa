import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time taken to execute {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper

@measure_execution_time
def sort_array():
    arr = [4,1,3,9,7]
    n = 5

    temp = 0
    for i in range(0, n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break
            j -= 1
    print(arr)

sort_array()
