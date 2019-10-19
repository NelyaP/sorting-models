import random

lst = random.sample(range(20000), 10000)
cnt = 0
# test
def test_qs(lst):
    i = 1
    while i < (len(lst) - 1):
        if lst[i] < lst[i-1]:
            print(i)
            return False
        i += 1
    return True

def partition(lst, low, high): 
    i = low - 1 
    pivot = lst[high]  
    for j in range(low, high): 
        if lst[j] <= pivot: 
            i = i + 1 
            lst[i],lst[j] = lst[j],lst[i] 
    lst[i + 1],lst[high] = lst[high],lst[i + 1] 
    return i + 1 

def qSort(lst, low, high):
    global cnt
    if low < high:
        p = partition(lst, low, high)
        qSort(lst, low, p - 1)
        qSort(lst, p + 1, high)
        cnt = cnt + 1
    return lst

qSort(lst, 0, len(lst) - 1)
print(test_qs(lst))
print(cnt)