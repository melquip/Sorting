# TO-DO: Complete the selection_sort() function below 
def swap(arr, i1, i2):
  # print(f'swap: {i1}, {i2}')
  arr[i1], arr[i2] = arr[i2], arr[i1]
  return arr

def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    current = i
    smallest = current
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    for j in range(current, len(arr)):
      #print(f'current:{current}, smallest:{smallest}')
      #print(f'{arr[j]} < {arr[current]} {arr[j] < arr[current]}')
      if arr[j] < arr[smallest]:
        smallest = j
    # TO-DO: swap
    if current != smallest:
      #print(f'switch: {current} {smallest}')
      swap(arr, current, smallest)
      #print(f'switch: {arr}')
  return arr

# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  # compare first pair of elements
    # if left less than right element
      # swap those two elements
  # largest value has bubbled to the end of array
  # repeat until no swaps are done
  swaps = True
  while swaps:
    swaps = False
    for i in range(0, len(arr) - 1):
      currN = i
      nextN = currN + 1
      # print(f'bubble: {currN}, {nextN} | {arr[currN]}, {arr[nextN]}')
      if arr[currN] > arr[nextN]:
        swap(arr, currN, nextN)
        swaps += 1



  return arr

# print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
  if maximum < 0:
    return arr
  count = [0] * (maximum + 1)
  for x in arr:
    count[x] += 1
  total = 0
  for x in range(maximum + 1):
    for z in range(count[x]):
      arr[total] = x
      total += 1

  return arr

print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7], 9))
