import pygame as pg

def InterpretFile(filename: str) -> dict:
    '''
    Interpret filename file and return dictionary with keys
    "vertices" and "edges"
    File syntax should be:
    vertices
    0 0 1
    0 1 0
    0 1 1
    edges 
    0 1 
    1 0 
    1 1 '''
    with open(filename, "r") as f:
        lines: list = f.read().split("\n")
        try:
            verticeStart: int = lines.index("vertices") + 1
        except ValueError as e:
            print("Não definiu os vértices no arquivo.")
        try:
            edgeStart: int = lines.index("edges") + 1
        except ValueError as e:
            print("Não definiu as arestas no arquivo.")
        
        vertices: list = lines[verticeStart:edgeStart-1]
        edges: list = lines[edgeStart:]
        
        edgePairs: list = []
        for _, x in enumerate(edges):
            edgePairs.append(x.split(' '))
            
        verticeTrios: list = []
        for _, x in enumerate(vertices):
            verticeTrios.append(x.split(' '))
            
        for i, pair in enumerate(edgePairs):
            edgePairs[i] = [int(pair[0]), int(pair[1])]
        
        for i, trio in enumerate(verticeTrios):
            verticeTrios[i] = [int(trio[0]), int(trio[1]), int(trio[2])]
            
        returnValue = {
            "vertices": verticeTrios,
            "edges": edgePairs
        }
        
        return returnValue
        
print(InterpretFile("example.txt"))