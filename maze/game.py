
# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()

# music

run_music = pygame.mixer.music.load('naruto_run.ogg')
pygame.mixer.music.play(-1)

# sound affects
coin_noise = pygame.mixer.Sound('nani.ogg')
coin_noise.play()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
screenwall.pygame.Surface(SIZE)



# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Make a player
player1 = [25,25,25,25]
player1_img = pygame.image.load('naruto3.png')
player2 = [400,400,25,25]
player2_img = pygame.image.load('S3.png')
vel1 = [0, 0]
vel2 = [0, 0]
player1_speed = 5
player2_speed = 4
score1 = 0
score2 = 0


# make walls
edge1 = [0,0,30,750]
edge2 = [30,750,0,0]
edge3 = [400, 400, 500, 700]

wall1 = [300, 275, 200, 25]
wall2 = [150, 275, 100, 75]
wall3 = [450, 100, 300, 25]
wall4 = [250, 200, 200, 25]
wall5 = [250, 300, 120, 50]
wall6 = [250, 400, 300, 25]




walls = [edge1,edge2,edge3,wall1,wall2, wall3, wall5, wall6]


# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [200, 150, 25, 25]
coin4 = [311, 150, 25, 25]
coin5 = [120, 130, 25, 25]
coin6 = [120, 150, 25, 25]
coin7 = [300, 500, 25, 25]
coin8 = [400, 150, 25, 25]
coin9 = [488, 299, 25, 25]
coin10 = [322, 178, 25, 25]
coin11 = [300, 150, 25, 25]

coins = [coin1, coin2, coin3, coin4,coin5,coin6,coin7,coin8,coin9,coin10,coin11]



# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    player1_attack = pressed[pygame.K_m]
    player2_attack = pressed[pygame.K_z]

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
        
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
    if right:
        right = pygame.transform.flip(player1_img,1,0)


    #player 2 controls

    pressed2 = pygame.key.get_pressed()

    up2 = pressed[pygame.K_w]
    down2 = pressed[pygame.K_s]
    left2 = pressed[pygame.K_a]
    right2 = pressed[pygame.K_d]

    if left2:
        vel2[0] = -player2_speed
    elif right2:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    if up2:
        vel2[1] = -player2_speed
        
    elif down2:
        vel2[1] = player2_speed
    else:
        vel2[1] = 0


        
        

        
    # Game logic (Check for collisions, update points, etc.)


    
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]
    

    ''' get block edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] +player1[3]

    left2 = player2[0]
    right2 = player2[0] + player2[2]
    top2 = player2[1]
    bottom2 = player2[1] +player2[3]

    '''players collisons '''

    if intersects.rect_rect(player1,player2):                    
        if vel1[1] > 0:
            player1[1] = player2[1] - player1[3]
        if vel1[1]< 0:
            player1[1] = player2[1] + player2[3]

    if intersects.rect_rect(player1, player2):        
        if vel1[0] > 0:
            player1[0] = player2[0] - player1[2]
        elif vel1[0] < 0:
            player1[0] = player2[0] + player2[2]


    if intersects.rect_rect(player2,player1):                    
        if vel1[1] > 0:
            player2[1] = player1[1] - player2[3]
        if vel1[1]< 0:
            player2[1] = player1[1] + player1[3]

    if intersects.rect_rect(player2, player1):        
        if vel1[0] > 0:
            player2[0] = player1[0] - player2[2]
        elif vel1[0] < 0:
            player2[0] = player1[0] + player1[2]   


    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]
                
    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:


                player1[1] = w[1] + w[3]
                
    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:


                player2[1] = w[1] + w[3]




    ''' here is where you should resolve player collisions with screen edges '''
    if left < 0:
            player1[0] = 0
    elif right > WIDTH:
            player1[0] = WIDTH - player1[2]

    if top < 0:
            player1[1] = 0
    elif bottom > HEIGHT:
            player1[1] = HEIGHT - player1[3]

    if left < 0:
            player2[0] = 0
    elif right > WIDTH:
            player2[0] = WIDTH - player2[2]

    if top < 0:
            player2[1] = 0
    elif bottom > HEIGHT:
            player2[1] = HEIGHT - player2[3]


    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coin_noise.play()
        
        
    if len(coins) == 0:
        win = True

    ''' get the coins '''

    for c in coins:
        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player2, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coin_noise.play()
        
        
    if len(coins) == 0:
        win = True

                
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    loc2 = player2 [:2] 
    loc = player1[:2]
    screen.blit(player1_img,loc)
    screen.blit(player2_img,loc2)
    
    
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        scroll = pygame.image.load("scroll.png")
        screen.blit(scroll, (c))

    font = pygame.font.Font(None, 30)
    text = font.render(str(score1) + " of scrolls", 1, YELLOW)
    screen.blit(text, [600 , 300])
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()


