import pygame
from pygame import display, event, image
import game_config as gc
from animal import animal
from time import sleep
def find_index(x,y):
    row = y // gc.img_size
    col = x // gc.img_size
    index = row * gc.num_tiles_side + col
    return index
pygame.init()
game_window = pygame.display.set_mode((512, 512))
pygame.display.set_caption("rhyme_python_animal_game")
match = image.load("other\matched.png")
# game_window.blit(match, [0,0])
# display.flip()
run = True
tiles = [animal(i) for i in range(0, gc.num_tiles_total)]

current_image = []

while run:
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            index = find_index(mousex,mousey)
            if index not in current_image:
                current_image.append(index)
            if len(current_image) > 2:
                current_image = current_image[1:]
    game_window.fill((255,255,255))
    total_skiped = 0
    for _, tile in enumerate(tiles):
        image_i = tile.image if tile.index in current_image else tile.box
        if not tile.skip:
            game_window.blit(image_i,(tile.col * gc.img_size + gc.margin,tile.row * gc.img_size + gc.margin))
        else:
            total_skiped += 1
    # display.flip()
    if len(current_image) == 2:
        idx1, idx2 = current_image
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True 
            tiles[idx2].skip = True 
            sleep(0.4)
            game_window.blit(match, (0,0))
            display.flip()
            sleep(0.4)
            current_image =[]
    if total_skiped == len(tiles):
        run = False
    display.flip()
print("end")
