import pygame
import random
from random import randint

#The idea of the game is to collect coins while avoiding monsters.
#The game was part of the course Advanced Programming.

def peli():
    pygame.init()
    score = 0
    naytto = pygame.display.set_mode((640, 480))
    fontti = pygame.font.SysFont("Arial", 24)
    teksti = fontti.render(f"Pisteet: {score}", True, (255, 0, 0))

#HAHMOT
    class Robo:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Kolikko:

        def __init__(self, kolikko_x: int, kolikko_y: int, kolikko_speed: float):
            self.x = kolikko_x
            self.y = kolikko_y
            self.speed = kolikko_speed

    class Hirvio:

        def __init__(self, hirvio_x: int, hirvio_y: int, hirvio_speed: float):
            self.x = hirvio_x
            self.y = hirvio_y
            self.speed = hirvio_speed

#KUVAT
    kolikko = pygame.image.load("kolikko.png")
    robo = pygame.image.load("robo.png")
    hirvio = pygame.image.load("hirvio.png")

#Hahmojen spawnaus
    robo1 = Robo(0, 480-robo.get_height())
    kolikko1 = Kolikko(randint(0,640-kolikko.get_width()),-randint(100,1000), 1)
    kolikko2 = Kolikko(randint(0,640-kolikko.get_width()),-randint(100,1000), 1)
    hirvio1 = Hirvio(randint(0,640-hirvio.get_width()),-randint(100,1000), 1)
    hirvio2 = Hirvio(randint(0,640-hirvio.get_width()),-randint(100,1000), 1)

#Muuta
    oikealle = False
    vasemmalle = False
    ylos = False
    alas = False

    kello = pygame.time.Clock()

#Itse ohjelma
    while True:
    #Robon liikkeet nuolilla
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    alas = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    alas = False
            else:
                robo1.x, robo1.y = robo1.x, robo1.y

            if tapahtuma.type == pygame.QUIT:
                exit()
    #ROBON LIIKKEET: vauhti ja seinät
        if (oikealle) and (robo1.x <= (640-robo.get_width())) and (robo1.x >= 0):
            robo1.x += 2
        elif robo1.x >= 640-robo.get_width():
            robo1.x = 640-robo.get_width()
        elif robo1.x <= 0:
            robo1.x = 0
        if (vasemmalle) and (robo1.x <= (640-robo.get_width())) and (robo1.x >= 0):
            robo1.x -= 2
        if (ylos) and (robo1.y >= 0) and (robo1.y <= (480-robo.get_height())):
            robo1.y -= 2
        elif robo1.y >= 480-robo.get_height():
            robo1.y = 480-robo.get_height()
        elif robo1.y <= 0:
            robo1.y = 0
        if (alas) and (robo1.y >= 0) and (robo1.y <= (480-robo.get_height())):
            robo1.y += 2

    #KOLIKOIDEN LIIKKEET

        kolikko1.y = kolikko1.y + kolikko1.speed
        if kolikko1.y > 480:
            kolikko1.x= random.randrange(0, 640)
            kolikko1.y = random.randrange(-150, -50)

        kolikko2.y = kolikko2.y + kolikko2.speed
        if kolikko2.y > 480:
            kolikko2.x= random.randrange(0, 640)
            kolikko2.y = random.randrange(-300, -150)

    #Saat pisteen per kolikko
        if (kolikko1.x in range(robo1.x - 20, robo1.x + 20)) and (kolikko1.y in range(robo1.y - 20, robo1.y + 20)):
            score += 1
            kolikko1.x= random.randrange(0, 640)
            kolikko1.y = random.randrange(-150, -50)

        if (kolikko2.x in range(robo1.x - 20, robo1.x + 20)) and (kolikko2.y in range(robo1.y - 20, robo1.y + 20)):
            score += 1
            kolikko2.x= random.randrange(0, 640)
            kolikko2.y = random.randrange(-300, -150)
    
    #HIRVIOIDEN LIIKKEET

        hirvio1.y = hirvio1.y + hirvio1.speed
        if hirvio1.y > 480:
            hirvio1.x= random.randrange(0, 640)
            hirvio1.y = random.randrange(-150, -50)

        hirvio2.y = hirvio2.y + hirvio2.speed
        if hirvio2.y > 480:
            hirvio2.x= random.randrange(0, 640)
            hirvio2.y = random.randrange(-300, -150)

    #Jos osut hirvioon peli alkaa alusta
        if (hirvio1.x in range(robo1.x - 20, robo1.x + 20)) and (hirvio1.y in range(robo1.y - 20, robo1.y + 20)):
            peli()

        if (hirvio2.x in range(robo1.x - 20, robo1.x + 20)) and (hirvio2.y in range(robo1.y - 20, robo1.y + 20)):
            peli()
            
        teksti = fontti.render(f"Pisteet: {score}", True, (255, 0, 0))
        naytto.fill((126, 0, 126))
        naytto.blit(robo, (robo1.x, robo1.y))
        naytto.blit(kolikko, (kolikko1.x, kolikko1.y))
        naytto.blit(kolikko, (kolikko2.x, kolikko2.y))
        naytto.blit(hirvio, (hirvio1.x, hirvio1.y))
        naytto.blit(hirvio, (hirvio2.x, hirvio2.y))
        naytto.blit(teksti, (550, 0))
        pygame.display.flip()

        kello.tick(60)

if __name__ == "__main__":
    peli()