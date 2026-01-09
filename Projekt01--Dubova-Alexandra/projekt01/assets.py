import pygame
from settings import section_width, section_height

bone_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0197.PNG'), 
                                    (section_width * 1.5, section_height * 2))

basket_width = int(section_width * 2.5)
basket_height = int(section_height * 2.5)

micek_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0202.PNG'), 
                                    (section_width *2 , section_height))

dog_basket_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0201.PNG'),
    (basket_width, basket_height)
)

dog_basket2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0200.PNG'),
    (basket_width, basket_height)
)

bowl_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0203.PNG'),
    (section_width*5 , section_height *4)
)
en1_img =pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0196.PNG'),
    (section_width*5, section_height*5)
)
en2_img =pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0204.PNG'),
    (section_width*5, section_height*5)
)
en3_img =pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0216.PNG'),
    (section_width*5, section_height*5)
)
princess1_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0198.PNG'),
    (section_width*3, section_height*3)
)
princess2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0205.PNG'),
    (section_width*3, section_height*3)
)
ball_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0202.PNG'),
    (section_width*1.5, section_height*2)
)
ball2_img = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0206.PNG'),
    (section_width*1.5, section_height*2)
)

standing = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0180.PNG'),(3 * section_width, 3 * section_height))

jumping = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0192.PNG'),(3 * section_width, 3 * section_height))

running = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0190.PNG'),(3 * section_width, 3 * section_height))

climbing1 = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0188.PNG'),(3 * section_width, 3 * section_height))

climbing2 = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0188.PNG'),(3 * section_width, 3 * section_height))

ukazovatko_stand = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0199.PNG'),(2.5 *section_width, 2.5 * section_height))   

ukazovatko_jump = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0199.PNG'),(2.5 *section_width, 2.5 * section_height))   

ukazovatko_overhead = pygame.transform.scale(pygame.image.load(r'C:\Users\saska\OneDrive\Desktop\projekt-obrazky\IMG_0199.PNG'),(2.5 *section_width, 3.5 * section_height))   


"""bone_img = pygame.transform.scale(
    load("IMG_0197.PNG"),
    (int(section_width * 1.5), int(section_height * 2))
)

basket_width = int(section_width * 2.5)
basket_height = int(section_height * 2.5)

dog_basket_img = pygame.transform.scale(
    load("IMG_0201.PNG"),
    (basket_width, basket_height)
)

dog_basket2_img = pygame.transform.scale(
    load("IMG_0200.PNG"),
    (basket_width, basket_height)
)

standing = pygame.transform.scale(
    load("IMG_0180.PNG"),
    (3 * section_width, 3 * section_height)
)
"""