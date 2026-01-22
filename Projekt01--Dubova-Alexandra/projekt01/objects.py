
import pygame
import random
from settings import section_width, section_height, window_height
from assets import bone_img, ball_img, ball2_img
from level import (
    row1_top, row2_top, row3_top,
    row4_top, row5_top, row6_y
)

screen = None
plats = []
lads = []
enemy_rect = None
dog_basket = None
enemy_face_dir = 1

class Bridge:
    def __init__(self, x_pos, y_pos, length, screen):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.top = self.draw(screen)

    def draw(self, screen):
        line_width = 7
        platform_color = (225, 51, 129)

        for i in range(self.length):
            bot = self.y_pos + section_height
            left = self.x_pos + section_width * i
            mid = left + section_width * 0.5
            right = left + section_width
            top = self.y_pos

            pygame.draw.line(screen, platform_color, (left, top), (right, top), line_width)
            pygame.draw.line(screen, platform_color, (left, bot), (right, bot), line_width)
            pygame.draw.line(screen, platform_color, (left, bot), (mid, top), line_width)
            pygame.draw.line(screen, platform_color, (mid, top), (right, bot), line_width)

        return pygame.Rect(self.x_pos, self.y_pos, self.length * section_width, 8)
                       
    
class Ladder:
    def __init__(self, x_pos, y_pos, length, screen):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.body = self.draw(screen)

    def draw(self, screen):
        line_width = 3
        lad_color = 'dark grey'
        lad_height = 0.6

        for i in range(self.length):
            top = self.y_pos + lad_height * section_height * i
            bot = top + lad_height * section_height
            mid = top + (lad_height / 2) * section_height
            left = self.x_pos
            right = left + section_width

            pygame.draw.line(screen, lad_color, (left, top), (left, bot), line_width)
            pygame.draw.line(screen, lad_color, (right, top), (right, bot), line_width)
            pygame.draw.line(screen, lad_color, (left, mid), (right, mid), line_width)

        return pygame.Rect(
            self.x_pos,
            self.y_pos - section_height,
            section_width,
            lad_height * self.length * section_height + section_height
        )

 
class Bone(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bone_img.convert_alpha()
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.y_change = 0
        self.x_change = 1
        self.pos = 0
        self.count = 0
        self.falling = False
        self.check_lad = False
       
        self.taken_by_enemy = False
        self.take_time = 0
        self.hold_duration = 300   
        self.taken_dir = 1

        # označení první bonei
        self.is_first = False

        self.bottom = self.rect

        self.basket_triggered = False

    def update(self, plats, lads, dog_basket, enemy_rect, screen_height):



  
        if self.taken_by_enemy:

            if enemy_rect is not None:
                hold_x = enemy_rect.centerx + (20 * self.taken_dir)  # offset, aby bone nebyla přesně ve středu
                hold_y = enemy_rect.centery - 10  # mírně nad enemy
                self.rect.center = (hold_x, hold_y)

            if pygame.time.get_ticks() - self.take_time > self.hold_duration:
                self.taken_by_enemy = False
            
                self.x_change = 5 * self.taken_dir
                self.y_change = -5
                self.falling = False
                self.check_lad = False

            self.bottom = pygame.rect.Rect((self.rect[0], self.rect.bottom), (self.rect[2], 3))
            return False
        
        if self.y_change < 8 and not self.falling:
            self.y_change +=2
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0
                self.falling = False

        if not self.falling:
            if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top > self.rect.bottom >= row2_top: 
                self.x_change = 3 
            else: 
                self.x_change = -3
        else:
            self.x_change = 0

        if dog_basket and self.rect.colliderect(dog_basket):
            return "basket"
        
        self.rect.move_ip(self.x_change, self.y_change)
    
        if self.rect.top > screen_height:
            self.kill()
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            if self.x_change > 0:
                if self.pos < 3:
                    self.pos += 1
                else:
                    self.pos = 0
            else:
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = 3
        self.bottom = pygame.rect.Rect((self.rect[0], self.rect.bottom), (self.rect[2], 3))     
        
        if not self.basket_triggered and self.rect.centerx <= 2 * section_width:
            self.basket_triggered = True
            return "basket"

        return False
        
    def check_fall(self):
        already_collided = False
        below = pygame.rect.Rect((self.rect[0], self.rect[1] + section_height), (self.rect[2], section_height))
        for lad in lads:
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True
           
                if self.is_first:
                    if random.randint(0, 3) == 0: 
                        self.falling = True
                        self.y_change = 6
                else:
                    if random.randint(0, 60) == 60:
                        self.rect.centerx = lad.centerx 
                        self.falling = True
                        self.y_change = 4
                        self.check_lad = False

        if not already_collided:
            self.check_lad = False
        
    def draw(self, screen):
        screen.blit(
            pygame.transform.rotate(self.image, 90 * self.pos),
            self.rect
        )
class Ball(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.pos = 1
        self.count = 0
        self.x_count = 0
        self.x_change = 2
        self.x_max = 4
        self.y_change = 0
        self.row = 1
        self.check_lad = False
        self.climbing = False

    def update(self):
        if self.y_change < 3 and not self.climbing:
            self.y_change += 0.25

        
        for i in range(len(plats)):
            if self.rect.colliderect(plats[i]):
                self.climbing = False
                self.y_change = -4

        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            self.pos *= -1
            if self.x_count < self.x_max:
                self.x_count += 1
            else:
                self.x_count = 0
      
                if self.x_change > 0:
                    if self.row in [1, 3, 5]:
                        self.x_max = random.randint(3, 6)
                    else:
                        self.x_max = random.randint(6, 10)
                else:
                    if self.row in [1, 3, 5]:
                        self.x_max = random.randint(6, 10)
                    else:
                        self.x_max = random.randint(3, 6)
                self.x_change *= -1

    
        if self.pos == 1:
            if self.x_change > 0:
                self.image = ball_img
            else:
                self.image = pygame.transform.flip(ball_img, True, False)
        else:
            if self.x_change > 0:
                self.image = ball2_img
            else:
                self.image = pygame.transform.flip(ball2_img, True, False)

        self.rect.move_ip(self.x_change, self.y_change)
        
        if self.rect.top > window_height or self.rect.top < 0:
            self.kill()

    def check_climb(self):
        already_collided = False
        for lad in lads:
            if self.rect.colliderect(lad) and not self.climbing and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 120) == 120:
                    self.climbing = True
                    self.y_change = -4
        if not already_collided:
            self.check_lad = False

        if self.rect.bottom < row6_y:
            self.row = 6
        else:

            self.row = 1
