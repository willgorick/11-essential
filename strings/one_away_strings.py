
#take two strings and return true if they are one character away from being the same.  i.e., "abcde" and "abfde" would return true

def one_away(s1, s2):
  l1, l2 = len(s1), len(s2)
  diff_count = 0
  if abs(l1-l2) > 1:
    return False
  if l1 == l2:
    for i in range(l1):
      if s1[i] != s2[i]:
        diff_count += 1
        if diff_count > 1:
          return False
    return True
  elif l1 > l2:
   return is_one_away_diff_len(s1, s2)
  else: #l2 > l1
   return is_one_away_diff_len(s2, s1)

def is_one_away_diff_len(s1, s2):
  j, diff_count = 0, 0
  for i in range(len(s1)):
    if j >= len(s2):
      return diff_count < 2
    if s1[i] != s2[j]:
      diff_count += 1
      if diff_count >= 2:
        return False
      j-= 1
    j += 1 #the first time they aren't the same, decrement j
  return True

def main():
  print(one_away('abcde', 'abfde')) #should return True
  print(one_away('abcde', 'abfda')) #should return False
  print(one_away("abcde", "abde")) #should return True
  print(one_away("abcde", "abdef")) #should return False
  print(one_away("xyz", "xyaz")) #should return True
  print(one_away("xyz", "xyax")) #should return False
  print(one_away("abcde", "abcd"))  # should return True
  print(one_away("abde", "abcde"))  # should return True
  print(one_away("a", "a"))  # should return True
  print(one_away("abcdef", "abqdef"))  # should return True
  print(one_away("abcdef", "abccef"))  # should return True
  print(one_away("abcdef", "abcde"))  # should return True
  print(one_away("aaa", "abc"))  # should return False
  print(one_away("abcde", "abc"))  # should return False
  print(one_away("abc", "abcde"))  # should return False
  print(one_away("abc", "bcc"))  # should return False

main()

#solution analysis:
#time: O(n)
#space: O(1)