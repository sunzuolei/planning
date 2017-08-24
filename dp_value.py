# ----------
# Compute the value in dynamic programming
# ----------

grid = [[0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1

value = [[99 for row in range(len(grid[0]))] for col in range(len(grid)) ]
value[goal[0]][goal[1]] = 0
policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
policy[goal[0]][goal[1]] = '*'
for i in range(len(grid)):
   for j in range(len(grid[0])):
      if grid[i][j] == 1:
            policy[i][j] = '1'
change = True
i = 0
while change:
   change = False
   print (i)
   i = i + 1
   for x in range(len(grid)):
      for y in range(len(grid[0])):
         if grid[x][y] == 0:
            for a in range(len(delta)):
               x2 = x + delta[a][0]
               y2 = y + delta[a][1]

               if x2 >= 0 and x2 < len(grid)  and \
                  y2 >= 0 and y2 < len(grid[0]) and \
                  grid[x2][y2] == 0:
                  v2 = value[x][y] + cost_step
                  if v2 < value[x2][y2]:
                     change = True
                     value[x2][y2] = v2
                     policy[x2][y2] = delta_name[a]
                 
for i in range(len(value)):
   print (value[i])

print
#  The policy here is incorrect
for i in range(len(policy)):
   print (policy[i])
