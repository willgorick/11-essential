from collections import deque

def click_dfs(field, num_rows, num_cols, given_i, given_j):
  print(field[given_i][given_j])
  print(given_i, given_j)
  if field[given_i][given_j] != 0:
    return field
  print(field[given_i][given_j])
  dfs(field, num_rows, num_cols, given_i, given_j)
  return field

def click_queue(field, num_rows, num_cols, given_i, given_j):
  if field[given_i][given_j] != 0:
    return field
  field[given_i][given_j] = -2
  queue = deque()
  queue.append((given_i, given_j))

  while queue:
    (start_i, start_j) = queue.popleft()
    for i in range(start_i -1, start_i+2):
      for j in range(start_j-1, start_j+2):
        if 0 <= i < num_cols and 0 <= j < num_rows and field[i][j] == 0:
          field[i][j] = -2
          queue.append((i,j))
  return field

#dfs with recursion
def dfs(field, num_rows, num_cols, i, j):
  if i >= 0 and j >= 0 and i < num_rows and j < num_cols and field[i][j] == 0:
    print("wut")
    field[i][j] = -2
    dfs(field, num_rows, num_cols, i-1, j)
    dfs(field, num_rows, num_cols, i-1, j-1)
    dfs(field, num_rows, num_cols, i-1, j+1)
    dfs(field, num_rows, num_cols, i+1, j-1)
    dfs(field, num_rows, num_cols, i+1, j)
    dfs(field, num_rows, num_cols, i+1, j+1)
    dfs(field, num_rows, num_cols, i, j-1)
    dfs(field, num_rows, num_cols, i, j+1)


def main():
  field1 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, -1, 1, 0]
  ]
  # result1 = click_dfs(field1, 3, 5, 2, 2)
  # for row in result1:
  #   print(row)
  
  result2 = click_dfs(field1, 3, 5, 1, 4)
  for row in result2:
    print(row)

  # resulttest = click_dfs(
  #   [
  #     [-1,-1,-1],
  #     [0,0,0],
  #     [0,1,1]
  #   ], 3, 3, 1, 1)
  # for row in resulttest:
  #   print(row)
  # print()
  # result3 = click_queue(field2, 4, 4, 1, 3) 
  # for row in result3:
  #   print(row)
  # print()

main()
  