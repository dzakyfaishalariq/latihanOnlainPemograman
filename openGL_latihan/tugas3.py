from math import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import os
os.system('cls')

# gambar garis


def garis(x, y, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()


def lingkaran(x_pos, y_pos, radius, sides):
    glBegin(GL_POLYGON)
    pi = 3.14
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides) + x_pos
        sine = radius * sin(i*2*pi/sides) + y_pos
        glVertex2f(cosine, sine)
    glEnd()
# buat iteratifnya


def iteratif():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iteratif()
    # warna garis kuning
    glColor3f(1.0, 0.3, 2.0)
    # buat kotak
    garis(200, 100, 100, 100)
    garis(100, 100, 100, 200)
    garis(100, 200, 200, 200)
    garis(200, 200, 200, 100)
    # buat pagar di openGL
    for i in range(600):
        lingkaran(i, 20, 10, 100)
    a = 0
    while a < 500:
        for i in range(50):
            lingkaran(a, i, 10, 50)
        a += 30
    # buat jalan
    garis(100, 100, 50, 50)
    garis(50, 50, 140, 50)
    garis(140, 50, 200, 100)
    # buat jendela
    garis(130, 130, 130, 160)
    garis(130, 130, 160, 130)
    garis(160, 130, 160, 160)
    garis(160, 160, 130, 160)
    garis(145, 145, 145, 160)
    garis(145, 145, 160, 145)
    garis(145, 145, 130, 145)
    garis(145, 145, 145, 130)
    # buat atap
    garis(100, 200, 150, 300)
    garis(150, 300, 200, 200)
    garis(150, 300, 400, 300)
    garis(400, 300, 450, 200)
    garis(450, 200, 350, 200)
    garis(350, 200, 400, 300)
    garis(350, 200, 200, 200)
    # buat badan
    garis(350, 200, 350, 100)
    garis(450, 200, 450, 100)
    garis(450, 100, 350, 100)
    garis(350, 100, 200, 100)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Tugas 2")
    glutDisplayFunc(screen)
    glutIdleFunc(screen)
    glutMainLoop()


main()
