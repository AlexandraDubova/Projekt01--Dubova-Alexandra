import pygame
import random
import os

from settings import (
    fps,
    bone_spawn_time,
    window_rows,
    window_cols,
    window_width,
    window_height,
    section_width,
    section_height,
    slope
)

from level import levels, start_y, row6_y
from player import Player
from objects import Bone, Ball, Bridge, Ladder
from assets import (
    princess1_img, princess2_img,
    dog_basket_img, dog_basket2_img,
    bowl_img,
    en1_img, en2_img)
from enemy import draw_enemy


os.environ['SDL_VIDEO_CENTERED'] = '1' 

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Kitty Kong!")

time = pygame.time.Clock()

"""pygame.init()

info = pygame.display.Info() 

screen_width, screen_height = info.current_w, info.current_h
window_width= screen_width - 800
window_height = screen_height - 150
screen = pygame.display.set_mode((window_height, window_width))
"""

bone_count = bone_spawn_time
bone_time = 360

ball_trigger = False
active_level = 0

first_bone_taken = False

basket_flipped = False
basket_flip_start = 0
basket_flip_duration = 0

enemy_rect = None

def draw_screen():
    platforms = []
    climbers = []
    ladder_objs = []
    bridge_objs = []

    ladders = levels[active_level]['ladders']
    bridges = levels[active_level]['bridges']

    for bridge in bridges:
        bridge_objs.append(Bridge(*bridge, screen))
        platforms.append(bridge_objs[-1].top)
    
    for ladder in ladders:
        ladder_objs.append(Ladder(*ladder, screen))
        if ladder[2] >= 3:
            climbers.append(ladder_objs[-1].body)
    return platforms, climbers

def draw_extras():
    global enemy_rect

    basket = draw_basket()
    draw_bowl()
    enemy_rect = draw_enemy(screen, section_width, section_height, row6_y)
    
    if bone_count < bone_spawn_time/2:
        screen.blit(princess1_img, (10* section_width, row6_y -5.4 * section_height))
    else:
        screen.blit(princess2_img, (10* section_width, row6_y -5.4 * section_height))
    return basket

def draw_basket():
    global basket_flipped, basket_flip_start
    elapsed_time_since_flip = (pygame.time.get_ticks() - basket_flip_start)

    basket_rect = pygame.Rect(1 * section_width, start_y - 2 * section_height,
                              section_width * 1, section_height * 1)
    
    hitbox = pygame.Rect(
    basket_rect.x - section_width - 4,
    basket_rect.y - 4,
    section_width * 3 + 8,
    section_height *  2+ 8
)
     # DEBUG
    pygame.draw.rect(screen, "red", hitbox, 2)


    if basket_flipped:
        screen.blit(dog_basket2_img, basket_rect.topleft)
        # pokud chceme, aby se po době obrátil zpět, kontrolujeme duration:
        if basket_flip_duration > 0 and elapsed_time_since_flip > basket_flip_duration:
            basket_flipped = False
    else:
        screen.blit(dog_basket_img, basket_rect.topleft)

    return hitbox

def draw_bowl():
    screen.blit(bowl_img, (int(1.2*section_width), int(row6_y -2.8 * section_height)))


timer = pygame.time.Clock()

start_time = pygame.time.get_ticks()

bones = pygame.sprite.Group()    
balls = pygame.sprite.Group()

bones.add(Bone(5 * section_width, 3 * section_height))  # TEST

player = Player(200, window_height - 130)

run = True
while run:
    now = pygame.time.get_ticks()

    timer.tick(fps)
    screen.fill('pink')
   

    plats, lads = draw_screen()
    dog_basket = draw_extras()   

    climb, down = player.can_climb(lads)

    if bone_count < bone_spawn_time:
        bone_count += 1
    else:
        bone_count = random.randint(0, 120)
        bone_time = bone_count - bone_spawn_time

        bone = Bone(250, 200)

        if not first_bone_taken:
            bone.is_first = True
            first_bone_taken = True
            bone.falling = True
            bone.y_change = 6
            bone.check_lad = True

        bones.add(bone)

    if bone.is_first and not basket_flipped:
        basket_flipped = True
        basket_flip_start = pygame.time.get_ticks()

        for _ in range(3):
            ball = Ball(
                dog_basket.centerx,
                dog_basket.top
            )
            balls.add(ball)


    basket_hit = False

    for bone in list(bones):   
        bone.check_fall()
        result = bone.update(plats,lads,dog_basket, enemy_rect, window_height)
    
        if result == "basket":
            basket_hit = True
        bone.draw(screen)
    
    if basket_hit and not basket_flipped:
        basket_flipped = True
        basket_flip_start = pygame.time.get_ticks()

        for _ in range(3):
            ball = Ball(
            dog_basket.centerx,
            dog_basket.top
        )
        balls.add(ball)



    MAX_BALLS = 6
    if ball_trigger:
        if len(balls) < MAX_BALLS:
            ball = Ball(5 * section_width, window_height - 4 * section_height)
            balls.add(ball)
            print("DEBUG: spawned Ball — total balls:", len(balls))
        else:
            print("DEBUG: spawn skipped (too many balls)")
        ball_trigger = False

    for b in list(balls):
        b.check_climb()
        b.update()
        screen.blit(b.image, b.rect.topleft)

    player.update(plats)
    player.draw(screen)
    

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not player.climbing:
                    player.x_change = 1
                    player.dir = 1
                if event.key == pygame.K_LEFT and not player.climbing:
                    player.x_change = -1
                    player.dir = -1
                if event.key == pygame.K_SPACE and player.landed:
                    player.landed = False
                    player.y_change = -6
                if event.key == pygame.K_UP:
                    if climb:
                        player.y_change = -2
                        player.x_change = 0
                        player.climbing = True
                if event.key == pygame.K_DOWN:
                    if down:
                        player.y_change = 2
                        player.x_change = 0
                        player.climbing = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.x_change = 0
                if event.key == pygame.K_LEFT:
                    player.x_change = 0
                if event.key == pygame.K_UP:
                    if climb:
                        player.y_change = 0
                    if player.climbing and player.landed:
                        player.climbing = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if down:
                        player.y_change = 0
                    if player.climbing and player.landed:
                        player.climbing = False
    pygame.display.flip()

pygame.quit()






