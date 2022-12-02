import pygame
import sys
import time
import text

pygame.init()

SAMPLE_TEXT = text.returnText()

every_word = SAMPLE_TEXT.split()

white = (255, 255, 255)
font = pygame.font.Font(None, 100)
update = 0

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Words")

def initialWait(update):
  if update == 0:
      win.blit(currentWord, text_rect)
      pygame.display.update()
      time.sleep(3)


running = True

while running:
    
    win.fill((0, 0, 0))

    currentWord = font.render(every_word[update], True, white)
    text_rect = currentWord.get_rect(center=(WIDTH/2, HEIGHT/2))

    initialWait(update)

    win.blit(currentWord, text_rect)

    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()

    if every_word[update][-1] == ".":
      pygame.time.delay(200)
    else:
      pygame.time.delay(110)

    update += 1