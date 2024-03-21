import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import tkinter as tk
from tkinter import messagebox
import pygame
import random
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)

pygame.init()
pygame.mixer.init(channels = 2)

class Pileczka(object):
    def __init__(self, color, start, speed, dirnx, dirny, wsp, first_bounce):
        self.color = color
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.speed = speed
        self.wsp = wsp
        self.first_bounce = first_bounce
        self.wait_for_input = True

    def move(self, dirnx, dirny, speed, wsp, first_bounce, wait_for_input):
        self.dirnx = dirnx
        self.dirny = dirny
        self.speed = speed
        #               Lewy górny                          Prawy dolny                         Lewy dolny                          Prawy górny
        self.hitbox = ((self.pos[0] - 7, self.pos[1] - 7), (self.pos[0] + 7, self.pos[1] + 7), (self.pos[0] - 7, self.pos[1]+7), (self.pos[0] + 7, self.pos[1] - 7))
        self.wsp = wsp
        self.first_bounce = first_bounce
        moveup = (wsp/100)*dirny*speed
        movehorizontal = dirnx * speed
        if self.wait_for_input == False:
            if dirnx == 1 and (dirny == 1 or dirny == -1):
                self.pos = (self.pos[0] + movehorizontal, self.pos[1] + moveup)
            elif (dirnx == 1 or dirnx == -1) and dirny == 0:
                self.pos = (self.pos[0] + movehorizontal, self.pos[1])
            elif dirnx == -1 and (dirny == 1 or dirny == -1):
                self.pos = (self.pos[0] + movehorizontal, self.pos[1] + moveup)

            if self.hitbox[0][1] <= 0 or self.hitbox[1][1] >=720:
                if self.pos[1] <= 7:
                    self.pos = (self.pos[0], 8)
                elif self.pos[1] >= 713:
                    self.pos = (self.pos[0], 712)
                self.dirny = -self.dirny

            bounce_sound_path = "assets\sound\ " + str(speed) + ".mp3"
            bounce_sound_path = bounce_sound_path.replace(" ", "")
            sound = pygame.mixer.Sound(bounce_sound_path)
            if self.first_bounce == True:
                if (self.hitbox[0][0] <= 40 and self.hitbox[0][0] >= 30) and (self.pos[1] >= palet1.hitbox_palet1[0][1] and self.pos[1] <= palet1.hitbox_palet1[1][1]):
                    channel2.play(sound)
                    point = self.pos[1]
                    middle1 = palet1.palet1_pos[1] + 50
                    self.wsp = (middle1 - point)*2
                    if self.wsp <0:
                        self.dirny = 1
                        self.wsp = -self.wsp
                        self.first_bounce = False
                    elif self.wsp >0:
                        self.dirny = -1
                        self.first_bounce = False
                    else:
                        self.wsp = 1
                        self.dirny = 1
                        self.first_bounce = False

                    if not self.speed >= 10:
                        self.speed = self.speed + 0.5

                    self.pos = (48, self.pos[1])
                    self.dirnx = (-1)*self.dirnx

                elif (self.hitbox[1][0] >= 1240 and self.hitbox[1][0] <= 1250) and (self.pos[1] >= palet1.hitbox_palet2[0][1] and self.pos[1] <= palet1.hitbox_palet2[1][1]):
                    channel2.play(sound)
                    point = self.pos[1]
                    middle2 = palet1.palet2_pos[1] + 50
                    self.wsp = (middle2 - point)*2
                    if self.wsp <0:
                        self.dirny = 1
                        self.wsp = -self.wsp
                        self.first_bounce = False
                    elif self.wsp >0:
                        self.dirny = -1
                        self.first_bounce = False
                    else:
                        self.wsp = 1
                        self.dirny = -1
                        self.first_bounce = False

                    if not self.speed >= 10:
                        self.speed = self.speed + 0.5

                    self.dirnx = (-1) * self.dirnx
                    self.pos = (1232, self.pos[1])
            else:
                if (self.hitbox[0][0] <= 40 and self.hitbox[0][0] >= 25) and (self.pos[1] >= palet1.hitbox_palet1[0][1] and self.pos[1] <= palet1.hitbox_palet1[1][1]):
                    channel2.play(sound)

                    if palet1.moving_p1up == True and self.wsp < 85:
                        self.wsp = self.wsp + 15
                    elif palet1.moving_p1down == True and self.wsp > 15:
                        self.wsp = self.wsp - 15

                    if not self.speed >= 10:
                        self.speed = self.speed + 0.5

                    self.pos = (48, self.pos[1])
                    self.dirnx = (-1)*self.dirnx

                elif (self.hitbox[1][0] >= 1240 and self.hitbox[1][0] <= 1255) and (self.pos[1] >= palet1.hitbox_palet2[0][1] and self.pos[1] <= palet1.hitbox_palet2[1][1]):
                    channel2.play(sound)

                    if palet1.moving_p2up == True and self.wsp < 85:
                        self.wsp = self.wsp + 15
                    elif palet1.moving_p2down == True and self.wsp > 15:
                        self.wsp = self.wsp - 15

                    if not self.speed >= 10:
                        self.speed = self.speed + 0.5

                    self.pos = (1232, self.pos[1])
                    self.dirnx = (-1)*self.dirnx
        else:
            if ((palet1.moving_p1up == True or palet1.moving_p1down == True) and self.dirnx == -1)or ((palet1.moving_p2up == True or palet1.moving_p2down == True) and self.dirnx == 1):
                self.wait_for_input = False

    def draw_ball(self, surface):
        radius = 7
        pygame.draw.circle(surface, self.color, self.pos, radius)

