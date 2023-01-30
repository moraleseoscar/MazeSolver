# Python3 program for the above approach
from collections import deque as queue
 
# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
 
# Function to check if a cell
# is be visited or not
def isValid(vis, row, col):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= 4 or col >= 4):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False

    if (grid[row][col] == 0):
        return False
 
    # Otherwise
    return True
 
# Function to perform the BFS traversal
def BFS(grid, vis, row, col):
   
    # Stores indices of the matrix cells
    q = queue()
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")
 
        if(grid[x][y] == 1):
            print(path[x][y])
            return x,y;
            break
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                if path[adjx][adjy]==[]:
                    path[adjx][adjy]=[x,y]
                q.append((adjx, adjy))
                vis[adjx][adjy] = True

    
 
# Driver Code
if __name__ == '__main__':
   
    # Given input matrix
    grid= [ [ 'a', 'b', 'c', 'd' ],
           [ 'e', 0, 'g', 'h' ],
           [ 'i', 0, 'k', 'l' ],
           [ 'm', 0, 1, 'p' ] ]
 
    # Declare the visited array
    vis = [[ False for i in range(4)] for i in range(4)]
    path = [[ [] for i in range(4)] for i in range(4)]
    # vis, False, sizeof vis)
    finy, finx = BFS(grid, vis, 0, 0);
    
    print(finy, finx)

    final = True;
    completa = []
    while final:
        if  path[finy][finx] != []: 
            finy = path[finy][finx][0]
            finx = path[finy][finx][1]
        else:
            final = False;
    
    print(completa)
 
#  [
#     [[], [0, 0], [0, 1], [0, 2]], 
#     [[0, 0], [], [0, 2], [0, 3]], 
#     [[1, 0], [], [1, 2], [1, 3]], 
#     [[2, 0], [], [2, 2], [2, 3]]]