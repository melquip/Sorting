# TO-DO: Complete the selection_sort() function below 
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
      swap = arr[current]
      arr[current] = arr[smallest]
      arr[smallest] = swap
      #print(f'switch: {arr}')
  return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

  return arr