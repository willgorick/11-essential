# return all common elements between two arrays
# the input arrays are both sorted
def common_elements(arr_a, arr_b):
  len_a = len(arr_a)
  len_b = len(arr_b)
  pointer_a, pointer_b = 0, 0
  result = []
  while pointer_a < len_a and pointer_b < len_b:
    a_val = arr_a[pointer_a]
    b_val = arr_b[pointer_b]
    if a_val == b_val:
      result.append(a_val)
      pointer_a += 1
      pointer_b += 1
    elif a_val > b_val:
      pointer_b += 1
    else: #b_val > a_val
      pointer_a +=1

  return result

def main():
  print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))

main()

#solution analysis:
# Time: O(n + m), where n and m are the lengths of the two arrays
# Space: O(min(n, m)), our result list may contain up to all the 