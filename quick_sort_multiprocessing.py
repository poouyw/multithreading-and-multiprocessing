import random
import time
import multiprocessing


def multiprocessing_quicksort(arr):
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
    
    left_process = multiprocessing.Process(target=multiprocessing_quicksort,args=(left,))
    left_process.start()
    right_process = multiprocessing.Process(target=multiprocessing_quicksort,args=(right,)) 
    right_process.start()

    left_process.join()
    right_process.join()

    return multiprocessing_quicksort(left.copy()) + middle + multiprocessing_quicksort(right.copy())


def make_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(1,5000))
    return lst

if __name__ == '__main__':
    lst = make_list(10)
    s = time.time()
    result = multiprocessing_quicksort(lst)
    print(result)
    e = time.time() 
    print(e-s)
