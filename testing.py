#!/usr/bin/env python
"""This script shows an example of using the PyWavefront module."""
import sys
sys.path.append('..')
import ctypes

import pyglet
from pyglet.gl import *
from pyglet.window import key

import pywavefront

rotation = 0

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
    glRotatef(rotation, 0, 1, 0)
    #glRotatef(-25, 1, 0, 0)
    #glRotatef(45, 0, 0, 1)
    #glEnable(GL_LIGHTING)

    meshes.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        global rotation
        rotation += 90
        glRotatef(rotation, 0, 1, 0)
        print('mouse clicked')

    elif symbol == key.RIGHT:
        print('right clicked')

    elif symbol == key.UP:
        print('up clicked')

    elif symbol == key.DOWN:
        print('down clicked')

def update(dt):
    global rotation
    rotation += 90*dt
    if rotation > 720: rotation = 0
    
pyglet.clock.schedule(update)

pyglet.app.run()
