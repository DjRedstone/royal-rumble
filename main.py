import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.arrow)
running = True


def quitAction():
    global running
    running = False


buttons = []


class Button:
    def __init__(self, x, y, width, height, bg_color, text, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text = text
        self.action = action

    def addToScreen(self):
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        textPos = (
            self.x + (self.width - self.text.get_width()) / 2, self.y + (self.height - self.text.get_height()) / 2)
        screen.blit(self.text, dest=textPos)


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
    playButton = Button(screen.get_width() / 2 - 150 / 2, 250, 150, 75, (150, 150, 150),
                        getFont().render("Jouer", True, (255, 255, 255)), loadLobby)
    playButton.addToScreen()
    buttons.append(playButton)
    listHerosButton = Button(screen.get_width() / 2 - 275 / 2, 350, 275, 75, (150, 150, 150),
                             getFont().render("Liste des héros", True, (255, 255, 255)), lambda: print("WIP"))
    listHerosButton.addToScreen()
    buttons.append(listHerosButton)
    quitButton = Button(screen.get_width() / 2 - 150 / 2, 450, 150, 75, (150, 150, 150),
                        getFont().render("Quitter", True, (255, 255, 255)), quitAction)
    quitButton.addToScreen()
    buttons.append(quitButton)
    pygame.display.flip()


def loadLobby():
    screen.fill("white")
    userDeck = getFont(size=54).render("Votre deck", True, (0, 0, 0))
    userDeckPos = (screen.get_width() / 4 - userDeck.get_width() / 2, 75)
    screen.blit(userDeck, dest=userDeckPos)
    botDeck = getFont(size=54).render("Votre deck", True, (0, 0, 0))
    botDeckPos = (screen.get_width() - (screen.get_width() / 4 + botDeck.get_width() / 2), 75)
    screen.blit(botDeck, dest=botDeckPos)


loadMainPage()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            for button in buttons:
                clickPos = e.pos
                if button.x <= clickPos[0] <= (button.x + button.width) and button.y <= clickPos[1] <= (
                        button.y + button.height):
                    button.action()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
