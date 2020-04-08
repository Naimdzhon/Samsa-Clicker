import pygame, random, os

display_w = 800
display_h = 500
game_exit = False

background = pygame.image.load(os.path.join("images", "background(2).png"))
samsa_image = pygame.image.load(os.path.join("images", "samsa.png"))

background = pygame.transform.scale(background, (1000, 1000))
samsa_image = pygame.transform.scale(samsa_image, (200, 200))

cursor = pygame.image.load(os.path.join("images", "cursor.png"))
oven = pygame.image.load(os.path.join("images", "oven.png"))
factory = pygame.image.load(os.path.join("images", "factory.png"))

cursor = pygame.transform.scale(cursor, (45, 45))
oven = pygame.transform.scale(oven, (40, 40))
factory = pygame.transform.scale(factory, (40, 40))

costs = [25, 123, 828, 650]

samsa = 0

cursors = 0
ovens = 0
factories = 0

tmp = 0

last_cursor = 0
last_oven = 0
last_factory = 0
last_factory2 = 0

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Samsa-Clicker v0.1')
clock = pygame.time.Clock()


def process_mouse(event):
    global samsa, cursors, ovens, factories
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            samsa += 1
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if cursor.get_rect().move((520, 38)).collidepoint(pos):
            if samsa >= costs[0]:
                if cursors < 1242:
                    samsa -= costs[0]
                    cursors += 1
                    costs[0] += 8
        elif oven.get_rect().move((530, 78)).collidepoint(pos):
            if samsa >= costs[1]:
                if ovens < 1242:
                    samsa -= costs[1]
                    ovens += 1
                    costs[1] += 13
        elif factory.get_rect().move((510, 142)).collidepoint(pos):
            if samsa >= costs[2]:
                if cursors < 1242:
                    samsa -= costs[3]
                    factories += 1
                    costs[2] += 13


def draw_text(fontsize, text, coord):
    font = pygame.font.Font(r"C:\Windows\Fonts\Candara.ttf", fontsize)
    text_image = font.render(text, True, (255, 255, 255))
    game_display.blit(text_image, coord)


def draw_texts():
    global samsa, cursors, ovens, factories

    draw_text(30, "SAMSA:" + str(samsa), (70, 0))
    draw_text(25, "!CLICK IT!", (80, 33))

    draw_text(30, "SHOP:", (650, 0))
    draw_text(28, "CURSOR : " + str(costs[0]) + "S", (580, 38))
    draw_text(28, "OVEN : " + str(costs[1]) + "S", (600, 100))
    draw_text(28, "FACTORY : " + str(costs[2]) + "S", (580, 144))

    draw_text(28, "   " + str(cursors) + "PCS", (50, 326))
    draw_text(28, str(ovens) + "PCS", (58, 380))
    draw_text(28, str(factories) + "PCS", (58, 435))


def draw_shop():
    game_display.blit(cursor, (520, 30))
    game_display.blit(oven, (530, 90))
    game_display.blit(factory, (510, 140))


def draw_improvements():
    game_display.blit(cursor, (16, 310))
    game_display.blit(oven, (12, 368))
    game_display.blit(factory, (12, 432))


def game_loop(update_time):
    global game_exit, tmp, last_cursor, last_oven, \
        last_factory, last_factory2, samsa, cursors, factories
    while not game_exit:
        for event in pygame.event.get():
            process_mouse(event)
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.blit(background, (0, 0))

        if samsa % 4 == 0:
            game_display.blit(samsa_image, (8, 62))
        elif  samsa % 4 == 1:
            game_display.blit(samsa_image, (18, 62))
        elif samsa % 4 == 2 :
            game_display.blit(samsa_image, (18, 72))
        else :
            game_display.blit(samsa_image, (8, 72))

        draw_shop()
        draw_improvements()
        draw_texts()

        tmp += 1

        if tmp >= 1000:
            tmp = 0
            last_cursor = 0
            last_oven = 0
            last_factory = 0
            last_factory2 = 0
        if tmp >= last_cursor + 50:
            samsa += cursors
            last_cursor = tmp

        if tmp >= last_oven + 30:
            samsa += ovens
            last_oven = tmp

        if tmp >= last_factory + 18:
            samsa += factories
            last_factory = tmp

        if tmp >= last_factory2 + 30:
            last_factory2 = tmp

        pygame.display.update()
        clock.tick(update_time)


game_loop(30)
