# 3drenderer
A 3D renderer made with python

It uses rotation matrices to spin the object around, and trigonometry to plot it to the screen.
This isn't fast, nor efficient, but this was just to learn about the math behind-the-scenes.

# REQUIRES:
PyGame and ArgParse, install them with pip:
```bash
pip install pygame argparse
```
Or if on linux-
```bash
sudo apt-get update && sudo apt-get install python3-pygame python3-argparse
```

# HOW TO USE
It requires a file with the vertice and edge data, I've provided an example file which is 'example.txt".
The syntax is very simple, use 'vertices' (no quotes) to indicate the start of the vertice data, then use
'edges' to indicate start of the edge data.
The edge data must come after the vertice data, else the program crashes. No comments, no nothing either.
The example file has a cube's data written onto it, take a look for help.
When you run the program, it takes in argument '--filename', and after it the name of the file to read.
It runs at 60fps and has a focalLength of 100.
Want it to not spin? Change the SPIN variable inside `main.py` to `False`. You can use notepad for that.
Want it to not appear at any angle, at all (effectively turning it 2D)? Change the ROTATE variable inside `main.py` to `False`.
please note, this is rotatedX when downloaded: 
```py
rotatedX: int | float = 0
```
If I wanna change it to start at 45°, for example:
```py
rotatedX: int | float = 45
```
Do NOT touch anything else. Same for the other variables.
You can find the description for each variable inside `descriptions.md`
