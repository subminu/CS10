# Listing_10-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Skier program

import pygame, sys, os, random
import time

# different images for the skier depending on his direction
"""
start = time. time()
"the code you want to test stays here"
end = time. time()
print(end - start)
"""


def load_images():
    folder = 'images/'
    image_names = []

    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.png']]):
            img_name = os.path.join(filename)
            if not filename.startswith(('IronMan_crash.png', 'IronMan_nuclear.png', 'meteoroid.png')):
                image_names.append(img_name)

    return image_names


def sort_images():
    sorted_images = ["IronMan_up.png", "IronMan_right1.png", "IronMan_right2.png", "IronMan_left2.png", "IronMan_left1.png"]
    '''unsorted_images = load_images()
    order_map = {}
    for pos, item in enumerate(image_order):
        order_map[item] = pos

    sorted_images = sorted(unsorted_images, key=order_map.get)
    print(sorted_images)'''
    return sorted_images


skier_images = sort_images()

"""
class GetImages(object):

    def __init__(self):
        self.folder = 'images/'
        self.image_order = ["skier_down.png", "skier_right1.png", "skier_right2.png","skier_left2.png", "skier_left1.png"]
        self.order_map = {}
        
        

    def load_images(self):
        self.image_names = []
        for filename in os.listdir(self.folder):
            if any([filename.endswith(x) for x in ['.png']]):
                img_name = os.path.join(filename)
                if not filename.startswith(('skier_crash.png', 'skier_flag.png', 'skier_tree.png')):
                    self.image_names.append(img_name)

        return self.image_names

    def sort_images(self):
        #self.sorted_images = self.load_images()
        
        for pos, item in enumerate(self.image_order):
            self.order_map[item] = pos

        #self.sorted_images = self.load_images(), self.sorted_images.sort(key=self.order_map.get)
        self.loaded_images = self.load_images()
        self.sorted_images = sorted(self.loaded_images, key=self.order_map.get)
        
        return self.sorted_images


#Sorted skier_images
#Simages = GetImages()

print(GetImages().load_images())
print(GetImages().sort_images())
skier_images1 = GetImages().sort_images()
print(skier_images1)
end = time. time()
print(end - start)

"""


# class for the Skier sprite
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("IronMan_up.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 540]
        self.angle = 0
        self.heart = 3

    def turn(self, direction):
        # load new image and change speed when the skier turns
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2
        if self.angle > 2:  self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 10 - abs(self.angle) * 2]
        return speed

    def move(self, speed):
        # move the skier right and left
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

    # class for obstacle sprites (trees and flags)


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self):
        global speed
        self.rect.centery += speed[1]
        if self.rect.centery > 640:
            self.kill()


# create one "screen" of obstacles: 640 x 640
# use "blocks" of 64 x 64 pixels, so objects aren't too close together
def create_map():
    global obstacles
    locations = []
    for _i in range(10):  # 10 obstacles per screen
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 32 , row * 64 + 32 - 640]  # center x, y for obstacle
        if not (location in locations):  # prevent 2 obstacles in the same place
            locations.append(location)
            type = random.choice(["meteoroid", "power"])
            if type == "meteoroid":
                img = "meteoroid.png"
            elif type == "power":
                img = "IronMan_nuclear.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)


# redraw the screen, including all sprites
def animate():
    screen.fill([0, 0, 0])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()


# initialize everything
pygame.init()
screen = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Thanos VS IronMan")
clock = pygame.time.Clock()
speed = [0, 10]
obstacles = pygame.sprite.Group()  # group of obstacle objects
skier = SkierClass()
map_position = 0
points = 0
create_map()  # create one screen full of obstacles
font = pygame.font.Font(None, 50)

# main Pygame event loop
running = True
while running:
    clock.tick(30)
    if skier.heart<=0:
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:  # left arrow turns left
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
                speed = skier.turn(1)
    skier.move(speed)  # move the skier (left or right)
    map_position -= speed[1]  # scroll the obstacles

    # create a new block of obstacles at the bottom
    if map_position <= -640:
        create_map()
        map_position = 0

    # check for hitting trees or getting flags
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "meteoroid" and not hit[0].passed:  # crashed into tree
            points = points - 50
            skier.image = pygame.image.load("IronMan_crash.png")  # crash image
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("IronMan_up.png")  # resume skiing
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
            skier.heart -=1
        elif hit[0].type == "power" and not hit[0].passed:  # got a flag
            points += 10
            hit[0].kill()  # remove the flag

    obstacles.update()
    score_text = font.render("Score: " + str(points), 1, (255, 255, 255))
    animate()

pygame.quit()