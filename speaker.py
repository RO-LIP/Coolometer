import pygame


class speaker:
    def __init__(self,fileName):
        pygame.mixer.init()
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.set_volume(1.0)
    
    def playSound(self):
        pygame.mixer.music.play()
    