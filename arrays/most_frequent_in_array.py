#return the most frequently occuring character in an array
def most_frequent(array):
  char_map = {}
  max_char, max_count = None, -1

  for num in array:
    char_map[num] = char_map.get(num, 0) + 1
    if char_map[num] > max_count:
      max_count = char_map[num]
      max_char = num

  return max_char

def main():
  print(most_frequent([0, -1, 10, 10, -1, 10, -1, -1, -1, 1]))
  print(most_frequent([1,3,1,3,2,1]))

main()

#solution analysis:
#Time: O(n)
#SPace: O(n), if every single character is unique