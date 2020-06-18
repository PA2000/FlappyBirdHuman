import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.font.init()
import time
import random
from Bird import Bird
from Pipe import Pipe
from Base import Base

#set window parameters
winWidth = 500
windHeight = 800
#load background
bgImg = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
#font for score
font = pygame.font.SysFont('calibri', 50)

def drawWindow(win, bird, pipes, base, score):
   win.blit(bgImg, (0, 0))
   bird.draw(win)
   for pipe in pipes:
      pipe.draw(win)
   base.draw(win)
   text = font.render("Score: " + str(score), 1, (255, 255, 255))
   win.blit(text, (winWidth - 10 - text.get_width(), 10))
   pygame.display.update()

def main():
   run = True
   while run:
      bird = Bird(230, 350)
      base = Base(700)
      pipes = [Pipe(730)]
      win = pygame.display.set_mode((winWidth, windHeight))
      pygame.display.set_caption("Padmank's Flappy Bird")
      clock = pygame.time.Clock()
      score = 0

      alive, paused = True, False
      while alive:
         clock.tick(30)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run, alive = False, False
               pygame.quit()
               quit()
               break
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                  run, alive = False, False
                  pygame.quit()
                  quit()
                  break
               if event.key == pygame.K_SPACE:
                  bird.jump()
               if event.key == pygame.K_r:
                  main()
         
         if not paused:
            bird.move()

            addPipe = False
            removePipes = []
            for pipe in pipes:
               if pipe.collide(bird):
                  paused = True
               if pipe.x + pipe.topPipe.get_width() < 0: #if pipe is off the screen completely
                  removePipes.append(pipe)
               if not pipe.passed and pipe.x < bird.x:
                  pipe.passed = True
                  addPipe = True
               pipe.move()
            if addPipe:
               score += 1
               pipes.append(Pipe(600))
            for r in removePipes:
               pipes.remove(r)

            if bird.y + bird.img.get_height() >= 730:
               paused = True

            base.move()
            drawWindow(win, bird, pipes, base, score)
   #pygame.quit()
   #quit()
   

if __name__ == "__main__":
    main()









