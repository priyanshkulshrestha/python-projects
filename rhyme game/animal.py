import os 
import pygame
import game_config as gc
import random 
from pygame import image, transform
animals_count = dict((a,0) for a in gc.asset_files)

def available_animals():
    return[a for a, c in animals_count.items() if c<2]

class animal:
    def __init__ (self, index):
        self.index = index 
        self.row = index // gc.num_tiles_side
        self.col = index % gc.num_tiles_side
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1
        self.image_path = os.path.join(gc.assest_dir, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.img_size - 2*gc.margin, gc.img_size - 2*gc.margin))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip =False
