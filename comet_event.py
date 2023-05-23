import pygame
from comet import Comet

#creer une classe pour gérer cette évènement
class CometFallEvent:

    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        #definir un groupe de sprite pour nos monstre aériens
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed /100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #boucle pour les valeur entre 1 et 30
        for i in range(1, 15):
            #apparaitre notre bombe aérienne
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        #la jauge d'evenement est complètement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print('bomb bomb bomb')
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement

    def update_bar(self,surface):

        #ajouter du pourcentage à la bar
        self.add_percent()

        #barre noir(en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() -10, #l'axe des y
            surface.get_width(), #longueur de la fenetre
            10 #epaisseur de la barre

        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187,11,11), [
            0,  # l'axe des x
            surface.get_height() -10,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10])  # epaisseur de la barre