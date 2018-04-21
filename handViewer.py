"""
Must have PyWavefront and pyglet to run

pip install PyWavefront
pip install pyglet
python3 handViewer.py
"""
import sys
sys.path.append('..')
import ctypes

import pyglet
from pyglet.gl import *
from pyglet.window import key

import pywavefront

offset = 5

xRotation = 0
yRotation = 0
zRotation = 0

meshes = pywavefront.Wavefront('hand.OBJ')

window = pyglet.window.Window(width = 1024, height = 700)

lightfv = ctypes.c_float * 4

@window.event
def on_resize(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., float(width)/height, 1., 100.)
    glMatrixMode(GL_MODELVIEW)
    return True

@window.event
def on_draw():
    window.clear()
    glLoadIdentity()

    #glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))
    #glEnable(GL_LIGHT0)

    glTranslated(0, 0, -3)
    glRotatef(xRotation, 0, 1, 0)
    glRotatef(yRotation, 1, 0, 0)
    glRotatef(zRotation, 0, 0, 1)
    #glRotatef(-25, 1, 0, 0)
    #glRotatef(45, 0, 0, 1)
    #glEnable(GL_LIGHTING)

    meshes.draw()

@window.event
def on_key_press(symbol, modifiers):
    global xRotation
    global yRotation
    global zRotation

    if symbol == key.LEFT:
        xRotation += offset

    elif symbol == key.RIGHT:
        xRotation -= offset

    elif symbol == key.UP:
        yRotation += offset

    elif symbol == key.DOWN:
        yRotation -= offset

    elif symbol == key.M:
        zRotation -= offset

    elif symbol == key.N:
        zRotation += offset

def update(dt):
    global xRotation
    global zRotation
    global yRotation

    if xRotation > 720: xRotation = 0
    if yRotation > 720: yRotation = 0
    if zRotation > 720: zRotation = 0
    
pyglet.clock.schedule(update)

pyglet.app.run()
