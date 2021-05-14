from configs import *
from character import Character

class Enemy(Character):
    def __init__(self, lista_):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        self.__health = 100
        self.__pos = vec(0,0)
        self.__std_acc = 0.5
        self.__vel = vec(0, 0)
        self.__acc = vec(0, 0)
        self.__std_acc = 0.1
        self.__jump_acc = -4
        self.__collisions = {"bottom": False,
                             "top": False, "right": False, "left": False}
    

        self.__lista = lista_
        self.__sprites = []

        self.load_sprite()

        self.__current_sprite = 4

        self.__image = self.__sprites[self.__current_sprite]
        self.__rect = self.__image.get_rect()
        self.__rect.midbottom = self.__pos

        self.animation("idle")

    def load_sprite(self):
        for image in range(len(self.__lista)):
            self.__sprites.append(pg.image.load(data + self.__lista[image]))

    def animation(self, command):
        if command == "left": #and not self.colisions['left']:
            self.__current_sprite -= 0.3
            if self.__current_sprite <= 0:
                self.__current_sprite = 3
        elif command == "right": #and not self.colisions['right']:
            self.__current_sprite += 0.3
            if self.__current_sprite >= len(self.__sprites):
                self.__current_sprite = 5
        else:
            self__current_sprite = 4

        self.__image = self.__sprites[int(self.__current_sprite)]

    def vai_e_volta(self):
        self.vel.x -= 5
        pg.time.delay(5000)
        self.vel.y += 5

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

    @ property
    def health(self):
        return self.__health

    @ health.setter
    def health(self, n):
        self.__health = n

    @ property
    def collisions(self):
        return self.__collisions

    @ collisions.setter
    def collisions(self, n):
        self.__collisions = n

    @ property
    def current_sprite(self):
        return self.__current_sprite