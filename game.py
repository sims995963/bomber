import pygame
import random
from sounds import SoundManager
from player import Player
from monster import ennemi1, ennemi2, Boss, ennemi10, ennemi11, guard, ennemi3, ennemi4, ennemi7, ennemi8, \
    bomb, ennemi12
from comet_event import CometFallEvent


#creer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #definir si notre à commencé
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)

        self.all_explosions = pygame.sprite.Group()


        #group de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.score_0 = False

        self.score_changed = False

        self.score_2 = False

        self.score_3 = False

        self.score_4 = False

        self.score_5 = False

        self.score_6 = False

        self.score_7 = False

        self.score_8 = False

        self.score_9 = False

        self.score_10 = False

        self.score_11 = False

        self.score_12 = False

        self.score_13 = False

        #gerer le son
        self.sound_manager = SoundManager()

        #mettre le score à 0
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 40)
        self.score = 0
        self.pressed ={}




    def start(self):
        self.is_playing = True
        self.spawn_monster(ennemi1)
        self.spawn_monster(ennemi1)
        self.spawn_monster(ennemi2)
        self.spawn_monster(ennemi2)


    def add_score(self, points=10):
        self.score += points



    def game_over(self):
        #remettre le jeu à 0, monstre vie etc...
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20,20))

        self.all_explosions.update()
        self.all_explosions.draw(screen)

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)


        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)




        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #recuperer les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()



        # appliquer les images des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon monstre
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comettes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1400:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 5:
            self.player.move_left()

            #______________________________________________________________________

            # Vérifier si le joueur a atteint 200 points
        if self.score >= 200 and not self.score_changed:
            # Supprimer les monstres existants
            self.all_monsters.empty()


            # Faire apparaître de nouveaux monstres
            self.spawn_monster(Boss)
            self.spawn_monster(guard)
            self.spawn_monster(guard)
            self.spawn_monster(guard)
            self.spawn_monster(guard)


            # Définir score_changed sur True
            self.score_changed = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)



            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_____________________________________________________________________________

        if self.score >= 700 and not self.score_2:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi4)
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi3)

            # Définir score_changed sur True
            self.score_2 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)

            #______________________________________________________________________
        if self.score >= 1100 and not self.score_3:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi8)
            self.spawn_monster(ennemi8)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi7)

            # Définir score_changed sur True
            self.score_3 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_____________________________________________________________________
        if self.score >= 1500 and not self.score_4:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(bomb)
            self.spawn_monster(bomb)
            self.spawn_monster(bomb)
            self.spawn_monster(ennemi12)
            self.spawn_monster(ennemi12)

            # Définir score_changed sur True
            self.score_4 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_____________________________________________________________________________________
        if self.score >= 2000 and not self.score_5:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi11)
            self.spawn_monster(ennemi11)
            self.spawn_monster(ennemi10)
            self.spawn_monster(ennemi10)
            self.spawn_monster(ennemi10)

            # Définir score_changed sur True
            self.score_5 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #___________________________________________________________________________

        if self.score >= 2500 and not self.score_6:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(Boss)
            self.spawn_monster(Boss)
            self.spawn_monster(guard)
            self.spawn_monster(guard)
            self.spawn_monster(guard)
            self.spawn_monster(guard)

            # Définir score_changed sur True
            self.score_6 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #___________________________________________________________________________

        if self.score >= 3000 and not self.score_7:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi4)
            self.spawn_monster(ennemi4)

            # Définir score_changed sur True
            self.score_7 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_________________________________________________________________________

        if self.score >= 3500 and not self.score_8:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi8)
            self.spawn_monster(ennemi8)

            # Définir score_changed sur True
            self.score_8 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #________________________________________________________________________

        if self.score >= 4000 and not self.score_9:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi12)
            self.spawn_monster(ennemi12)
            self.spawn_monster(bomb)
            self.spawn_monster(bomb)
            self.spawn_monster(bomb)
            self.spawn_monster(bomb)

            # Définir score_changed sur True
            self.score_9 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_______________________________________________________________

        if self.score >= 4500 and not self.score_10:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi11)
            self.spawn_monster(ennemi11)
            self.spawn_monster(ennemi10)
            self.spawn_monster(ennemi10)
            self.spawn_monster(ennemi10)
            self.spawn_monster(ennemi10)

            # Définir score_changed sur True
            self.score_10 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #_____________________________________________________________________

        if self.score >= 5000 and not self.score_11:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi10)
            self.spawn_monster(bomb)
            self.spawn_monster(ennemi1)
            self.spawn_monster(ennemi2)

            # Définir score_changed sur True
            self.score_11 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)
            #______________________________________________________

        if self.score >= 5000 and not self.score_12:
            # Supprimer les monstres existants
            self.all_monsters.empty()

            # Faire apparaître de nouveaux monstres
            self.spawn_monster(ennemi3)
            self.spawn_monster(ennemi7)
            self.spawn_monster(ennemi10)
            self.spawn_monster(bomb)
            self.spawn_monster(ennemi1)
            self.spawn_monster(ennemi2)

            # Définir score_changed sur True
            self.score_12 = True

            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)
                #__________________________________________________
            if self.score >= 5500 and not self.score_13:
                # Supprimer les monstres existants
                self.all_monsters.empty()

                # Faire apparaître de nouveaux monstres
                self.spawn_monster(ennemi4)
                self.spawn_monster(ennemi8)
                self.spawn_monster(ennemi11)
                self.spawn_monster(ennemi12)
                self.spawn_monster(Boss)

                # Définir score_changed sur True
                self.score_13 = True

                for monster in self.all_monsters:
                    monster.forward()
                    monster.update_health_bar(screen)

            # Afficher les autres éléments
            self.all_explosions.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            self.player.update_health_bar(screen)
            self.comet_event.update_bar(screen)
            self.player.all_projectiles.draw(screen)
            self.all_monsters.draw(screen)
            self.comet_event.all_comets.draw(screen)





    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))