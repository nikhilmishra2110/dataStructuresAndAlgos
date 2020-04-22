def remove_duplicates(arr):
  # index of the next non-duplicate element
  b_pointer = 1

  i = 1
  while(i < len(arr)):
    if arr[b_pointer - 1] != arr[i]:
      arr[b_pointer] = arr[i]
      b_pointer += 1
    i += 1
    print ("b_pointer -> ", b_pointer)
    print ("i ->", i)

  return b_pointer


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

main()