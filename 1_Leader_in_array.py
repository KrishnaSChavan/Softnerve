def ans(arr : list) -> list:
    if not arr:
        return []
    ar = []
    max = arr[-1]
    ar.append(max)
    for i in range(len(arr)):
        if max < arr[len(arr)-i-1]:
            max = arr[len(arr)-i-1]
            ar.append(max)
    return ar[::-1]
    

y = ans([7,10,4,10,6,5,2])

print(y)