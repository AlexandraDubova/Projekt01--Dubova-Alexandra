import os   #pro dynamiku
import random 
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1' #call befor pzgame.init()
pygame.init()
info = pygame.display.Info() #vzska, sirka hry
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 800, screen_height - 150

#pro prevraceni kosiku
start_time = pygame.time.get_ticks()

#pro fps
timer = pygame.time.Clock()
fps = 60

pygame.display.set_caption ('Kitty Kong!') #jeste asi prejmenuji
#pro zmeneni ikonky pygame.display.set_icon ('image file')

screen = pygame.display.set_mode([window_width, window_height])
#na tohle se bude vsechno zobrazovat

section_width = window_width // 32 
section_height = window_height // 32
slope = section_height // 8

bone_spawn_time = 360
bone_count = bone_spawn_time
bone_time = 360
bone_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0197.PNG'), 
                                    (section_width * 1.5, section_height * 2))

basket_width = int(section_width * 2.5)
basket_height = int(section_height * 2.5)

micek_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0202.PNG'), 
                                    (section_width *2 , section_height))

dog_basket_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0201.PNG'),
    (basket_width, basket_height)
)

dog_basket2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0200.PNG'),
    (basket_width, basket_height)
)

bowl_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0203.PNG'),
    (section_width*5 , section_height *4)
)
en1_img =pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0196.PNG'),
    (section_width*5, section_height*5)
)
en2_img =pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0204.PNG'),
    (section_width*5, section_height*5)
)
princess1_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0198.PNG'),
    (section_width*3, section_height*3)
)
princess2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0205.PNG'),
    (section_width*3, section_height*3)
)
ball_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0202.PNG'),
    (section_width*1.5, section_height*2)
)
ball2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\Desktop\projekt-obrazky\IMG_0206.PNG'),
    (section_width*1.5, section_height*2)
)

start_y = window_height - 2 * section_height
row2_y = start_y - 4 * section_height
row3_y = row2_y - 7 * slope - 3 * section_height
row4_y = row3_y - 4 * section_height
row5_y = row4_y - 7 * slope - 3 * section_height
row6_y = row5_y - 4 * section_height
row6_top = row6_y - 4 * slope
row5_top = row5_y - 8 * slope
row4_top = row4_y - 8 * slope
row3_top = row3_y - 8 * slope
row2_top = row2_y - 8 * slope
row1_top = start_y - 5 * slope

ball_trigger = False
active_level = 0
counter = 0

enemy_rect = None
enemy_face_dir = 1   
enemy_x = int(3.5 * section_width)
enemy_y = int(row6_y - 4 * section_height)
enemy_speed = 3   # jak rychle se enemy pohybuje směrem k cíli


first_bone_taken = False


basket_flipped = False
basket_flip_start = 0
basket_flip_duration = 0

levels = [{'bridges': [(1, start_y, 15), (16, start_y - slope, 3),
                       (19, start_y - 2 * slope, 3), (22, start_y - 3 * slope, 3),
                       (25, start_y - 4 * slope, 3), (28, start_y - 5 * slope, 3),
                       (25, row2_y, 3), (22, row2_y - slope, 3),
                       (19, row2_y - 2 * slope, 3), (16, row2_y - 3 * slope, 3),
                       (13, row2_y - 4 * slope, 3), (10, row2_y - 5 * slope, 3),
                       (7, row2_y - 6 * slope, 3), (4, row2_y - 7 * slope, 3),
                       (2, row2_y - 8 * slope, 2), (4, row3_y, 3),
                       (7, row3_y - slope, 3), (10, row3_y - 2 * slope, 3),
                       (13, row3_y - 3 * slope, 3), (16, row3_y - 4 * slope, 3),
                       (19, row3_y - 5 * slope, 3), (22, row3_y - 6 * slope, 3),
                       (25, row3_y - 7 * slope, 3), (28, row3_y - 8 * slope, 2),
                       (25, row4_y, 3), (22, row4_y - slope, 3),
                       (19, row4_y - 2 * slope, 3), (16, row4_y - 3 * slope, 3),
                       (13, row4_y - 4 * slope, 3), (10, row4_y - 5 * slope, 3),
                       (7, row4_y - 6 * slope, 3), (4, row4_y - 7 * slope, 3),
                       (2, row4_y - 8 * slope, 2), (4, row5_y, 3),
                       (7, row5_y - slope, 3), (10, row5_y - 2 * slope, 3),
                       (13, row5_y - 3 * slope, 3), (16, row5_y - 4 * slope, 3),
                       (19, row5_y - 5 * slope, 3), (22, row5_y - 6 * slope, 3),
                       (25, row5_y - 7 * slope, 3), (28, row5_y - 8 * slope, 2),
                       (25, row6_y, 3), (22, row6_y - slope, 3),
                       (19, row6_y - 2 * slope, 3), (16, row6_y - 3 * slope, 3),
                       (2, row6_y - 4 * slope, 14), (13, row6_y - 4 * section_height, 6),
                       (10, row6_y - 3 * section_height, 3)],
           'ladders' :[(12, row2_y + 6 * slope, 2), (12, row2_y + 26 * slope, 2),
                       (25, row2_y + 11 * slope, 4), (6, row3_y + 11 * slope, 3),
                       (14, row3_y + 8 * slope, 4), (10, row4_y + 6 * slope, 1),
                       (10, row4_y + 24 * slope, 2), (16, row4_y + 6 * slope, 5),
                       (25, row4_y + 9 * slope, 4), (6, row5_y + 11 * slope, 3),
                       (11, row5_y + 8 * slope, 4), (23, row5_y + 4 * slope, 1),
                       (23, row5_y + 24 * slope, 2), (25, row6_y + 9 * slope, 4),
                       (13, row6_y + 5 * slope, 2), (13, row6_y + 25 * slope, 2),
                       (18, row6_y - 27 * slope, 4), (12, row6_y - 17 * slope, 2),
                       (10, row6_y - 17 * slope, 2), (12, -5, 13), (10, -5, 13)]}]


