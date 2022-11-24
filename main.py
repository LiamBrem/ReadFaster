import pygame
import sys
import time

pygame.init()

SAMPLE_TEXT = """Mr. and Mrs. Dursley, of number four, Privet Drive, were
proud to say that they were perfectly normal, thank
you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't
hold with such nonsense.
Mr. Dursley was the director of a firm called Grunnings, which
made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin
and blonde and had nearly twice the usual amount of neck, which
came in very useful as she spent so much of her time craning over
garden fences, spying on the neighbors. The Dursleys had a small
son called Dudley and in their opinion there was no finer boy
anywhere."""

every_word = SAMPLE_TEXT.split()

white = (255, 255, 255)
font = pygame.font.Font(None, 100)
update = 0

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Words")


running = True

while running:
    

    win.fill((0, 0, 0))

    currentWord = font.render(every_word[update], True, white)
    text_rect = currentWord.get_rect(center=(WIDTH/2, HEIGHT/2))

    if update == 0:
      win.blit(currentWord, text_rect)
      pygame.display.update()
      time.sleep(3)

    win.blit(currentWord, text_rect)

    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()

    if every_word[update][-1] == ".":
      pygame.time.delay(190)
    else:
      pygame.time.delay(110)

    update += 1

