from pyglet.gl import *

from pyglet import app, graphics
from pyglet.window import Window, key
import numpy as np

d, d1, d2 = 5, 10, 15
wx, wy = 1.5 * d2, 1.5 * d2
width, height = int(30 * wx), int(30 * wy)
window = Window(visible=True, width=width, height=height, resizable=True)
glClearColor(0.1, 0.1, 0.1, 1.0)
glClear(GL_COLOR_BUFFER_BIT)


def texInit():
    iWidth = iHeight = 64
    n = 3 * iWidth * iHeight
    img = np.zeros((3, iWidth, iHeight), dtype='uint8')
    for i in range(iHeight):
        for j in range(iWidth):
            img[:, i, j] = ((i - 1) & 16 ^ (j - 1) & 16) * 255
    img = img.reshape(n)
    # новые строки
    for i in range(2, n, 3):
        img[i] = 0
    # /новые строки
    img = (GLubyte * n)(*img)
    p, r = GL_TEXTURE_2D, GL_RGB
    glTexParameterf(p, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(p, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(p, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(p, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(p, 0, r, iWidth, iHeight, 0, r, GL_UNSIGNED_BYTE, img)
    glEnable(p)


texInit()
zv = -d2 / 2
v0, v1, v2, v3 = (-d2, d2, zv), (-d1, d1, 0), (d1, d1, 0), (d2, d2, zv)

# было ('t2f', (0, 1, 0, 0, 1, 0, 1, 1))
# стало ('t2f', t0 + t1 + t2 + t3)
# новые строки
#for i in range(2, n, 3):
#    img[i] = 0

# d1 < d2
a = 2*d1
b = 2*d2
h = d1 + d2
t0 = [0, 1]
t1 = [(b-a)/2 / b, 0]
t2 = [((b-a)/2+a) / b, 0]
t3 = [1, 1]

@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-wx, wx, -wy, wy, -20, 20)
    glRotatef(90, 1, 0, 0)
    graphics.draw(4, GL_QUADS, ('v3f', (v0 + v1 + v2 + v3)), ('t2f', t0 + t1 + t2 + t3))


app.run()
