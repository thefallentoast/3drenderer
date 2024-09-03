import pygame as pg
import random as rnd

import localmath as lmath

VERTICE_COLOR: pg.Color = pg.Color(0,255,0)
EDGE_COLOR: pg.Color = pg.Color(0,255,0)

WIN: pg.Surface = pg.display.set_mode((1024, 1024))
pg.display.set_caption("3d renderer!")

running: bool = True
focalLength: int = 100

rotatedX: int | float = 0
rotatedY: int | float = 45
rotatedZ: int | float = 0

drawnVertices: list[pg.Vector3] = []

clock = pg.time.Clock()

targetFPS = 60

ROTATE: bool = True
SPIN: bool = True

vertices: list[list[int, int, int]] = [
    [40,  40,  40],  # ftr
    [40, -40,  40],  # fbr
    [-40, -40,  40], # fbl
    [-40,  40,  40], # ftl
    [40,  40, -40],  # btr
    [40, -40, -40],  # bbr
    [-40, -40, -40], # bbl
    [-40,  40, -40], # btl
]

edges: list[list[int, int]] = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # front
    [4, 5], [5, 6], [6, 7], [7, 4],  # back
    [0, 4], [1, 5], [2, 6], [3, 7],  # connection
]


def drawVertice(vertice: pg.Vector3, rotate: bool) -> None:
    global rotatedX, rotatedY, rotatedZ
    global WIN, VERTICE_COLOR
    
    drawPosition: pg.Vector3 = vertice
    
    if rotate:
        drawPosition = lmath.rotateAroundX(drawPosition, rotatedX)
        drawPosition = lmath.rotateAroundY(drawPosition, rotatedY)
        drawPosition = lmath.rotateAroundZ(drawPosition, rotatedZ)
    
    projectedPosition = lmath.projectVertexOntoScreen(drawPosition, focalLength)

    projectedPosition = lmath.offsetVector2(projectedPosition, 500)
    
    pg.draw.circle(WIN, VERTICE_COLOR, projectedPosition, 3)

def drawEdge(edgePair: int, rotate: bool) -> None:
    global drawnVertices, WIN, EDGE_COLOR
    # pseudocode:
    # read edge pair
    # read corresponding vertices' positions
    # plot line
    verticeA = pg.Vector3(drawnVertices[edgePair[0]])
    verticeB = pg.Vector3(drawnVertices[edgePair[1]])
    
    if rotate:
        verticeA = lmath.rotateAroundX(verticeA, rotatedX)
        verticeA = lmath.rotateAroundY(verticeA, rotatedY)
        verticeA = lmath.rotateAroundZ(verticeA, rotatedZ)
        
        verticeB = lmath.rotateAroundX(verticeB, rotatedX)
        verticeB = lmath.rotateAroundY(verticeB, rotatedY)
        verticeB = lmath.rotateAroundZ(verticeB, rotatedZ)

    projectedVerticeA = lmath.projectVertexOntoScreen(verticeA, focalLength)
    projectedVerticeB = lmath.projectVertexOntoScreen(verticeB, focalLength)
    
    projectedVerticeA = lmath.offsetVector2(projectedVerticeA, 500)
    projectedVerticeB = lmath.offsetVector2(projectedVerticeB, 500)
    
    pg.draw.line(WIN, EDGE_COLOR, projectedVerticeA, projectedVerticeB)

def eventloop():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

def main():
    global rotatedX, rotatedY, rotatedZ, drawnVertices
    while (running):
        drawnVertices = []
        eventloop()
        WIN.fill(pg.Color(0,0,0))
        
        for i, v in enumerate(vertices):
            drawVertice(pg.Vector3(v), ROTATE)
            drawnVertices.append(v)
        
        for i, v in enumerate(edges):
            drawEdge(v, ROTATE)
        
        if SPIN:
            rotatedX += rnd.randrange(0, 2) - 1
            rotatedY += rnd.randrange(0, 1) - 1
            rotatedZ += rnd.randrange(0, 1) - 1
        
        pg.display.flip()
        
        clock.tick(targetFPS)
    pg.quit()   
        
if __name__ == "__main__":
    main()
