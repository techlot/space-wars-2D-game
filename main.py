import pygame
import sys
import os
pygame.font.init()
pygame.mixer.init()

# Main window settings --------------------------------------------------- #
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 40

SPACESHIP_SPEED = 3
MAX_BULLETS = 5
BULLET_SPEED = 9

YELLOW_HIT = pygame.USEREVENT + 1
PURPLE_HIT = pygame.USEREVENT + 2


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Media imports ---------------------------------------------------------- #
SPACE_IMAGE = pygame.image.load(os.path.join('Assets', 'space.png'))
SPACE_WARS_LOGO = pygame.image.load(os.path.join('Assets', 'space-wars-logo.png'))
BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'button.png')),(160, 44))
BUTTON_IMAGE_ACT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'button-act.png')),(161, 45))
MENU_FONT = pygame.font.Font('Assets/FSEX300.ttf', 23)
MENU_FONT_ACT = pygame.font.Font('Assets/FSEX300.ttf', 24)
CREDITS_IMAGE = pygame.image.load(os.path.join('Assets', 'credits.png'))
GO_BACK_BUTTON_IMAGE = pygame.image.load(os.path.join('Assets', 'go-back-button.png'))
GO_BACK_BUTTON_IMAGE_ACT = pygame.image.load(os.path.join('Assets', 'go-back-button-act.png'))
CREDITS_FONT = pygame.font.Font('Assets/FSEX300.ttf', 30)
HELP_IMAGE = pygame.image.load(os.path.join('Assets', 'help.png'))
HELP_FONT = pygame.font.Font('Assets/FSEX300.ttf', 20)
YELLOW_SPACESHIP = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'yellow-spaceship.png')), 90), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
PURPLE_SPACESHIP = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'purple-spaceship.png')), 270), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'yellow-bullet.png')), 270)
PURPLE_BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'purple-bullet.png')), 90)
HEALTH_FONT = pygame.font.Font('Assets/FSEX300.ttf', 25)
WINNER_FONT = pygame.font.Font('Assets/FSEX300.ttf', 150)
SYSTEM_FONT = pygame.font.Font('Assets/FSEX300.ttf', 60)
SYSTEM_FONT_1 = pygame.font.Font('Assets/FSEX300.ttf', 30)
SYSTEM_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'credits.png')), (400, 129))
BUTTON_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'button-01.png')), (135, 30))
BUTTON_IMAGE_1_ACT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'button-01-act.png')), (136, 31))
YELLOW_FIRE = pygame.mixer.Sound('Assets/purple-shoot.wav')
PURPLE_FIRE = pygame.mixer.Sound('Assets/yellow-shoot.wav')
BULLET_HIT =  pygame.mixer.Sound('Assets/hit.wav')
WIN_SOUND =  pygame.mixer.Sound('Assets/win-sound.wav')

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (255, 255, 0)
PURPLE_COLOR = (255, 0, 255)
PALE_YELLOW_COLOR = (248, 250, 187)
PALE_PURPLE_COLOR = (212, 187, 250)
SKY_BLUE_COLOR = (40, 209, 226)

FPS = 60

