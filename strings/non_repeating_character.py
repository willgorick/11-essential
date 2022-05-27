#given a string, return the first character in the string that only occurs once.  If no such characters, return None
import math

def non_repeating_characters(given_string):
  char_map = {}
  for i in range(len(given_string)):
    if given_string[i] in char_map:
      count, ind = char_map[given_string[i]]
      char_map[given_string[i]] = [count+1, i]
    else:
      char_map[given_string[i]] = [1, i]

  min_ind, non_repeat_char = math.inf, None
  for key, val in char_map.items():
    if val[0] == 1:
      if val[1] < min_ind:
        min_ind = val[1]
        non_repeat_char = key
  return non_repeat_char

def main():
  print(non_repeating_characters("abcab"))
  print(non_repeating_characters("abacc"))
  print(non_repeating_characters("xxyzx"))

main()

#solution analysis:
#time: O(n), at most this solution will take 2n time to run; if every character is unique we will run through them all once to setup the dictionary, then again to find the one with the earliest index
#space: O(n) for the dict if every char is unique