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
        self.bottom = self.rect

    def update(self, micek_trig):
        if self.y_change < 8 and not self.falling:
            bone.y_change +=2
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0
                self.falling = False
        if self.rect.colliderect(dog_basket): 
            if not self.basket_collision:
                self.basket_collision = True
                if random.randint(0, 4) == 4:
                    micek_trig = True

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
        return micek_trig
        
    def check_fall(self):
        already_collided = False
        below = pygame.rect.Rect((self.rect[0], self.rect[1] + section_height), (self.rect[2], section_height))
        for lad in lads:
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 60) == 60:
                    self.falling = True
                    self.y_change = 4
        if not already_collided:
            self.check_lad = False

    def draw(self):
        screen.blit(pygame.transform.rotate(bone_img, 90 * self.pos), self.rect.topleft)

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
    #princezna
    #dog basket
    basket = draw_basket()
    draw_bowl()
    draw_enemy()
    return basket


def draw_basket():
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 

    basket_rect = pygame.Rect(1 * section_width, start_y - 2 * section_height,
                              section_width * 1, section_height * 1)
  
    if elapsed_time < 30.5:
        screen.blit(dog_basket_img, basket_rect.topleft)
    else:
        screen.blit(dog_basket2_img, basket_rect.topleft)


    return basket_rect

def draw_bowl():
    screen.blit(bowl_img, (int(1.2*section_width), int(row6_y -2.8 * section_height)))

def draw_enemy():
    phase_time = bone_time //4
    if bone_spawn_time - bone_time > 3 * phase_time:
        en_img = en1_img
    else :
        en_img = pygame.transform.flip(en1_img, True, False)
        screen.blit(bone_img, (250, 250))
    screen.blit(en1_img, (3.5 * section_width, row6_y - 5.5 * section_height))


bones = pygame.sprite.Group()


run = True
while run:
    screen.fill ('pink')
    timer.tick(fps)

      #draw platforms and ladders on the screen  in dedicated functions
    plats, lads = draw_screen()
    dog_basket = draw_extras()
    
    if bone_count < bone_spawn_time: 
        bone_count += 1
    else:
        bone_count = random.randint(0, 120)
        bone_time = bone_count - bone_spawn_time
        bone = Bone(270, 270)
        bones.add(bone)

    for bone in bones:
        bone.draw()
        bone.check_fall()
        ball_trigger = bone.update(ball_trigger)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
