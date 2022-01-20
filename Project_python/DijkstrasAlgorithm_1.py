#O(v**2 +e) Time | O(v) space 
def dijkstrasAlgorithm(start,edges):
    numVertices = len(edges)
    distances= [float('inf')]*numVertices
    distances[start] = 0 
    visited = set()

    while len(visited) != numVertices:
        vertex, currentMinDistance = VertexAndCurrMinDistance(distances,visited)

        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, NewDistance= edge
            if destination in visited:
                continue
            
            newPathDistance= NewDistance + currentMinDistance
            if newPathDistance < distances[destination]:
                distances[destination] = newPathDistance
            
    return list(map(lambda x: -1 if x==float('inf') else x, distances))







    return list(map(lambda x: -1 if float('inf') else x, distances))

def VertexAndCurrMinDistance(distances,visited):
    vertex = None
    currMinDistance = float('inf')

    for v,d in enumerate(distances):
        if v in visited:
            continue
        if d < currMinDistance:
            currMinDistance = d
            vertex = v
    
    return vertex,currMinDistance





if __name__ =="__main__":
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    minDistanceArr= dijkstrasAlgorithm(start,edges)

    print('\n')



