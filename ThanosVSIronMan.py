import pygame, random

# class for the IronMan sprite
class IronManClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("IronMan_up.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 540]
        self.angle = 0
        self.heart = 3

    def turn(self, direction):
        # load new image and change speed when the IronMan turns
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2
        if self.angle > 2:  self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(IronMan_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 10 - abs(self.angle) * 2]
        return speed

    def move(self, speed):
        # move the IronMan right and left
        self.rect.centerx = self.rect.centerx + speed[0] * 3
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620


# class for obstacle sprites (meteoroids and nuclears)
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
            type = random.choice(["meteoroid", "meteoroid", "power"]) # Make more meteoroids displayed on screen
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
    screen.blit(IronMan.image, IronMan.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()


# initialize everything
pygame.init()
screen = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Thanos VS IronMan")
IronMan_images = ["IronMan_up.png", "IronMan_right1.png", "IronMan_right2.png", "IronMan_left2.png", "IronMan_left1.png"]
clock = pygame.time.Clock()
speed = [0, 10]
obstacles = pygame.sprite.Group()  # group of obstacle objects
IronMan = IronManClass()
map_position = 0
points = 0
create_map()  # create one screen full of obstacles
font = pygame.font.Font(None, 50)

# main Pygame event loop
running = True
while running:
    clock.tick(30)
    if IronMan.heart<=0:
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:  # left arrow turns left
                speed = IronMan.turn(-1)
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
                speed = IronMan.turn(1)
    IronMan.move(speed)  # move the IronMan (left or right)
    map_position -= speed[1]  # scroll the obstacles

    # create a new block of obstacles at the bottom
    if map_position <= -640:
        create_map()
        map_position = 0

    # check for hitting meteoroids or getting nuclears
    hit = pygame.sprite.spritecollide(IronMan, obstacles, False)
    if hit:
        if hit[0].type == "meteoroid" and not hit[0].passed:  # crashed into meteoroids
            points = points - 50
            IronMan.image = pygame.image.load("IronMan_crash.png")  # crash image
            animate()
            pygame.time.delay(1000)
            IronMan.image = pygame.image.load("IronMan_up.png")  # resume skiing
            IronMan.angle = 0
            speed = [0, 10]
            hit[0].passed = True
            IronMan.heart -=1
        elif hit[0].type == "power" and not hit[0].passed:  # got a nuclear
            points += 10
            hit[0].kill()  # remove the nuclear

    obstacles.update()
    score_text = font.render("Score: " + str(points), 1, (255, 255, 255))
    animate()

pygame.quit()