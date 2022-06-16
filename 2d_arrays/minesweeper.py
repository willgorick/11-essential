#assume no duplicates in bombs
def minesweeper(bombs, num_rows, num_cols):
  field = [[0 for i in range(num_cols)] for j in range(num_rows)]

  for bomb in bombs:
    i = bomb[0]
    j = bomb[1]
    field[bomb[0]][bomb[1]] = -1
    #check all surrounding cells
    for x in range(i-1, i+2):
      for y in range(j-1, j+2):
        if is_valid(x, y, num_rows, num_cols, field):
          field[x][y] += 1

  return field
 
def is_valid(x, y, num_rows, num_cols, field):
   return x >= 0 and x < num_rows and y >= 0 and y < num_cols and field[x][y] != -1

def print_field(field):
  for row in field:
    print(row)
  print()
def main():
  print_field(minesweeper([[0,0], [0,1]], 3, 4))
  print_field(minesweeper([[0,0], [0,1], [1,2]], 3, 4))


main()

#solution analysis:
#time: O(b) where b is the number of bombs
#space: O(r*c), the number of rows * the number of columns