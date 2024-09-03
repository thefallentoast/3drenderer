import pygame as pg
from math import sin, cos, radians

def offsetVector3(origin: pg.Vector3, offset: int) -> pg.Vector3:
    returnValue: pg.Vector3 = origin
    
    returnValue.x += offset
    returnValue.y += offset
    returnValue.z += offset
    
    return returnValue

def offsetVector2(origin: pg.Vector2, offset: int) -> pg.Vector3:
    returnValue: pg.Vector2 = origin
    
    returnValue.x += offset
    returnValue.y += offset
    
    return returnValue

def projectVertexOntoScreen(position: pg.Vector3, focalLength: int) -> pg.Vector2:
    '''
    Calculate X and Y coordinates ready to be plotted onto screen based on
    vertex position and focal length.
    '''
    
    returnValue: pg.Vector2 = pg.Vector2(0,0)
    
    returnValue.x = int((focalLength * position.x) // (focalLength + position.z))
    returnValue.y = int((focalLength * position.y) // (focalLength + position.z))
    
    return returnValue
    
def rotateAroundX(origin: pg.Vector3, angle: int) -> pg.Vector3:
    '''
    Rotate origin by angle around the X axis.
    Expects angle in degrees.
    '''
    returnValue: pg.Vector3 = pg.Vector3(0,0,0)
    
    theta = radians(angle)
    
    returnValue.x = origin.x
    returnValue.y = (origin.y * cos(theta)) - (origin.z * sin(theta))
    returnValue.z = (origin.y * sin(theta)) + (origin.z * cos(theta))
    
    return returnValue

def rotateAroundY(origin: pg.Vector3, angle: int) -> pg.Vector3:
    '''
    Rotate origin by angle around the Y axis.
    Expects angle in degrees.
    '''
    returnValue: pg.Vector3 = pg.Vector3(0,0,0)
    
    theta = radians(angle)
    
    returnValue.x = (origin.x * cos(theta)) + (origin.z * sin(theta))
    returnValue.y = origin.y
    returnValue.z = (-origin.x * sin(theta)) + (origin.z * cos(theta))
    
    return returnValue

def rotateAroundZ(origin: pg.Vector3, angle: int) -> pg.Vector3:
    '''
    Rotate origin by angle around the Z axis.
    Expects angle in degrees.
    '''
    returnValue: pg.Vector3 = pg.Vector3(0,0,0)
    
    theta = radians(angle)
    
    returnValue.x = (origin.x * cos(theta)) - (origin.y * sin(theta))
    returnValue.y = (origin.x * sin(theta)) + (origin.y * cos(theta))
    returnValue.z = origin.z
    
    return returnValue

def rotationSplitVector3(rotation: pg.Vector3) -> list[int, int, int]:
    return [rotation.x, rotation.y, rotation.z]

def rotationUniteList(rotation: list[int, int, int]):
    returnValue: pg.Vector3 = pg.Vector3(0,0,0)
    
    returnValue.x = rotation[0]
    returnValue.y = rotation[1]
    returnValue.z = rotation[2]
    
    return returnValue
    
