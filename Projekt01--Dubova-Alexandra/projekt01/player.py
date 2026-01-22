import pygame
from settings import section_width, section_height
from assets import standing, running, jumping, climbing1, climbing2



class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.y_change = 0
        self.x_speed = 3
        self.x_change = 0
        self.landed = False
        self.pos = 0
        self.dir = 1
        self.count = 0
        self.climbing = False
        self.image = standing
        self.ukazovatko = False
        self.max_ukazovatko = 450
        self.ukazovatko_len = self.max_ukazovatko
        self.ukazovatko_pos = 1
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.ukazovatko_box = self.rect
        self.rect.center = (x_pos, y_pos)
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)
        self.state = "idle" 

    def update(self, plats):
        self.landed = False
        for plat in plats:
            if self.bottom.colliderect(plat):
                self.landed = True
                if not self.climbing:
                    self.rect.centery = plat.top - self.rect.height / 2 + 1
                    self.y_change = 0
        if not self.landed and not self.climbing:
            self.y_change += 0.25
        self.rect.move_ip(self.x_change * self.x_speed, self.y_change)
        self.bottom = pygame.rect.Rect(self.rect.left + 10, self.rect.bottom - 10, self.rect.width-20, 10)
        if self.x_change != 0 or (self.climbing and self.y_change != 0):
            if self.count < 3:
                self.count += 1
            else:
                self.count = 0
                if self.pos == 0:
                    self.pos += 1
                else:
                    self.pos = 0
        else:
            self.pos = 0
        if self.ukazovatko:
            self.ukazovatko_pos = (self.ukazovatko_len // 30) % 2
            self.ukazovatko_len -= 1
            if self.ukazovatko_len == 0:
                self.ukazovatko = False
                self.ukazovatko_len = self.max_ukazovatko

        if self.state in ("run", "climb"):
            if self.count < 3:
                self.count += 1
            else:
                self.count = 0
                self.pos = 1 - self.pos
        else:
            self.pos = 0

        if self.climbing:
            self.state = "climb"
        elif not self.landed:
            self.state = "jump"
        elif self.x_change != 0:
            self.state = "run"
        else:
            self.state = "idle"
        
    def can_climb(self, ladders):
        can_climb = False
        climb_down = False

        under = pygame.Rect(
            self.rect.x,
            self.rect.y + 2 * self.rect.height,
            self.rect.width,
            self.rect.height
        )
        for lad in ladders:
            if self.rect.colliderect(lad) and not can_climb:
                can_climb = True
            if under.colliderect(lad) and not climb_down:
                climb_down = True
        return can_climb, climb_down


    def draw(self, screen):       
        if self.state == "climb":
            self.image = climbing1 if self.pos == 0 else climbing2
        elif self.state == "jump":
            self.image = jumping
        elif self.state == "run":
            self.image = running
        else:
            self.image = standing

        if self.dir == -1:
            img = pygame.transform.flip(self.image, True, False)
        else:
            img = self.image

        screen.blit(img, self.rect.topleft)

    def calc_hitbox(self):
        if not self.ukazovatko:
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5),
                                           (self.rect[2] - 30, self.rect[3] - 10))
        elif self.ukazovatko_pos == 0:
            if self.dir == 1:
                self.hitbox = pygame.rect.Rect((self.rect[0], self.rect[1] + 5),
                                               (self.rect[2] - 30, self.rect[3] - 10))
                self.ukazovatko_box = pygame.rect.Rect((self.hitbox[0] + self.hitbox[2], self.rect[1] + 5),
                                                   (self.hitbox[2], self.rect[3] - 10))
            else:
                self.hitbox = pygame.rect.Rect((self.rect[0] + 40, self.rect[1] + 5),
                                               (self.rect[2] - 30, self.rect[3] - 10))
                self.ukazovatko_box = pygame.rect.Rect((self.hitbox[0] - self.hitbox[2], self.rect[1] + 5),
                                                   (self.hitbox[2], self.rect[3] - 10))
        else:
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5),
                                           (self.rect[2] - 30, self.rect[3] - 10))
            self.ukazovatko_box = pygame.rect.Rect((self.hitbox[0], self.hitbox[1] - section_height),
                                               (self.hitbox[2], section_height))




