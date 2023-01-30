from PIL import Image
from collections import deque as queue
 
start = [];
end = [];
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def pixelate(input_file_path, output_file_path, pixel_size):
    threshold = 127
    red = True;
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.convert("RGB")
    r,g,b = image.split()
    r = r.point(lambda x: 255 * (x > threshold))
    g = g.point(lambda x: 255 * (x > threshold)) 
    b = b.point(lambda x: 255 * (x > threshold))
    image = Image.merge("RGB", (r,g,b))
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel[1] > threshold and pixel[0] < threshold and pixel[2] < threshold:
                end.append((x,y))
            if red and pixel[0] > threshold and pixel[1] < threshold and pixel[2] < threshold:
                red = False;
                image.putpixel((x,y),(255,0,0))
                start.append((x,y));
            elif not red and pixel[0] > threshold and pixel[1] < threshold and pixel[2] < threshold:
                image.putpixel((x,y), (255,255,255))

    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.save(output_file_path)

 
def isValid(vis, row, col, width, height, grid):
   
    if (row < 0 or col < 0 or row >= width or col >= height):
        return False
 
    if (vis[row][col]):
        return False
    
    if (grid[col][row] == (0,0,0)):
        return False

    return True

def BFS(path):
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

    q = queue()
 
    q.append((start[0][0], start[0][1]))
    vis[start[0][0]][start[0][1]] = True
 
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]

        if (grid[y][x] == (0,255,0)):
            print('encontrado') 
            finy, finx = y, x;
            break
 
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy, width, height, grid)):
                if path[adjx][adjy]==[]:
                    path[adjx][adjy]=[x,y]
                q.append((adjx, adjy))

                # img.putpixel((adjx,adjy), (125,0,125))
                vis[adjx][adjy] = True


    final = True;
    while final:
        try: 
            img.putpixel((finx,finy), (125,0,125))
            finx = path[finx][finy][0]
            finy = path[finx][finy][1]
        except:
            final = False;

    img.save("InteligenciaArtificial\Lab 1\Result.png")

def DFS(path):
    # Cargar la imagen
    img = Image.open(path)
    img = img.resize(
            (img.size[0] // newta, img.size[1] // newta),
            Image.NEAREST
        )

    pixel_data = list(img.getdata())

    width, height = img.size
    pixel_data = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
    grid = pixel_data

    vis = [[ False for i in range(width)] for i in range(height)]
    path = [[ [] for i in range(width)] for i in range(height)]

    st = []
    st.append([start[0][0], start[0][1]])
    
    while (len(st) > 0):
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]
 
        if (isValid(vis, row, col, width, height, grid) == False):
            continue
        
        vis[row][col] = True
 
        if (grid[col][row] == (0,255,0)):
            print('encontrado')
            break
 
        img.putpixel((row,col), (125,0,125))

        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])

    img.save("InteligenciaArtificial\Lab 1\Result.png")

if __name__ == '__main__':
    newta = 4;
   #Crea la imagen y muestra el inicio
    #pixelate("InteligenciaArtificial\Lab 1\Turing.png", "InteligenciaArtificial\Lab 1\TuringConverted.png", newta);
    pixelate("InteligenciaArtificial\Lab 1\Image1.bmp", "InteligenciaArtificial\Lab 1\Image1Converted.png", newta);
    print(start)
    # BFS("InteligenciaArtificial\Lab 1\Image1Converted.png");
    DFS("InteligenciaArtificial\Lab 1\Image1Converted.png")
    
    

