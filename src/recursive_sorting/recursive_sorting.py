# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
  elements = len( arrA ) + len( arrB )
  merged_arr = []
  # TO-DO
  L = 0
  R = 0
  while L < len(arrA) and R < len(arrB):
    if arrA[L] < arrB[R]:
      merged_arr.append(arrA[L])
      L += 1
    else:
      merged_arr.append(arrB[R])
      R += 1
  
  return merged_arr + arrA[L:] + arrB[R:] 

# print(merge([1, 5, 8], [0, 3, 7]))

def splitInHalf(arr):
  half = len(arr) // 2
  return arr[:half], arr[half:]
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
  # TO-DO
  while len(arr) > 1:
    p1, p2 = splitInHalf(arr)
    ms1 = merge_sort(p1)
    ms2 = merge_sort(p2)
    return merge(ms1, ms2)
  return arr

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
  # TO-DO

  return arr

def merge_sort_in_place(arr, l, r): 
  # TO-DO

  return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

  return arr
