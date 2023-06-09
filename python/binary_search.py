def binary_search(s, e, num1, j):
    while s <= e:
        mid = (s+e) // 2

        if num1[mid] == j:
            return 1
        elif num1[mid] < j:
            s = mid+1
        else:
            e = mid-1
    return 0