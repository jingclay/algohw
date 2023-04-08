def even_odd(arr:list):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] % 2 == 0:
            i += 1
        else:
            if arr[j] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j -= 1

    return arr


test_list = [1, 7, 3, 2, 8, 10, 12]
print(test_list)
test_result_list = even_odd(test_list)
print(test_result_list)
print(test_list)


def increment_number(arr:list):
    list8 = 1
    for i in range(len(arr)-1, -1, -1):
        arr[i] += list8
        if arr[i] < 10:
            list8 = 0
            break
        arr[i] = 0
    if list8 == 1:
        arr.insert(0, 1)
    return arr

test_list2 = [1,6,8]
test_list3 = [1,9,9]
test_list4 = [9,9,9]
print(increment_number(test_list2))
print(increment_number(test_list3))
print(increment_number(test_list4))