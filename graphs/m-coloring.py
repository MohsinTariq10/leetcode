def graphColoring(mat,m):
    #Your code goes here
    colors = [0 for x in range(len(mat))]
    
    for i, c in enumerate(colors):
        if c != 0: continue
        visited = [i]
        q = [i]
        colors[i] = 1
        maxColors = 1
        while len(q) > 0:
            node = q.pop(0)
            adjacency = mat[node]
            for idx, adjacent in enumerate(adjacency):
                if adjacent == 0: continue # is say adjacent hai hi nai
                if colors[node] == colors[idx]:
                    colors[idx] +=1
                maxColors = max(maxColors, max(colors[idx], colors[node]))
                if maxColors > m:
                    return "NO"
                if idx not in visited:
                    visited.append(idx)
                    q.append(idx)
    return "YES"