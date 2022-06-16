import math
def rotate_out_of_place(grid):
  sq_len = len(grid)
  new_grid = [[0 for x in range(sq_len)] for y in range(sq_len)]
  for i in range(sq_len):
    for j in range(sq_len):
      new_grid[j][sq_len-i-1] = grid[i][j]
  return new_grid 

def rotate_sub(i, j, n):
  return j, n-1-i

def rotate_in_place(grid):
  sq_len = len(grid)
  print(sq_len)
  for i in range(math.ceil(sq_len/2)):
    for j in range(sq_len//2):
      tmp = [0,0,0,0]
      curr_i, curr_j = i, j
      for k in range(4):
        tmp[k] = grid[curr_i][curr_j]
        curr_i, curr_j = rotate_sub(curr_i, curr_j, sq_len)
      for k in range(4):
        grid[curr_i][curr_j] = tmp[(k-1) %4]
        curr_i, curr_j = rotate_sub(curr_i, curr_j, sq_len)
  return grid

def main():
  grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]

  goal = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
  ]
  # rotated_grid = rotate_out_of_place(grid)
  # print(rotated_grid)
  # print(rotated_grid == goal)


  rotated_grid = rotate_in_place(grid)
  print(rotated_grid)
  print(rotated_grid == goal)

main()