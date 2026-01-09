import pygame
from assets import en1_img, en2_img

def draw_enemy(screen, section_width, section_height, row6_y):
    enemy_x = int(3.5 * section_width)
    enemy_y = int(row6_y - 4 * section_height)

    t = pygame.time.get_ticks() // 500
    img = en1_img if t % 2 == 0 else en2_img

    screen.blit(img, (enemy_x, enemy_y))

    # vracíme rect, aby ho main mohl použít
    return pygame.Rect(
        enemy_x,
        enemy_y,
        img.get_width(),
        img.get_height()
    )
