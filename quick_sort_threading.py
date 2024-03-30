import random
import time
import threading
random.seed(1)

def threading_quicksort(arr):
    if len(arr) <= 1:
        return arr    
    pivot = arr[len(arr) // 2]
    left=[]
    middle=[]
    right=[]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else :
            middle.append(i)
    
    left_thread = threading.Thread(target=threading_quicksort,args=(left,))
    left_thread.start()
    right_thread = threading.Thread(target=threading_quicksort,args=(right,)) 
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return threading_quicksort(left.copy()) + middle + threading_quicksort(right.copy())

def quicksort(arr):
    if len(arr) <= 1:
        return arr    
    pivot = arr[len(arr) // 2]
    left=[]
    middle=[]
    right=[]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else :
            middle.append(i)
    
    return quicksort(left) + middle + quicksort(right)


def make_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(1,5000))
    return lst

if __name__ == '__main__':
    lst = make_list(100)
    my_lst = make_list(100)
    s = time.time()
    result = threading_quicksort(lst)
    e = time.time()
    print(e-s)
    s2 = time.time()
    result2 = quicksort(my_lst)
    e2 = time.time()
    print(e2-s2)