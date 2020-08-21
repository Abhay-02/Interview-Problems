def partition(arr, beg, end):
    loc = left = beg
    right = end
    flag = 0
    while flag != 1:
        while arr[right] > arr[loc] and loc != right:
            right -= 1

            if loc == right:
                flag = 1

            elif arr[loc] > arr[right]:
                arr[loc], arr[right] = arr[right], arr[loc]

            if flag != 1:
                