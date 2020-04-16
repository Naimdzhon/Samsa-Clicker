import pygame, random, os

display_w = 800
display_h = 500
game_exit = False

background = pygame.image.load("background.png")
samsa_image = pygame.image.load("samsa.png")

background = pygame.transform.scale(background, (1000, 1000))
samsa_image = pygame.transform.scale(samsa_image, (200, 200))

cursor = pygame.image.load(os.path.join("cursor.png"))
oven = pygame.image.load(os.path.join("oven.png"))
factory = pygame.image.load(os.path.join("factory.png"))

cursor = pygame.transform.scale(cursor, (45, 45))
oven = pygame.transform.scale(oven, (40, 40))
factory = pygame.transform.scale(factory, (40, 40))

shop = {cursor: (420, 30), oven: (430, 90), factory: (410, 140)}
improvements = {cursor: (16, 310), oven: (12, 368), factory: (12, 432)}

costs = [25, 123, 828]

samsa = 0

number = [0, 0, 0]  # number of cursors,ovens,factories

tmp = 0

last_cursor = 0
last_oven = 0
last_factory = 0
last_factory2 = 0

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Samsa-Clicker v0.1')
clock = pygame.time.Clock()


def buy(index):
    global samsa
    if samsa >= costs[index]:
        if number[index] < 1242:
            samsa -= costs[index]
            number[index] += 1
            costs[index] += 8 + index * 4


def Clicked_to(pos):
    index = 0
    for i in shop:
        if i.get_rect().move(shop[i]).collidepoint(pos):
            return index
        index += 1
    return -1


def process_mouse(event):
    global samsa

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            samsa += 1
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        index = Clicked_to(pos)
        if (index != -1):
            buy(index)


def draw_text(fontsize, text, coord):
    font = pygame.font.SysFont('arial', fontsize)
    text_image = font.render(text, True, (255, 255, 255))
    game_display.blit(text_image, coord)


def draw_texts():
    global samsa

    draw_text(30, "SAMSA:" + str(samsa), (70, 0))
    draw_text(25, "!CLICK IT!", (80, 33))

    draw_text(30, "SHOP:", (500, 0))
    draw_text(28, "CURSOR : " + str(costs[0]) + "S", (480, 38))
    draw_text(28, "OVEN : " + str(costs[1]) + "S", (500, 100))
    draw_text(28, "FACTORY : " + str(costs[2]) + "S", (460, 144))

    draw_text(28, "   " + str(number[0]) + "PCS", (50, 326))
    draw_text(28, str(number[1]) + "PCS", (58, 380))
    draw_text(28, str(number[2]) + "PCS", (58, 435))


def draw_shop():
    for i in shop:
        game_display.blit(i, shop[i])


def draw_improvements():
    for i in improvements:
        game_display.blit(i, improvements[i])


def game_loop(update_time):
    global game_exit, tmp, last_cursor, last_oven, \
        last_factory, last_factory2, samsa
    while not game_exit:
        for event in pygame.event.get():
            process_mouse(event)
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.blit(background, (0, 0))

        r = samsa % 4
        game_display.blit(samsa_image, (20 + 3 * r * (2 - r), 62 - 3 * r * (2 - r)))

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
            samsa += number[0]
            last_cursor = tmp

        if tmp >= last_oven + 30:
            samsa += number[1]
            last_oven = tmp

        if tmp >= last_factory + 18:
            samsa += number[2]
            last_factory = tmp

        if tmp >= last_factory2 + 30:
            last_factory2 = tmp

        pygame.display.update()
        clock.tick(update_time)


game_loop(30)
