from PIL import Image
# Python 3 program of the above approach

start = [(9, 112)]
# Function to check if mat[row][col]
# is unvisited and lies within the
# boundary of the given matrix
def isValid(vis, row, col, width, height, grid):
   
    if (row < 0 or col < 0 or row >= width or col >= height):
        return False
 
    # If the cell is already visited
    if (vis[row][col]):
        return False
    
    if (grid[col][row] == (0,0,0)):
        return False

    # Otherwise, it can be visited
    return True
 
# Function to perform DFS
# Traversal on the matrix grid[]
def DFS(path):

    # Initialize direction vectors
    # dRow = [0, 1, 0, -1]
    # dCol = [-1, 0, 1, 0]
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]
    # Cargar la imagen
    img = Image.open(path)
    img = img.resize(
            (img.size[0] // newta, img.size[1] // newta),
            Image.NEAREST
        )

    # Obtener los datos de los pixeles en forma de un array 2D
    pixel_data = list(img.getdata())

    width, height = img.size
    pixel_data = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
    grid = pixel_data

    vis = [[ False for i in range(width)] for i in range(height)]
    path = [[ [] for i in range(width)] for i in range(height)]

    # Initialize a stack of pairs and
    # push the starting cell into it
    st = []
    st.append([start[0][0], start[0][1]])
    
    # Iterate until the
    # stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]
 
        # Check if the current popped
        # cell is a valid cell or not
        if (isValid(vis, row, col, width, height, grid) == False):
            continue
        
        # Mark the current
        # cell as visited
        vis[row][col] = True
 
        # Print the element at
        # the current top cell
        if (grid[col][row] == (0,255,0)):
            print('encontrado')
            break
 
        img.putpixel((row,col), (125,0,125))
        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])

    img.save("InteligenciaArtificial\Lab 1\Result.png")

 
# Driver Code
if __name__ == '__main__':
    newta = 4;
    grid =  [['s', 2, 3],
             [0, 9, 8],
             ['e', 0, 1]]
 
    # Function call
    DFS("InteligenciaArtificial\Lab 1\Image1Converted.png")
# grid = [['s', 2, 3],
#         [0, 9, 8],
#         [1, 0, 1]]
