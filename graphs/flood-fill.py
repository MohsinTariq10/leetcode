def floodFill(image, x, y, newColor):
    # Write your Code here.
    old_color = image[x][y]
    image[x][y] = newColor
    if newColor == old_color:
        return image
    q = [(x,y)]
    rows = len(image)
    cols = len(image[0])

    while q:
        a, b = q.pop()
        children = get_children(a,b, rows, cols)
        for child_a, child_b in children:
            if old_color == image[child_a][child_b]:
                q.append((child_a, child_b))
                image[child_a][child_b] = newColor
    return image
        

def get_children(a, b, rows, cols):
    children = []
    if a!=0:
        children.append((a-1, b))
    if b!=0:
        children.append((a, b-1))
    if a!=rows-1:
        children.append((a+1, b))
    if b!=cols-1:
        children.append((a, b+1))
    return children
