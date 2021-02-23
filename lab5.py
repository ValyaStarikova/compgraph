#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from pyglet.gl import *
from pyglet import app
from pyglet.window import Window, key
from math import sqrt
import random


# In[3]:


random.seed()
d = 12
wx, wy = 1.5 * d, 1.5 * d  # Параметры области визуализации
width, height = int(20 * wx), int(20 * wy)  # Размеры окна вывода
gr = (1 + sqrt(5))/2
ax, ay, az = 0, 0, 0
rand = False
save_to_file = True 
read_from_file = False 
if read_from_file: 
    save_to_file = False

window = Window(visible=True, width=width, height=height,
                resizable=True, caption='lab5')
# window.projection = pyglet.window.Projection3D()
glClearColor(0.1, 0.1, 0.1, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glPointSize(5)
glEnable(GL_POINT_SMOOTH)
glEnable(GL_DEPTH_TEST)

for i in range(12):
    for j in range(5):
        #if rand:
        glColor3d(random.random(),random.random(),random.random())

def get_dod():
    v1 = [
        [1.,1.,1.],
        [1.,1.,-1.],
        [1.,-1.,-1.],
        [1.,-1.,1.],
        [-1.,1.,1.],
        [-1.,-1.,1.],
        [-1.,1.,-1.],
        [-1.,-1.,-1.],
        [gr,1./gr,0.],
        [gr,-1./gr,0.],
        [-gr,-1./gr,0.],
        [-gr,1./gr,0.],
        [0.,gr,1./gr],
        [0.,gr,-1./gr],
        [0.,-gr,-1./gr],
        [0.,-gr,1./gr],
        [1./gr,0.,gr],
        [1./gr,0.,-gr],
        [-1./gr,0.,-gr],
        [-1./gr,0.,gr]
    ]

    g1 = [
        [2,9,3,15,14],
        [3,9,8,0,16],
        [16,0,12,4,19],
        [16,19,5,15,3],
        [15,5,10,7,14],
        [14,7,18,17,2],
        [2,17,1,8,9],
        [8,1,13,12,0],
        [13,1,17,18,6],
        [10,11,6,18,7],
        [11,10,5,19,4],
        [6,11,4,12,13]
    ]
    return v1, g1


if read_from_file:
    print('Загрузка данных из двоичных файлов')
    def load_data(file):
        with open(file, 'rb') as r_b:
            data = np.fromfile(r_b)
            data.reshape(1, 2)
        return data
    vrts = load_data('D://python//fileNew.bin')

else:
    vrts = get_dod()
if save_to_file:
    print('Запись данных в двоичные файлы')
    def write_to_bin(file, data):
        fn = open(file, 'wb')
        fn.write(np.array(data))
        fn.close()
    write_to_bin('D://python//fileNew.bin', vrts)

glEnable(GL_CULL_FACE)
glCullFace(GL_BACK) 
@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-wx, wx, -wy, wy, -20, 20)
    glRotatef(ax, 1, 0, 0)
    glRotatef(ay, 0, 1, 0)
    glRotatef(az, 0, 0, 1)
    glColor3d(0.5,1,0.5)
    v, g = vrts[0], vrts[1]
    for i in range(12):
        glBegin(GL_POLYGON)
        for j in range(5):
            if rand:
                glColor3d(random.random(),random.random(),random.random())
            nv = g[i][j]
            glVertex3d(v[nv][0],v[nv][1],v[nv][2])

        glEnd()

        
@window.event
def on_key_press(symbol, modifiers):
    global ax, ay, az, rand
    if symbol == key._1:
        glPolygonMode(GL_FRONT, GL_LINE)
    elif symbol == key._2:
        glPolygonMode(GL_FRONT, GL_POINT)
    elif symbol == key._3:
        glPolygonMode(GL_FRONT, GL_FILL)
        gl.glShadeModel(gl.GL_FLAT)
        rand = True
    elif symbol == key._4:
        glPolygonMode(GL_FRONT, GL_FILL)
        gl.glShadeModel(gl.GL_SMOOTH)
        rand = True
    elif symbol == key._5:
        ax += 5
    elif symbol == key._6:
        ay += 5
    elif symbol == key._7:
        az += 5
    elif symbol == key._8:
        ax, ay, az = 0, 0, 0
app.run()


# In[ ]:




