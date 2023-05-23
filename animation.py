import pygame


class AnimateSprite(pygame.sprite.Sprite):

    #definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(150,150)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
#definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    images = []

    path = f"assets/{sprite_name}/{sprite_name}"
    for num in range (1,1):
        image_path = path + '.png'
        images.append(pygame.image.load(image_path))

        #revoyer le contenu de la liste d'image
        return images

#definir un dictionnaire qui va contenir les imafes chargées de chaque images
animations ={
    'ennemi1': load_animation_images('ennemi1'),
    'player' : load_animation_images('player1'),
    'alien': load_animation_images('ennemi2'),
    'Boss': load_animation_images('boss'),
    'Explosion': load_animation_images('bang')
}