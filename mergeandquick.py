import random
from time import time

def print_array(a):
    for i in range(len(a)):
        print(a[i])

'''
mergeSort algorithm
'''
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = mergeSort(array[:half])
    right = mergeSort(array[half:])

    return merge(left, right)

'''
FIN mergeSort algorithm
'''


'''
INICIO QUICKSORT
'''
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


'''
FIN QUICKSORT
'''



#n = input("Tamano del vector aleatorio: ")
f_merge=open("merge_data.txt", "w+")
f_quick=open("quick_data.txt", "w+")
n = 500000
for i in range(40):
    a = []
    mergeArray = []
    quickArray = []

    for j in range(n):
        num = random.randint(0,n)
        a.append(num)
        mergeArray.append(num)
        quickArray.append(num)
    time1 = time()
    mergeSort(mergeArray)
    time2 = time()
    time_mergeSort = time2 - time1
    time3 = time()
    quickSort(quickArray)
    time4 = time()
    time_quickSort = time4 - time3
    
    f_merge.write(str(time_mergeSort) + '\n')
    f_quick.write(str(time_quickSort) + '\n')
    print(time_mergeSort, time_quickSort)
f_merge.close()
f_quick.close()
    #print_array(a)


