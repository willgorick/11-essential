class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

#assume no duplicates 
#this is a binary tree, each node has 2 children
#no level attribute
#no back links
def lca(head, x, y):
  first_path = path_to_x(head, x, [])
  second_path = path_to_x(head, y, [])
  if first_path == None or second_path == None:
    return None
  i = 0
  min_len = min(len(first_path), len(second_path))
  while i < min_len and first_path[i] == second_path[i]:
    i += 1
  return first_path[i-1]

def path_to_x(node, x, path_so_far):
  if node == None:
    return None
  path_so_far.append(node.value)
  new_path1 = path_so_far.copy()
  new_path2 = path_so_far.copy()
  if node.value == x:
    return path_so_far
  left_sub = path_to_x(node.left, x, new_path1)
  if left_sub != None:
    return left_sub
  right_sub = path_to_x(node.right, x, new_path2)
  if right_sub != None:
    return right_sub
  return None

def create_tree(mapping, head_value):
  head = Node(head_value)
  nodes = {head_value: head}
  for key, value in mapping.items():
    nodes[value[0]] = Node(value[0])
    nodes[value[1]] = Node(value[1])
  for key, value in mapping.items():
    nodes[key].left = nodes[value[0]]
    nodes[key].right = nodes[value[1]]
  return head


def main():
  mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
  head1 = create_tree(mapping1, 0)
  # This tree is:
  # head1 = 0
  #        / \
  #       1   2
  #      /\   /\
  #     3  4 5  6

  mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
  head2 = create_tree(mapping2, 5)
  # This tree is:
  #  head2 = 5
  #        /   \
  #       1     4
  #      /\    / \
  #     3  8  9  2
  #    /\
  #   6  7

  print(lca(head1, 1, 5)) # should return 0
  print(lca(head1, 3, 1)) # should return 1
  print(lca(head1, 1, 4)) # should return 1
  print(lca(head1, 0, 5)) # should return 0
  print(lca(head2, 4, 7)) # should return 5
  print(lca(head2, 3, 3)) # should return 3
  print(lca(head2, 8, 7)) # should return 1
  print(lca(head2, 3, 0)) # should return None (0 does not exist in the tree)
main()