class Palet1(object):
    def __init__(self, color, start, start2):
        self.color = color
        self.palet1_pos = start
        self.palet2_pos = start2
        self.hitbox_palet1 = ((self.palet1_pos[0], self.palet1_pos[1]), (self.palet1_pos[0] + 10, self.palet1_pos[1] + 100))
        self.hitbox_palet2 = ((self.palet2_pos[0], self.palet2_pos[1]), (self.palet2_pos[0] + 10, self.palet2_pos[1] + 100))
        self.moving_p1up = False
        self.moving_p1down = False
        self.moving_p2up = False
        self.moving_p2down = False

    def move(self, moving_p1up, moving_p1down, moving_p2up, moving_p2down):
        self.hitbox_palet1 = ((self.palet1_pos[0], self.palet1_pos[1]), (self.palet1_pos[0] + 10, self.palet1_pos[1] + 100))
        self.hitbox_palet2 = ((self.palet2_pos[0], self.palet2_pos[1]), (self.palet2_pos[0] + 10, self.palet2_pos[1] + 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win32gui.ShowWindow(the_program_to_hide, win32con.SW_SHOW)
                exit()

        keys = pygame.key.get_pressed()
        palet1_speed = 6
        if keys[pygame.K_w]:
            if not self.palet1_pos[1] <= 0:
                self.moving_p1up = True
                self.palet1_pos = (self.palet1_pos[0], self.palet1_pos[1] - palet1_speed)
            else:
                self.moving_p1up = False
        elif keys[pygame.K_s]:
            if not self.palet1_pos[1] + 100 >= 720:
                self.moving_p1down = True
                self.palet1_pos = (self.palet1_pos[0], self.palet1_pos[1] + palet1_speed)
            else:
                self.moving_p1down = False
        else:
            self.moving_p1up = False
            self.moving_p1down = False
        if keys[pygame.K_UP]:
            if not self.palet2_pos[1] <= 0:
                self.moving_p2up = True
                self.palet2_pos = (self.palet2_pos[0], self.palet2_pos[1] - palet1_speed)
            else:
                self.moving_p2up = False
        elif keys[pygame.K_DOWN]:
            if not self.palet2_pos[1] + 100 >= 720:
                self.moving_p2down = True
                self.palet2_pos = (self.palet2_pos[0], self.palet2_pos[1] + palet1_speed)
            else:
                self.moving_p2down = False
        else:
            self.moving_p2up = False
            self.moving_p2down = False


    def draw_palet1(self, surface):
        palet1_posx = self.palet1_pos[0]
        palet1_posy = self.palet1_pos[1]
        pygame.draw.rect(surface, self.color, (palet1_posx, palet1_posy, 10, 100))

    def draw_palet2(self, surface):
        palet2_posx = self.palet2_pos[0]
        palet2_posy = self.palet2_pos[1]
        pygame.draw.rect(surface, self.color, (palet2_posx, palet2_posy, 10, 100))

class button(object):
    def __init__(self, pos, color, main_menu):
        self.pos = pos
        but_x = self.pos[0]
        but_y = self.pos[1]
        #               Lewy górny                  Lewy dolny                  Prawy górny                 Prawy dolny
        self.box = ((but_x - 128, but_y - 72), (but_x - 128, but_y + 72), (but_x + 128, but_y - 72), (but_x + 128, but_y + 72))
        self.color = color
        self.color2 = (150, 150, 150)
        self.main_menu = main_menu

    def work(self, main_menu):
        self.main_menu = main_menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win32gui.ShowWindow(the_program_to_hide, win32con.SW_SHOW)
                exit()

            mousepos = pygame.mouse.get_pos()

            if (mousepos[0] >= 512 and mousepos[1] >= 288) and (mousepos[1] <= 432 and mousepos[0] <= 768):
                self.color = (100, 100, 100)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.main_menu = False
            elif (mousepos[0] >= 512 and mousepos[1] >= 532) and (mousepos[1] <= 676 and mousepos[0] <= 768):
                self.color2 = (100, 100, 100)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    win32gui.ShowWindow(the_program_to_hide, win32con.SW_SHOW)
                    exit()
            else:
                self.color = (150, 150, 150)
                self.color2 = (150, 150, 150)

    def draw_button(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (512, 288, 256, 144))
        pygame.draw.rect(surface, self.color, (522, 298, 236, 124))

    def draw_button2(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (512, 532, 256, 144))
        pygame.draw.rect(surface, self.color2, (522, 542, 236, 124))

class Strzalka(object):
    def __init__(self, pos, color):
        self.start_pos = pos
        self.color = color

    def draw(self, surface):
        ax = self.start_pos[0]
        ay = self.start_pos[1]
        if ball.dirnx == -1:
            pygame.draw.lines(surface, self.color, True, [(ax, ay), (ax-100, ay), (ax - 100, ay-50), (ax-200, ay+50), (ax-100, ay+150), (ax-100, ay+100), (ax, ay+100)], width = 3)
        else:
            pygame.draw.lines(surface, self.color, True, [(ax, ay), (ax+100, ay), (ax + 100, ay-50), (ax+200, ay+50), (ax+100, ay+150), (ax+100, ay+100), (ax, ay+100)], width = 3)

def punkt():
    if ball.pos[0] >= 1287:
        ball.first_bounce = True
        ball.wait_for_input = True
        ball.dirnx = 1
        ball.dirny = 0
        ball.wsp = 0
        ball.speed = 3
        palet1.palet1_pos = (20, 310)
        palet1.palet2_pos = (1250, 310)
        ball.pos = (640, 360)
    elif ball.pos[0] <= -7:
        ball.first_bounce = True
        ball.wait_for_input = True
        ball.dirnx = -1
        ball.dirny = 0
        ball.wsp = 0
        ball.speed = 3
        ball.pos = (640, 360)
        palet1.palet1_pos = (20, 310)
        palet1.palet2_pos = (1250, 310)

def draw_screen_menu(surface):
    Button.draw_button(surface)
    Button.draw_button2(surface)
    Title_Font = pygame.font.SysFont("Times New Roman", 70, False, False)
    Font = pygame.font.SysFont("Times New Roman", 30, False, False)
    Font2 = pygame.font.SysFont("Times New Roman", 20, False, False)
    Title_Text = Title_Font.render("Pong", True, (255, 255, 255))
    Text = Font.render("Play", True, (0, 0, 0))
    Text2 = Font.render("Exit", True, (0, 0, 0))
    Text3 = Font2.render("Autor: Piotr Wieczorkiewicz", True, (255, 255, 255))
    pygame.draw.rect(surface, (0, 0, 0), (512, 0, 256, 144))
    pygame.draw.rect(surface, (0, 0, 75), (522, 0, 236, 134))
    window.blit(Title_Text, (565, 10))
    window.blit(Text, (615, 340))
    window.blit(Text2, (615, 590))
    window.blit(Text3, (1043, 700))
    pygame.display.update()

def draw_screen(surface):
    surface.fill((0, 0, 100))
    ball.draw_ball(surface)
    palet1.draw_palet1(surface)
    palet1.draw_palet2(surface)
    if ball.wait_for_input == True and ball.dirnx == -1:
        arrow1.draw(surface)
    elif ball.wait_for_input == True and ball.dirnx == 1:
        arrow2.draw(surface)
    else:
        pass
    Font = pygame.font.SysFont("Times New Roman", 20, False, False)
    Text = Font.render("Player A: " + str(score_A) + "      Player B: " + str(score_B), True, (255, 255, 255))
    window.blit(Text, (540, 0))
    pygame.display.update()

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", 1)
    root.withdraw()
    messagebox.showinfo(subject, content)

    try:
        root.destroy()
    except:
        pass

def main():
    global x, y, speed, ball, palet1, palet2, window, score_A, score_B, first_bounce, move, channel1, channel2, music, Button, main_menu, arrow1, arrow2
    score_A = 0
    score_B = 0
    x = 1280
    y = 720
    speed = 3
    score_limit = 10
    main_menu = True
    music = pygame.mixer.Sound("assets\sound\Pixel Miner.mp3")
    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
    channel2.set_volume(50)
    channel1.play(music)
    channel1.set_volume(5)
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Pong")
    pygame.display.set_icon(pygame.image.load("assets/visuals/Icon.png"))

    dirnx_los = 0
    while dirnx_los ==0:
        dirnx_los = random.randint(-1, 1)

    dirny =0
    wsp = 0
    first_bounce = True
    ball = Pileczka((255, 255, 255), (640, 360), speed, dirnx_los, dirny, wsp, first_bounce)
    palet1 = Palet1((255, 255, 255), (20, 310), (1250, 310))
    Button = button((640,360), (150, 150, 150), main_menu)
    arrow1 = Strzalka((300,310),(255, 255, 255))
    arrow2 = Strzalka((980, 310), (255, 255, 255))
    running = True
    menu_bg = pygame.image.load("assets/visuals/menu_bg.jpg")
    menu_bg_top = window.get_height() - window.get_height()
    menu_bg_left = window.get_width() / 2 - window.get_width() / 2

    while running:

        if Button.main_menu == True:
            Button.work(Button.main_menu)
            clock.tick(60)
            window.blit(menu_bg, (menu_bg_left, menu_bg_top))
            draw_screen_menu(window)
        else:
            clock.tick(60)
            ball.move(ball.dirnx, ball.dirny, ball.speed, ball.wsp, ball.first_bounce, ball.wait_for_input)
            palet1.move(palet1.moving_p1up, palet1.moving_p1down, palet1.moving_p2up, palet1.moving_p2down)
            if ball.pos[0] >= 1287:
                score_A+=1
            elif ball.pos[0] <= -7:
                score_B+=1

            draw_screen(window)
            if score_A == score_limit or score_B == score_limit:
                if score_A > score_B:
                    player = "Player A"
                else:
                    player = "Player B"
                content = player + " wins!"
                message_box("Congratulations", content)
                score_A = 0
                score_B = 0
                Button.main_menu = True

            punkt()


main()
