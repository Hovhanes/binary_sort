def binary_search(arr, val, start, end):
    print(arr, val, start, end)
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)  # Use binary search for already sorted array
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


def test_insertion_binary_sort_success():
    integers_list = [1, 4, 3, 2, 5]
    expected_result = [1, 2, 3, 4, 5]
    result = insertion_binary_sort(integers_list)
    message = "Test pass OK"

    if result != expected_result:
        message = f"Test fail {expected_result} != {result}"

    print(message)


test_insertion_binary_sort_success()