#nejspis predelam
class Bone(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.y_change = 0
        self.x_change = 1
        self.pos = 0
        self.count = 0
        self.basket_collision = False
        self.falling = False
        self.check_lad = False
         # enemy/taken logic
        self.taken_by_enemy = False
        self.take_time = 0
        self.hold_duration = 300   # ms - jak dlouho enemy drží kost před hodem
        self.taken_dir = 1

        # označení první kosti
        self.is_first = False

        self.bottom = self.rect
        self.last_trigger = 0
        self.trigger_cooldown = 800

    def update(self, ball_trig):

                # pokud je kost držená enemy, následuje enemy a po uplynutí hold_duration je hozena
        if self.taken_by_enemy:
            # následuj enemy pokud máme enemy_rect
            if enemy_rect is not None:
                hold_x = enemy_rect.centerx + (20 * self.taken_dir)  # offset, aby kost nebyla přesně ve středu
                hold_y = enemy_rect.centery - 10  # mírně nad enemy
                self.rect.center = (hold_x, hold_y)

            # když uplynul čas držení, kost se "hodí"
            if pygame.time.get_ticks() - self.take_time > self.hold_duration:
                self.taken_by_enemy = False
                # pohození: nastavit rychlost do směru enemy a lehký oblouk nahoru
                self.x_change = 5 * self.taken_dir
                self.y_change = -5
                self.falling = False
                self.check_lad = False
                global enemy_face_dir
                enemy_face_dir = self.taken_dir
                print("DEBUG: bone thrown by enemy, dir:", self.taken_dir)

            # během držení neprovádíme další update logiku
            self.bottom = pygame.rect.Rect((self.rect[0], self.rect.bottom), (self.rect[2], 3))
            return ball_trig

        if self.y_change < 8 and not self.falling:
            self.y_change +=2
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0
                self.falling = False
        if self.rect.colliderect(dog_basket): 
            now = pygame.time.get_ticks()
            if not self.basket_collision:
                self.basket_collision = True

            global basket_flipped, basket_flip_start
            if not basket_flipped:
                basket_flipped = True
                basket_flip_start = now
                print("DEBUG: basket flipped by bone at", self.rect.center)

            if now - self.last_trigger > self.trigger_cooldown:
                if random.random() < 0.4:   # 40% šance, uprav podle chuti (0..1)
                    ball_trig = True
                    self.last_trigger = now
                    print("DEBUG: Bone collided — spawn (probabilistic, cooldown passed)")
                else: 
                    print("DEBUG: Bone collided — but random failed  (probabilistic)")
                
        if not self.falling:
            if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top > self.rect.bottom >= row2_top: 
                self.x_change = 3 
            else: 
                self.x_change = -3
        else:
            self.x_change = 0
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
        return ball_trig
        
    def check_fall(self):
        already_collided = False
        below = pygame.rect.Rect((self.rect[0], self.rect[1] + section_height), (self.rect[2], section_height))
        for lad in lads:
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True
                # pokud je to první kost, výrazně zvýšíme šanci, že sjede po žebříku
                if self.is_first:
                    if random.randint(0, 3) == 0:   # 25% chance on ladder checks -> rychleji dolů
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

    def draw(self):
        screen.blit(pygame.transform.rotate(bone_img, 90 * self.pos), self.rect.topleft)

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
        # pokud narazí na platformu, přestat padat
        for i in range(len(plats)):
            if self.rect.colliderect(plats[i]):
                self.climbing = False
                self.y_change = -4

        # animace a změna směru analogicky k originálu
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            self.pos *= -1
            if self.x_count < self.x_max:
                self.x_count += 1
            else:
                self.x_count = 0
                # uprav rozsahy podle řady, aby se střídal pohyb jako originál
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

        # vybrat správný obrázek podle směru a fáze
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
        if self.rect.top > screen_height or self.rect.top < 0:
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

        # zjistit kde je řada (můžeš upravit prahy podle layoutu)
        if self.rect.bottom < row6_y:
            self.row = 6
        elif self.rect.bottom < row5_y:
            self.row = 5
        elif self.rect.bottom < row4_y:
            self.row = 4
        elif self.rect.bottom < row3_y:
            self.row = 3
        elif self.rect.bottom < row2_y:
            self.row = 2
        else:
            self.row = 1

class Bridge:
    def __init__(self, x_pos, y_pos, length ):
        self.x_pos = x_pos * section_width 
        self.y_pos = y_pos
        self.length = length
        self.top = self.draw()

    def draw(self):
        line_width = 7
        platform_color = (225, 51, 129) #'red', 'dark red' mze byt
        for i in range(self.length):
            bot_coord = self.y_pos + section_height
            left_coord = self.x_pos + (section_width * i)
            mid_coord = left_coord + (section_width * 0.5)
            right_coord = left_coord + section_width 
            top_coord = self.y_pos
            # draw 4 lines, top,bot,left diag, right diag
            pygame.draw.line(screen, platform_color, (left_coord, top_coord), 
                                    (right_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), 
                                    (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), 
                                    (mid_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (mid_coord, top_coord), 
                                    (right_coord, bot_coord), line_width)
            # get the top platform 'surface'
        top_line = pygame.rect.Rect((self.x_pos, self.y_pos),(self.length*section_width, 2))
        #pygame.draw.rect(screen, 'blue', top_line)
        return top_line
 
class Ladder:
    def __init__(self, x_pos, y_pos, length ):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.body = self.draw()

    def draw(self):
        line_width = 3
        lad_color = 'dark grey'  
        lad_height = 0.6
        for i in range(self.length):
            top_coord = self.y_pos + lad_height * section_height * i
            bot_coord = top_coord + lad_height * section_height
            mid_coord = (lad_height / 2) * section_height + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + section_width
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)
        body = pygame.rect.Rect((self.x_pos, self.y_pos - section_height),
                                (section_width, (lad_height * self.length * section_height + section_height)))
        return body

#funkce na malovani platform a zebriky
def draw_screen():
    platforms = []
    climbers = []
    ladder_objs = []
    bridge_objs = []

    ladders = levels[active_level]['ladders']
    bridges = levels[active_level]['bridges']

    for bridge in bridges:
        bridge_objs.append(Bridge(*bridge))
        platforms.append(bridge_objs[-1].top)
    
    for ladder in ladders:
        ladder_objs.append(Ladder(*ladder))
        if ladder[2] >= 3:
            climbers.append(ladder_objs[-1].body)
    return platforms, climbers

def draw_extras():
    #bonusovz text, yivotz, level
    #dog basket
    basket = draw_basket()
    draw_bowl()
    draw_enemy()
    
    #princezna
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

    # pokud je basket_flipped True, vykresli druhý obrázek (převrácený)
    if basket_flipped:
        screen.blit(dog_basket2_img, basket_rect.topleft)
        # pokud chceme, aby se po době obrátil zpět, kontrolujeme duration:
        if basket_flip_duration > 0 and elapsed_time_since_flip > basket_flip_duration:
            basket_flipped = False
            print("DEBUG: basket auto-unflipped after duration")
    else:
        screen.blit(dog_basket_img, basket_rect.topleft)

    return basket_rect

def draw_bowl():
    screen.blit(bowl_img, (int(1.2*section_width), int(row6_y -2.8 * section_height)))

def draw_enemy():
    global enemy_rect
    # vždy nastavíme img = en1_img jako základ
    img = en1_img

    t = pygame.time.get_ticks() // 500
    phase = t % 4

    # vyber frame podle animace
    if phase == 0:
        frame = en1_img
    elif phase == 1:
        frame = en2_img
    elif phase == 2:
        frame = pygame.transform.flip(en1_img, True, False)
    else:
        frame = pygame.transform.flip(en2_img, True, False)

    # použij ten frame jako pracovní obrázek
    img = frame

    # pokud chce enemy koukat doleva
    if enemy_face_dir == -1:
        img = pygame.transform.flip(img, True, False)

    # vykreslit
    screen.blit(img, (enemy_x, enemy_y))

    # aktualizovat enemy_rect
    enemy_rect = pygame.Rect(enemy_x, enemy_y, img.get_width(), img.get_height())



# ----- replace main loop with this block -----
bones = pygame.sprite.Group()
balls = pygame.sprite.Group()

run = True
while run:
    timer.tick(fps)

    # --- events (must be called every loop) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    # --- clear / draw background ---
    screen.fill('pink')

    # --- draw platforms / ladders and extras (this sets enemy_rect inside draw_enemy) ---
    plats, lads = draw_screen()
    dog_basket = draw_extras()    # draw_enemy() is called inside, sets enemy_rect

    now = pygame.time.get_ticks()

    # --- decide which bone enemy should move to (nearest untaken, not falling) ---
    target_bone = None
    min_dx = 10**9
    for bone in bones:
        if (not bone.taken_by_enemy) and (not bone.falling):
            dx = abs(bone.rect.centerx - enemy_x)
            if dx < min_dx:
                min_dx = dx
                target_bone = bone

    # --- move enemy horizontally toward target bone (or return to default) ---
    default_x = int(3.5 * section_width)
    """if target_bone is not None:
        # move enemy toward target bone
        if abs(enemy_x - target_bone.rect.centerx) > enemy_speed:
            if enemy_x < target_bone.rect.centerx:
                enemy_x += enemy_speed
                enemy_face_dir = 1
            else:
                enemy_x -= enemy_speed
                enemy_face_dir = -1
        # else: if very close, collision detection below will pick up bone
    else:
        # no target -> slowly return to default_x
        if abs(enemy_x - default_x) > enemy_speed:
            enemy_x += enemy_speed * (1 if enemy_x < default_x else -1)
            enemy_face_dir = 1 if enemy_x < default_x else -1
        else:
            enemy_x = default_x"""

    t = pygame.time.get_ticks() // 500
    phase = t % 4
    if phase == 0:
        frame = en1_img
    elif phase == 1:
        frame = en2_img
    elif phase == 2:
        frame = pygame.transform.flip(en1_img, True, False)
    else:
        frame = pygame.transform.flip(en2_img, True, False)
    img = frame
    if enemy_face_dir == -1:
        img = pygame.transform.flip(img, True, False)
    # blit and set rect
    screen.blit(img, (enemy_x, enemy_y))
    enemy_rect = pygame.Rect(enemy_x, enemy_y, img.get_width(), img.get_height())

    # --- spawn bones (same logic as before) ---
    if bone_count < bone_spawn_time:
        bone_count += 1
    else:
        bone_count = random.randint(0, 120)
        bone_time = bone_count - bone_spawn_time
        bone = Bone(270, 270)
        if not first_bone_taken:
            bone.is_first = True
            first_bone_taken = True
            bone.falling = True
            bone.y_change = 6
            bone.check_lad = True
        bones.add(bone)

    # --- check collisions: if enemy touches a bone, mark it taken ---
    # (we do this AFTER moving enemy so positions are consistent)
    for bone in bones:
        if enemy_rect is not None and not bone.taken_by_enemy and not bone.falling:
            if bone.rect.colliderect(enemy_rect):
                bone.taken_by_enemy = True
                bone.take_time = now
                # decide direction based on bone position relative to enemy
                if bone.rect.centerx > enemy_rect.centerx:
                    bone.taken_dir = 1
                    enemy_face_dir = 1
                else:
                    bone.taken_dir = -1
                    enemy_face_dir = -1
                # make first bone special
                bone.hold_duration = 120 if bone.is_first else 300
                print("DEBUG: enemy picked bone at", bone.rect.center, "dir:", bone.taken_dir)

    # --- update & draw bones ---
    for bone in list(bones):   # list() to be safe if group changes while iterating
        bone.check_fall()
        ball_trigger = bone.update(ball_trigger)
        bone.draw()

    # --- handle ball spawn ---
    MAX_BALLS = 6
    if ball_trigger:
        if len(balls) < MAX_BALLS:
            ball = Ball(5 * section_width, window_height - 4 * section_height)
            balls.add(ball)
            print("DEBUG: spawned Ball — total balls:", len(balls))
        else:
            print("DEBUG: spawn skipped (too many balls)")
        ball_trigger = False

    # --- update & draw balls ---
    for b in list(balls):
        b.check_climb()
        b.update()
        screen.blit(b.image, b.rect.topleft)

    # --- flip display ---
    pygame.display.flip()

pygame.quit()
# ----- end replacement block -----
