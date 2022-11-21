import pygame
import sys

pygame.init()

SAMPLE_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

every_word = SAMPLE_TEXT.split()

white = (255,255,255)
font = ("arial", 25)
update = 0

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Words")


running = True

while running:
    update += 1
    win.fill((0,0,0))


    win.blit(every_word[update],(22,0))

    for eve in pygame.event.get():
      if eve.type==pygame.QUIT:
         pygame.quit()
         sys.exit()

    pygame.display.update()
    pygame.time.delay(100)

