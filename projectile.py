import pygame

#definir la classe qui va gérer le projectile de notre jeux
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 20
        self.player = player
        self.image = pygame.image.load('assets/projectile6.png')
        self.image = pygame.transform.scale(self.image,(30,20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 140
        self.rect.y = player.rect.y + 70


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity


        #vérifier si notre projectile rentre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des dégat
            monster.damage(self.player.attack)

        #vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x >1500:
            # supprimer le projectile
            self.remove()