def main_menu():
    py_1 = 0
    py_2 = WINDOW_HEIGHT * -1
    background_speed = 1
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pic_1 = WINDOW.blit(SPACE_IMAGE, (0, py_1))
        pic_2 = WINDOW.blit(SPACE_IMAGE, (0, py_2))
        py_1 += background_speed
        py_2 += background_speed

        if py_1 >= WINDOW_HEIGHT:
            py_1 = WINDOW_HEIGHT * -1
        
        if py_2 >= WINDOW_HEIGHT:
            py_2 = WINDOW_HEIGHT * -1

        space_wars_logo = WINDOW.blit(SPACE_WARS_LOGO, (WINDOW_WIDTH // 2 - SPACE_WARS_LOGO.get_width() // 2, 50))
    
        button_start = WINDOW.blit(BUTTON_IMAGE, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 220))
        start_txt = MENU_FONT.render('START', 1, BLACK_COLOR)
        WINDOW.blit(start_txt, (WINDOW_WIDTH // 2 - start_txt.get_width() // 2, 229))
        
        button_help = WINDOW.blit(BUTTON_IMAGE, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 290))
        help_txt = MENU_FONT.render('HELP', 1, BLACK_COLOR)
        WINDOW.blit(help_txt, (WINDOW_WIDTH // 2 - help_txt.get_width() // 2, 299))
        
        button_credits = WINDOW.blit(BUTTON_IMAGE, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 360))
        credits_txt = MENU_FONT.render('CREDITS', 1, BLACK_COLOR)
        WINDOW.blit(credits_txt, (WINDOW_WIDTH // 2 - credits_txt.get_width() // 2, 369))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button_start.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(BUTTON_IMAGE_ACT, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 220))
            start_txt_act = MENU_FONT_ACT.render('START', 1, BLACK_COLOR)
            WINDOW.blit(start_txt_act, (WINDOW_WIDTH // 2 - start_txt_act.get_width() // 2, 229))
            if click:
                game()

        if button_help.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(BUTTON_IMAGE_ACT, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 290))
            help_txt_act = MENU_FONT_ACT.render('HELP', 1, BLACK_COLOR)
            WINDOW.blit(help_txt_act, (WINDOW_WIDTH // 2 - help_txt_act.get_width() // 2, 299))
            if click:
                help()

        if button_credits.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(BUTTON_IMAGE_ACT, (WINDOW_WIDTH // 2 - BUTTON_IMAGE.get_width() // 2, 360))
            credits_txt_act = MENU_FONT_ACT.render('CREDITS', 1, BLACK_COLOR)
            WINDOW.blit(credits_txt_act, (WINDOW_WIDTH // 2 - credits_txt_act.get_width() // 2, 369))
            if click:
                credits()

        pygame.display.update()

def game():
    is_running = True
    
    yellow_spaceship = pygame.Rect(200, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    purple_spaceship = pygame.Rect(750, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    purple_bullets = []

    YELLOW_HEALTH, PURPLE_HEALTH = 100, 100

    clock = pygame.time.Clock()
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and len(yellow_bullets) < MAX_BULLETS:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(yellow_spaceship.x + SPACESHIP_WIDTH, yellow_spaceship.y + SPACESHIP_HEIGHT // 2 - 3, 14, 7)
                    yellow_bullets.append(bullet)
                    YELLOW_FIRE.play()

            if event.type == pygame.KEYDOWN and len(purple_bullets) < MAX_BULLETS:
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(purple_spaceship.x - 14, purple_spaceship.y + SPACESHIP_HEIGHT // 2 - 3, 14, 7)
                    purple_bullets.append(bullet)
                    PURPLE_FIRE.play()

            if event.type == PURPLE_HIT:
                PURPLE_HEALTH -= 5
            
            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 5

        key_is_pressed = pygame.key.get_pressed() 

        if key_is_pressed[pygame.K_a] and yellow_spaceship.x > 0:
            yellow_spaceship.x -= SPACESHIP_SPEED
        if key_is_pressed[pygame.K_d] and yellow_spaceship.x < 495 - SPACESHIP_HEIGHT:
            yellow_spaceship.x += SPACESHIP_SPEED
        if key_is_pressed[pygame.K_w] and yellow_spaceship.y > 0:
            yellow_spaceship.y -= SPACESHIP_SPEED
        if key_is_pressed[pygame.K_s] and yellow_spaceship.y < WINDOW_HEIGHT - SPACESHIP_HEIGHT:
            yellow_spaceship.y += SPACESHIP_SPEED

        if key_is_pressed[pygame.K_LEFT] and purple_spaceship.x > 505 + 10:
            purple_spaceship.x -= SPACESHIP_SPEED
        if key_is_pressed[pygame.K_RIGHT] and purple_spaceship.x < WINDOW_WIDTH - SPACESHIP_WIDTH:
            purple_spaceship.x += SPACESHIP_SPEED
        if key_is_pressed[pygame.K_UP] and purple_spaceship.y > 0:
            purple_spaceship.y -= SPACESHIP_SPEED
        if key_is_pressed[pygame.K_DOWN] and purple_spaceship.y < WINDOW_HEIGHT - SPACESHIP_HEIGHT:
            purple_spaceship.y += SPACESHIP_SPEED 

        for bullet in yellow_bullets:
            bullet.x += BULLET_SPEED
            if purple_spaceship.colliderect(bullet):
                BULLET_HIT.play()
                pygame.event.post(pygame.event.Event(PURPLE_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > WINDOW_WIDTH:
                yellow_bullets.remove(bullet)

        for bullet in purple_bullets:
            bullet.x -= BULLET_SPEED
            if yellow_spaceship.colliderect(bullet):
                BULLET_HIT.play()
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                purple_bullets.remove(bullet)
            elif bullet.x < -14:
                purple_bullets.remove(bullet)

        WINDOW.blit(SPACE_IMAGE, (0, 0))
        yellow_health_text = HEALTH_FONT.render('Health: ' + str(YELLOW_HEALTH), 1, SKY_BLUE_COLOR)
        purple_health_text = HEALTH_FONT.render('Health: ' + str(PURPLE_HEALTH), 1, SKY_BLUE_COLOR)
        WINDOW.blit(yellow_health_text, (10, 10))
        WINDOW.blit(purple_health_text, (WINDOW_WIDTH - purple_health_text.get_width() - 10, 10))
        WINDOW.blit(YELLOW_SPACESHIP, (yellow_spaceship.x, yellow_spaceship.y))
        WINDOW.blit(PURPLE_SPACESHIP, (purple_spaceship.x, purple_spaceship.y))
        for bullet in yellow_bullets:
            WINDOW.blit(YELLOW_BULLET, (bullet.x, bullet.y))
        for bullet in purple_bullets:
            WINDOW.blit(PURPLE_BULLET, (bullet.x, bullet.y))

        win_message = ''
        win_color = BLACK_COLOR
        if YELLOW_HEALTH <= 0:
            win_message = 'PURPLE WON'
            win_color = PURPLE_COLOR
        
        if PURPLE_HEALTH <= 0:
            win_message = 'YELLOW WON'
            win_color = YELLOW_COLOR 

        if win_message != '':
            WIN_SOUND.play()
            winner_message = WINNER_FONT.render(win_message, 1, win_color)
            WINDOW.blit(winner_message, (WINDOW_WIDTH // 2 - winner_message.get_width() // 2, WINDOW_HEIGHT // 2 - winner_message.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            system_menu()
            is_running = False
            
        pygame.display.update()

def help():
    is_running = True
    py_1 = 0
    py_2 = WINDOW_HEIGHT * -1
    background_speed = 1
    clock = pygame.time.Clock()
    while is_running:
        clock.tick(FPS)
        pic_1 = WINDOW.blit(SPACE_IMAGE, (0, py_1))
        pic_2 = WINDOW.blit(SPACE_IMAGE, (0, py_2))
        py_1 += background_speed
        py_2 += background_speed

        if py_1 >= WINDOW_HEIGHT:
            py_1 = WINDOW_HEIGHT * -1
        
        if py_2 >= WINDOW_HEIGHT:
            py_2 = WINDOW_HEIGHT * -1

        WINDOW.blit(HELP_IMAGE, (WINDOW_WIDTH // 2 - HELP_IMAGE.get_width() // 2, WINDOW_HEIGHT // 2 - HELP_IMAGE.get_height() // 2))
        help_text = HELP_FONT.render('Use these keys to move your spaceships and fire:', 1, BLACK_COLOR)
        WINDOW.blit(help_text, (WINDOW_WIDTH // 2 - help_text.get_width() // 2, 115))
        w_text = HELP_FONT.render('W - up', 1, PALE_YELLOW_COLOR)
        WINDOW.blit(w_text, (310, 140))
        s_text = HELP_FONT.render('S - down', 1, PALE_YELLOW_COLOR)
        WINDOW.blit(s_text, (310, 160))
        a_text = HELP_FONT.render('A - left', 1, PALE_YELLOW_COLOR)
        WINDOW.blit(a_text, (310, 180))
        d_text = HELP_FONT.render('D - right', 1, PALE_YELLOW_COLOR)
        WINDOW.blit(d_text, (310, 200))
        l_ctrl_text = HELP_FONT.render('LCTRL - fire', 1, PALE_YELLOW_COLOR)
        WINDOW.blit(l_ctrl_text, (310, 220))

        up_text = HELP_FONT.render('/\ - up', 1, PALE_PURPLE_COLOR)
        WINDOW.blit(up_text, (600, 140))
        down_text = HELP_FONT.render('\/ - down', 1, PALE_PURPLE_COLOR)
        WINDOW.blit(down_text, (600, 160))
        left_text = HELP_FONT.render('< - left', 1, PALE_PURPLE_COLOR)
        WINDOW.blit(left_text, (600, 180))
        right_text = HELP_FONT.render('> - right', 1, PALE_PURPLE_COLOR)
        WINDOW.blit(right_text, (600, 200))
        r_ctrl_text = HELP_FONT.render('RCTRL - fire', 1, PALE_PURPLE_COLOR)
        WINDOW.blit(r_ctrl_text, (600, 220))

        go_back_button = WINDOW.blit(GO_BACK_BUTTON_IMAGE, (196, 450))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if go_back_button.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(GO_BACK_BUTTON_IMAGE_ACT, (196, 451))
            if click:
                is_running = False

        click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def credits():
    is_running = True
    py_1 = 0
    py_2 = WINDOW_HEIGHT * -1
    background_speed = 1
    clock = pygame.time.Clock()
    while is_running:
        clock.tick(FPS)
        pic_1 = WINDOW.blit(SPACE_IMAGE, (0, py_1))
        pic_2 = WINDOW.blit(SPACE_IMAGE, (0, py_2))
        py_1 += background_speed
        py_2 += background_speed

        if py_1 >= WINDOW_HEIGHT:
            py_1 = WINDOW_HEIGHT * -1
        
        if py_2 >= WINDOW_HEIGHT:
            py_2 = WINDOW_HEIGHT * -1

        WINDOW.blit(CREDITS_IMAGE, (WINDOW_WIDTH // 2 - CREDITS_IMAGE.get_width() // 2, WINDOW_HEIGHT // 2 - CREDITS_IMAGE.get_height() // 2))
        created_by_text = CREDITS_FONT.render('Created by', 1, BLACK_COLOR)
        WINDOW.blit(created_by_text, (WINDOW_WIDTH // 2 - created_by_text.get_width() // 2, WINDOW_HEIGHT // 2 - 40))
        name_text = CREDITS_FONT.render('Anton Chernukha', 1, WHITE_COLOR)
        WINDOW.blit(name_text, (WINDOW_WIDTH // 2 - name_text.get_width() // 2, WINDOW_HEIGHT // 2))
        go_back_button = WINDOW.blit(GO_BACK_BUTTON_IMAGE, (246, 315))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if go_back_button.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(GO_BACK_BUTTON_IMAGE_ACT, (246, 316))
            if click:
                is_running = False

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
            
def system_menu():
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        clock.tick(FPS)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        WINDOW.blit(SPACE_IMAGE, (0, 0))
        WINDOW.blit(SYSTEM_MENU_IMAGE, (WINDOW_WIDTH // 2 - SYSTEM_MENU_IMAGE.get_width() // 2, WINDOW_HEIGHT // 2 - CREDITS_IMAGE.get_height() // 2))
        system_text = SYSTEM_FONT_1.render('Game Ended!', 1, BLACK_COLOR)
        WINDOW.blit(system_text, (WINDOW_WIDTH // 2 - system_text.get_width() // 2, WINDOW_HEIGHT // 2 - 50))
        play_again_button = WINDOW.blit(BUTTON_IMAGE_1, (335, 300))
        play_again_text = MENU_FONT.render('PLAY AGAIN', 1, WHITE_COLOR)
        WINDOW.blit(play_again_text, (346, 302))
        main_menu_button = WINDOW.blit(BUTTON_IMAGE_1, (530, 300))
        main_menu_text = MENU_FONT.render('MAIN MENU', 1, WHITE_COLOR)
        WINDOW.blit(main_menu_text, (547, 302))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_again_button.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(BUTTON_IMAGE_1_ACT, (335, 300))
            play_again_text_act = MENU_FONT_ACT.render('PLAY AGAIN', 1, BLACK_COLOR)
            WINDOW.blit(play_again_text_act, (345, 301))
            if click:
                is_running = False
                game()

        if main_menu_button.collidepoint(mouse_x, mouse_y):
            WINDOW.blit(BUTTON_IMAGE_1_ACT, (530, 300))
            main_menu_text_act = MENU_FONT_ACT.render('MAIN MENU', 1, BLACK_COLOR)
            WINDOW.blit(main_menu_text_act, (546, 301))
            if click:
                is_running = False

        pygame.display.update()
    

if __name__ == "__main__":
    main_menu()