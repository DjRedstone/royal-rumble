import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


def createButton(x, y, width, height, bg_color, text):
    pygame.draw.rect(screen, bg_color, (x - width / 2, y - height / 2, width, height))
    textPos = (x-text.get_width()/2, y-text.get_height()/2)
    screen.blit(text, dest=textPos)


def getFont(size=36, font=None):
    if font is None:
        return pygame.font.SysFont("Papyrus", size)
    elif font == "default":
        return pygame.font.Font(pygame.font.get_default_font(), size)


def loadMainPage():
    screen.fill("white")
    title = getFont(size=72).render("Royal Rumble", True, (0, 0, 0))
    titlePos = (screen.get_width() / 2 - title.get_width() / 2, 50)
    screen.blit(title, dest=titlePos)
    createButton(screen.get_width() / 2, 250, 150, 75, (150, 150, 150),
                 getFont().render("Jouer", True, (255, 255, 255)))
    createButton(screen.get_width() / 2, 350, 275, 75, (150, 150, 150),
                 getFont().render("Liste des héros", True, (255, 255, 255)))
    createButton(screen.get_width() / 2, 450, 150, 75, (150, 150, 150),
                 getFont().render("Quitter", True, (255, 255, 255)))
    pygame.display.flip()


loadMainPage()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
