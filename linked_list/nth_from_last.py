class Node:
  def __init__(self, value, child=None):
    self.value = value;
    self.child = child

def nth_from_last(head, n):
  if head == None:
    return None
  p2, p1 = head, head
  p1 = head
  while p1 and n:
    n -= 1
    p1 = p1.child
  if n > 0:
    return None
  while p1:
    p1 = p1.child
    p2 = p2.child
  return p2.value

def main():
  current = Node(1)
  for i in range(2, 8):
      current = Node(i, current)
  head = current

  # print(nth_from_last(head, 1))
  # print(nth_from_last(head, 4))


  current2 = Node(4)
  for i in range(3, 0, -1):
      current2 = Node(i, current2)
  head2 = current2
  # print(nth_from_last(head2, 2))
  # print(nth_from_last(head2, 4))
  # print(nth_from_last(head2, 5))
  print(nth_from_last(None, 1))

main()