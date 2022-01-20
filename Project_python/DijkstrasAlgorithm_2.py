from dis import dis
from MinHeap_Dijjkstras import *
#Using Min Heap to lookup the 

#O((v+e)*logv) Time | O(v) space 
def dijkstrasAlgorithm(start,edges):
    numVertices = len(edges)
    distances= [float('inf')]*numVertices
    distances[start] = 0 
    
    dist_Heap = MinHeap([(id,float('inf')) for id in range(len(distances))])
    dist_Heap.update(start,0)
    
    visited = set()

    while len(visited) != numVertices:
        vertex, currentMinDistance = dist_Heap.remove()

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
                dist_Heap.update(destination,newPathDistance)
            
    return list(map(lambda x: -1 if x==float('inf') else x, distances))










if __name__ =="__main__":
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    minDistanceArr= dijkstrasAlgorithm(start,edges)

    print('\n')



