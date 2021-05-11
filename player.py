from prototipo.configs import *
import pygame as pg
import os
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__size = (32, 48)
        self.__pos = vec(WIDTH / 4, HEIGHT / 2)  # deve ser definido pelo level
        self.__vel = vec(0, 0)  # velocidade
        self.__acc = vec(0, 0)  # aceleracao
        self.__std_acc = 0.5  # aceleracao padrao
        self.__jump_acc = -14  # aceleracao pulo
        self.__key = False
        self.__image = pg.Surface(self.__size)
        self.__rect = self.__image.get_rect()

    @ property
    def image(self):
        return self.__image

    @ property
    def rect(self):
        return self.__rect

    @ property
    def size(self):
        return self.__size

    @ size.setter
    def size(self, n):
        self.__size = n

    @ property
    def pos(self):
        return self.__pos

    @ pos.setter
    def pos(self, n):
        self.__pos = n

    @ property
    def vel(self):
        return self.__vel

    @ vel.setter
    def vel(self, n):
        self.__vel = n

    @ property
    def acc(self):
        return self.__acc

    @ acc.setter
    def acc(self, n):
        self.__acc = n

    @ property
    def std_acc(self):
        return self.__std_acc

    @ property
    def jump_acc(self):
        return self.__jump_acc

    @ property
    def key(self):
        return self.__key

    @ key.setter
    def key(self, n):
        self.__key = n