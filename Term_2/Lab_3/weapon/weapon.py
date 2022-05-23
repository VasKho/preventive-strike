import pygame
import yaml
import os
from math import sin, cos, radians
from abc import ABC, abstractclassmethod
import time


class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage, bullet_image, velocity, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath(bullet_image)).convert()
        self.image = pygame.transform.scale(self.image, (0.01*pygame.display.Info().current_w, 0.01*pygame.display.Info().current_h))
        self.image.set_colorkey((255, 255, 255))
        self.velocity = velocity
        self.angle = angle
        self.rect = self.image.get_rect()
        self.damage = damage
    

    def update(self):
        if self.rect.x in range(0, pygame.display.Info().current_w):
            self.rect.x += self.velocity * sin(radians(self.angle))
        else:
            self.kill()
        if self.rect.y in range(0, pygame.display.Info().current_h):
            self.rect.y += self.velocity * cos(radians(self.angle))
        else:
            self.kill()
    pass


class Weapon(ABC):
    def __init__(self, reload_time) -> None:
        self.reload_time = reload_time


    @abstractclassmethod
    def fire(self, owner):
        pass


class Pistol(Weapon):
    def __init__(self) -> None:
        with open("weapon/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            print(conf)
            super().__init__(conf['Pistol']['reload_time'])
            self.damage = conf['Pistol']['damage']
            self.bullet_image_path = conf['Pistol']['bullet_image_path']
            self.bullet_velocity = conf['Pistol']['bullet_velocity']
        self.reloading = False
        self.last_reload_time = time.time()


    def fire(self, owner):
        if not self.reloading:
            self.bullet = Bullet(self.damage, self.bullet_image_path, self.bullet_velocity, owner.angle)
            self.bullet.rect = self.bullet.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
            self.last_reload_time = time.time()
            return self.bullet
    pass
