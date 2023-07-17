def max_sequence(arr):
    if len(arr) == 0 or all([x <= 0 for x in arr]):
        return 0
    max_sum = arr[0]
    ending_sum = 0
    for _ in range(len(arr)):
        ending_sum = ending_sum + arr[_]
        ending_sum = 0 if ending_sum < 0 else ending_sum
        max_sum = max(max_sum, ending_sum)
    return max_sum