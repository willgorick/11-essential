#check if one array is a rotation of the other
#Can assume no duplicates

def is_rotation(list1, list2):
  a_len, b_len = len(list1), len(list2)
  if a_len != b_len:
    return False

  b_rotation_start = -1
  for i in range(a_len):
    if list2[i] == list1[0]:
      b_rotation_start = i
      break

  if b_rotation_start == -1: #didn't find the starting value from array a anywhere in array b
    return False

  for i in range(a_len):
    if list1[i] != list2[(i + b_rotation_start) % a_len]:
      return False
  return True

def main():
  print(is_rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))
  print(is_rotation([1,2,3,4,5,6,9], [4,5,6,7,1,2,3]))

main()

#solution analysis:
#time: O(n)
#space: O(1), just storing the array length variables, and the b_rotation_start variable
