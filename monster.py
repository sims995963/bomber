import pygame
import random
import animation

#creer une clase qui va gérer la notion de monstre sur notre jeu


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.images = [
            pygame.image.load('assets/bang.png').convert_alpha(),
            # Ajoutez d'autres images d'explosion si nécessaire
        ]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=position)
        self.animation_time = 100  # Temps entre chaque image de l'animation
        self.current_time = pygame.time.get_ticks()

    def update(self):
        # Animation de l'explosion
        if pygame.time.get_ticks() - self.current_time >= self.animation_time:
            self.index += 1
            if self.index >= len(self.images):
                self.kill()

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.name = Monster
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1400 + random.randint(0, 300)
        self.rect.y = 490 - offset
        self.loot_amount = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(2, 5)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount
        if self.health <= 0:
            # Créer une explosion
            explosion = Explosion(self.rect.center)
            self.game.all_explosions.add(explosion)


                            #vérifier si son nouveau nombre de point de point de vie est égale à 0 au moin
        if self.health <= 0:

            #reapparaitre comme un nouveau monstre
            self.rect.x = 1400 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            #ajouter le nombre de point
            self.game.add_score(self.loot_amount)

            #si la barre d'evenement est chargé au max
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)
                # appel de la Méthode pour déclancher la plus de comet
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):

        #desiner notre bar de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 80, self.rect.y + 9, self.max_health, 6])
        pygame.draw.rect(surface, (48, 236, 15), [self.rect.x + 80, self.rect.y + 9, self.health, 6])



    def forward(self):
        #le déplacement ne ce fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity

        #si le monstre est en collision avec le joueur
        else:
            #infliger des dégâts (aux joueurs)
            self.game.player.damage(self.attack)


#definir une class pour le monstre 1
class ennemi1(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi1", (255,255))
        self.set_speed(5)
        self.set_loot_amount(20)


#definir une seconde classe de monstre
class ennemi2(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi2", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.set_speed(3)
        self.set_loot_amount(10)

class Boss(Monster):
    def __init__(self, game):
        super().__init__(game, "boss", (400,400), 150)
        self.health = 250
        self.max_health = 250
        self.attack = 3
        self.set_speed(2)
        self.set_loot_amount(40)


class guard(Monster):
    def __init__(self, game):
        super().__init__(game, "guard", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 2
        self.set_speed(3)
        self.set_loot_amount(30)



class ennemi4(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi4", (400,400), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 2
        self.set_speed(2)
        self.set_loot_amount(50)


class ennemi3(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi3", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.set_speed(6)
        self.set_loot_amount(20)

class ennemi8(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi8", (400,400), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 4
        self.set_speed(2)
        self.set_loot_amount(80)

class ennemi7(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi7", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 6
        self.set_speed(5)
        self.set_loot_amount(50)

class ennemi11(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi11", (400,400), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 10
        self.set_speed(4)
        self.set_loot_amount(150)

class ennemi10(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi10", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 8
        self.set_speed(5)
        self.set_loot_amount(80)

class ennemi12(Monster):
    def __init__(self, game):
        super().__init__(game, "ennemi12", (400,400), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 6
        self.set_speed(4)
        self.set_loot_amount(100)


class bomb(Monster):
    def __init__(self, game):
        super().__init__(game, "bomb", (255,255))
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.set_speed(9)
        self.set_loot_amount(80)

