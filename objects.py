from pygame.sprite import Sprite
from pygame import Surface, image, transform
from pygame import Color
from pygame import Rect


class MovingPlatform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.last_state = 'up'
        self.state = 'up'
        self.vel_y = 0
        self.vel_x = 0
        self.moved = 0
        self.original_y = y
        self.image = Surface((160, 20))
        self.image.fill(Color('Orange'))
        self.rect = Rect(x, y, 160, 20)

    def update(self):
        if self.rect.y == 40:
            self.rect.y = 520
            self.moved = 0
        self.rect.y -= 1
        self.moved += 1


class CoinBox(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = image.load('sprites/coin1.png').convert()
        self.image = transform.scale(self.image, (40, 40))
        self.rect = Rect(x, y, 40, 40)

    def update(self, state):
        if state == 0:
            self.image = image.load('sprites/coin2.png').convert()
            self.image = transform.scale(self.image, (40, 40))


class GoalPole(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = image.load('sprites/flag.png').convert()
        self.image = transform.scale(self.image, (50, 300))
        self.rect = Rect(x - 10, y, 20, 290)


class Decoration(Sprite):
    def __init__(self, x, y, sprite):
        Sprite.__init__(self)
        self.image = image.load(sprite).convert()
        a = self.image.get_rect()
        self.image = transform.scale(self.image, (a[2] * 2, a[3] * 2))
        self.rect = Rect(x, y + 10, 0, 0)


class MushroomBox(CoinBox):
    def __init__(self, x, y):
        CoinBox.__init__(self, x, y)
