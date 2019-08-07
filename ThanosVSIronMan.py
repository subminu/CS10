import pygame, random, sys

# class for the IronMan sprite
class IronManClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("IronMan_up.png")
        self.state = pygame.image.load("IronMan_state.png")
        self.image_heart = pygame.image.load("heart.png")
        self.face = self.state.get_rect()
        self.rect = self.image.get_rect()
        self.rect_heart = self.image_heart.get_rect()
        self.face.center = [15,627.5]
        self.rect.center = [320, 540]
        self.angle = 0
        self.heart = 3

    def show_stamina(self, demage=False):
        if demage:
            self.heart -= 1
        for i in range(self.heart):
            screen.blit(IronMan.image_heart,[600-40*i,15])

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

    def proceed(self, speed):
        self.face[0] += speed
        if self.face[0] >= 600:
            global Thanos
            Thanos = Thanos_images[-1]
            animate()
            show_game_over('Win')

# class for object sprites (meteoroids and power)
class ObjectClass(pygame.sprite.Sprite):
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


# create one "screen" of object: 640 x 640
# use "blocks" of 64 x 64 pixels, so objects aren't too close together
def create_map():
    global objects
    locations = []
    for _i in range(10):  # 10 objects per screen
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 32 , row * 64 + 32 - 640]  # center x, y for objects
        if not (location in locations):  # prevent 2 objects in the same place
            locations.append(location)
            type = random.choice(["meteoroid", "meteoroid", "power"]) # Make more meteoroids displayed on screen
            if type == "meteoroid":
                img = "meteoroid.png"
            elif type == "power":
                img = "IronMan_nuclear.png"
            object = ObjectClass(img, location, type)
            objects.add(object)

# redraw the screen, including all sprites
def animate(scroll=False):
    screen.fill([0, 0, 0])
    objects.draw(screen)
    screen.blit(IronMan.image, IronMan.rect)
    screen.blit(score_text, [10, 10])
    screen.blit(Thanos,[600,590])
    if Thanos == Thanos_images[-1]:
        screen.blit(Thanos,[305,230])
    if scroll:
        IronMan.proceed(1)
    IronMan.show_stamina()
    screen.blit(IronMan.state, IronMan.face)
    pygame.display.flip()

def show_game_over(result):
    if result == 'Lose':
        lose_test = font.render("You lose", 3, (255, 255, 255))
        screen.blit(lose_test,[250, 280])
        screen.blit(Thanos, [305, 230])
    elif result == 'Win':
        win_text = font.render("You Win", 3, (255, 255, 255))
        screen.blit(win_text,[250, 280])
    exit_text = font.render("Click close button to exit", 2, (255, 255, 255))
    screen.blit(exit_text,[110, 310])
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == 12:
                running = False
    sys.exit()

# initialize everything
pygame.init()
screen = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Thanos VS IronMan")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
IronMan_images = ["IronMan_up.png", "IronMan_right1.png", "IronMan_right2.png", "IronMan_left2.png", "IronMan_left1.png"]
Thanos_images = [pygame.image.load(x) for x in ["Thanos.png","Thanos_lose.png"]]
Thanos = Thanos_images[0]
speed = [0, 10]
objects = pygame.sprite.Group()  # group of objects
IronMan = IronManClass()
IronMan.show_stamina()
map_position = 0
points = 0
create_map()  # create one screen full of objects
scroll = 0

# main Pygame event loop
running = True
while running:
    clock.tick(30)
    if IronMan.heart <= 0 :
        running = False
        show_game_over("Lose")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:  # left arrow turns left
                speed = IronMan.turn(-1)
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
                speed = IronMan.turn(1)
    IronMan.move(speed)  # move the IronMan (left or right)
    map_position -= speed[1]  # scroll the objects

    # create a new block of objects at the top
    if map_position <= -640:
        create_map()
        map_position = 0

    # check for hitting meteoroids or getting power
    hit = pygame.sprite.spritecollide(IronMan, objects, False)
    if hit:
        if hit[0].type == "meteoroid" and not hit[0].passed:  # crashed into meteoroids
            points -= 50
            IronMan.image = pygame.image.load("IronMan_crash.png")  # crash image
            animate()
            pygame.time.delay(1000)
            IronMan.image = pygame.image.load("IronMan_up.png")  # resume skiing
            IronMan.angle = 0
            speed = [0, 10]
            hit[0].passed = True
            if points >= 90 :
                points -= 100
            else:
                IronMan.heart -= 1
            hit[0].kill()
        elif hit[0].type == "power" and not hit[0].passed:  # got a power
            if IronMan.heart < 3 and points >= 90:
                print("worked")
                points -= 100
                IronMan.heart += 1
            points += 10
            hit[0].kill()  # remove the power


    objects.update()
    score_text = font.render("Score: " + str(points), 1, (255, 255, 255))
    if scroll == 1:
        animate(True)
        scroll = 0
    else:
        animate()
        scroll += 1