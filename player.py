import pygame
from projectile import Projectile

#creer une première classe qui va représenter notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 560

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # desiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 12, self.rect.y + 9, self.max_health, 8])
        pygame.draw.rect(surface, (48, 236, 15), [self.rect.x + 12, self.rect.y + 9, self.health, 8])

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        #jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur n'esp pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity