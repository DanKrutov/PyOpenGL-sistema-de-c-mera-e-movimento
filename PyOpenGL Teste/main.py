import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from cubemdl import *
from slamdl import *


def main():
    pygame.init()
    display = (1024, 768)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('OPENGL')
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.5, -5) # posicao da camera (X, Y, Z)
    def_dir = "F"

    while True:
        pos = glTranslatef
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if def_dir == "F":
                        glTranslatef(0, 0, -1)
                    elif def_dir == "T":
                        glTranslatef(0, 0, 1)
                    elif def_dir == "E":
                        glTranslatef(-1, 0, 0)
                    elif def_dir == "D":
                        glTranslatef(1, 0, 0)

                if event.key == K_UP:
                    if def_dir == "F":
                        glTranslatef(0, 0, 1)
                    elif def_dir == "T":
                        glTranslatef(0, 0, -1)
                    elif def_dir == "E":
                        glTranslatef(1, 0, 0)
                    elif def_dir == "D":
                        glTranslatef(-1, 0, 0)

                if event.key == K_LEFT:
                    if def_dir == "F":
                        glTranslatef(1, 0, 0)
                    if def_dir == "T":
                        glTranslatef(-1, 0, 0)
                    if def_dir == "E":
                        glTranslatef(0, 0, -1)
                    if def_dir == "D":
                        glTranslatef(0, 0, 1)

                if event.key == K_RIGHT:
                    if def_dir == "F":
                        glTranslatef(-1, 0, 0)
                    if def_dir == "T":
                        glTranslatef(1, 0, 0)
                    if def_dir == "E":
                        glTranslatef(0, 0, 1)
                    if def_dir == "D":
                        glTranslatef(0, 0, -1)

                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == K_KP6:
                    if def_dir == "F":
                        def_dir = "D"
                    elif def_dir == "D":
                        def_dir = "T"
                    elif def_dir == "T":
                        def_dir = "E"
                    elif def_dir == "E":
                        def_dir = "F"

                    glRotatef(90, 0, 1, 0)
                    #glTranslatef(-3, 0, -3)
                    glTranslatef(-3, 0, -3)
                if event.key == K_KP4:
                    if def_dir == "F":
                        def_dir = "E"
                    elif def_dir == "E":
                        def_dir = "T"
                    elif def_dir == "T":
                        def_dir = "D"
                    elif def_dir == "D":
                        def_dir = "F"

                    glRotatef(-90, 0, 1, 0)
                    #glTranslatef(3, 0, -3)
                    glTranslatef(3, 0, -3)


        #glRotatef(0, 0, 1, 0)  # angulo e velocidade de rotação (velocidade, y, x, ?)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)  # intervalo entre frames/whiles

main()
