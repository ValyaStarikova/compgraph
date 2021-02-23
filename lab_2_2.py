import pyglet
from pyglet import app, gl, graphics
from pyglet.window import Window, key
import numpy as np
d, d2 = 12, 10
wx, wy = 1.5 * d, 1.2 * d # Параметры области визуализации
width, height = int(20 * wx), int(20 * wy) # Размеры окна вывода
window = Window(visible = True, width = width, height = height,
                resizable = True, caption = 'lab_2_2')
gl.glClearColor(0.1, 0.1, 0.1, 1.0)
gl.glClear(gl.GL_COLOR_BUFFER_BIT)

gl.glLineWidth(3)
gl.glPointSize(16)

def f(x, d):
    return [d*np.cos(x), d*np.sin(x)]


@window.event
def on_draw():
    window.clear()
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-wx, wx, -wy, wy, -1, 1)

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1, 0.5, 1)
    gl.glVertex3f(d, d, 0)
    gl.glColor3f(1, 1, 0.5)
    gl.glVertex3f(d, -d, 0)
    gl.glColor3f(0.5, 1, 1)
    gl.glVertex3f(-d, -d, 0)
    gl.glColor3f(1, 0.5, 0.5)
    gl.glVertex3f(-d, d, 0)
    gl.glColor3f(1, 1, 1)
    gl.glEnd()

    pattern = '0b1111000011110000'
    gl.glLineStipple(2, int(pattern, 2))  

    gl.glColor3f(1, 0.5, 0.5)
    gl.glBegin(gl.GL_LINES)
    gl.glVertex3f(-20*d, 0, 0)
    gl.glVertex3f(20*d, 0, 0)
    gl.glVertex3f(0, -20*d, 0)
    gl.glVertex3f(0, 20*d, 0)
    gl.glEnd()

    gl.glDisable(gl.GL_LINE_STIPPLE)
    gl.glColor3f(1, 1, 1)

    gl.glBegin(gl.GL_LINE_LOOP)
    for i in range(0, 5):
        gl.glVertex3f(f(2*np.pi*i/5, d)[0], f(2*np.pi*i/5, d)[1], 0)
    gl.glEnd()

    gl.glBegin(gl.GL_POINTS)
    gl.glVertex3f(0, 0, 0)
    gl.glEnd()
    
    gl.glDisable(gl.GL_POINT_SMOOTH)
    gl.glBegin(gl.GL_POINTS)
    for i in range(0, 5):
        gl.glVertex3f(f(2*np.pi*i/5, d)[0], f(2*np.pi*i/5, d)[1], 0)
    gl.glEnd()

    graphics.draw(3, gl.GL_TRIANGLES,
                ('v2f', (
                f((2*np.pi*1/3)+ np.pi/2, d/3)[0], 
                f((2*np.pi*1/3)+ np.pi/2, d/3)[1],    

                f((2*np.pi*2/3)+ np.pi/2, d/3)[0], 
                f((2*np.pi*2/3)+ np.pi/2, d/3)[1], 

                f((2*np.pi*3/3)+ np.pi/2, d/3)[0],
                f((2*np.pi*3/3)+ np.pi/2, d/3)[1]
                )),
                ('c3f', (
                1, 0, 0, 
                0, 1, 0, 
                0, 0, 1
                )))

@window.event
def on_key_press(symbol, modifiers):
    mode_f = mode_b = None
    shade_model = None

    if symbol == key._1:
        gl.glEnable(gl.GL_LINE_STIPPLE)

    elif symbol == key._2:
        gl.glDisable(gl.GL_LINE_STIPPLE)

    elif symbol == key._3:
        mode_f = mode_b = gl.GL_FILL
        shade_model = gl.GL_FLAT

    elif symbol == key._4:
        mode_f = gl.GL_POINT
        mode_b = gl.GL_LINE
        shade_model = gl.GL_SMOOTH

    elif symbol == key._5:
        gl.glEnable(gl.GL_POINT_SMOOTH)

    elif symbol == key._6:
        gl.glDisable(gl.GL_POINT_SMOOTH)

    elif symbol == key._7:
        mode_f = mode_b = gl.GL_FILL
        shade_model = gl.GL_SMOOTH

    if mode_f is not None:
        gl.glPolygonMode(gl.GL_FRONT, mode_f)
        gl.glPolygonMode(gl.GL_BACK, mode_b)
        gl.glShadeModel(shade_model)
app.run()