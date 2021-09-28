from OpenGL.GL import *

# vértices / pontos do cubo
vertices = (
    #Quadrado
    (1, -1, -1), # B Inferior Direito - 0
    (1, 1, -1), # B Superior Direito - 1
    (-1, 1, -1), # B Superior Esquerdo - 2
    (-1, -1, -1), # B Inferior Esquerdo - 3
    (1, -1, 1), # F Inferior Direito - 4
    (1, 1, 1), # F Superior Direito - 5
    (-1, -1, 1), # F Inferior Esquerdo - 6
    (-1, 1, 1), # F Superior Esquerdo - 7

    #Telha
    (0, 1.5, -1), # trás - 8
    (0, 1.5, 1), # frente - 9

    # porta
    (-0.3, 0, 1), # sup esquerda - 10
    (0.3, 0, 1), # sup direita - 11
    (-0.3, -1, 1), # inf esquerda - 12
    (0.3, -1, 1), # inf direita - 13

    #casa2
    (1, -1, 5), # F Inferior Direito - 14
    (1, 1, 5), # F Superior Direito - 15
    (-1, 1, 5), # F Superior Esquerdo - 16
    (-1, -1, 5), # F Inferior Esquerdo - 17
    (1, -1, 7), # B Inferior Direito - 18
    (1, 1, 7), # B Superior Direito - 19
    (-1, -1, 7), # B Inferior Esquerdo - 20
    (-1, 1, 7), # B Superior Esquerdo - 21

    #porta2
    (-0.3, 0, 5), # sup esquerda - 22
    (0.3, 0, 5), # sup direita - 23
    (-0.3, -1, 5), # inf esquerda - 24
    (0.3, -1, 5), # inf direita - 25

    #telha2
    (0, 1.5, 6), # ponta telha - 26

    )

# linhas que conectam cada vértice
edges = (

    #telha piramide
    (26, 15),
    (26, 16),
    (26, 19),
    (26, 21),

    # quadrado
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),

    # telha
    (8, 9),
    (9, 7),
    (9, 5),
    (8, 2),
    (8, 1),

    # porta
    (10, 11),
    (10, 12),
    (11, 13),

    # porta 2
    (22, 23),
    (22, 24),
    (23, 25),

    # rota
    (12, 24),
    (13, 25),

    # casa 2
    (14, 15),
    (14, 17),
    (14, 18),
    (16, 15),
    (16, 17),
    (16, 21),
    (20, 17),
    (20, 18),
    (20, 21),
    (19, 15),
    (19, 18),
    (19, 21),
    )



def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()