import pgzrun #getting pgzrun errors, no module??
from random import *
import time

#screen dimension variables
WIDTH = 800
HEIGHT = 600


#boolean variables
game_over = False
finalized = False
garden_happy = True

#time variables
time_elapsed = 0
start_time = time.time()


#actor variables
cow = Actor("cow")
cow.pos = (100, 500)


#list variables
flower_list = []
wilted_list = []

def draw():
  global game_over, time_elapsed, finalized
  if(not game_over):
    screen.clear()
    screen.blit("garden", (0,0))
    cow.draw()
    for flower in flower_list:
      flower.draw()
    time_elapsed = int(time.time() - start_time)
    screen.draw.text("Your garden was happy for: " + str(time_elapsed) + " seconds", topleft = (10, 10), color = "black")
  else:
    if(not finalized):
      cow.draw()
      screen.draw.text("Your garden was happy for: " + str(time_elapsed) + " seconds", topleft = (10, 10), color = "black")
      if(not garden_happy):
        screen.draw.text("GARDEN UNHAPPY; GAME OVER! >:(", topleft = (10, 50), color = "black")
        finalized = True

def new_flower():
  global flower_list, wilted_list
  flower_new = Actor("flower")
  flower_new.pos = (randint(50, WIDTH - 50), randint(150, HEIGHT - 100))
  flower_list.append(flower_new)
  wilted_list.append("happy")

def add_flowers():
  global game_over
  if(not game_over):
    new_flower()
    clock.schedule(add_flowers, 4)

def check_wilt_times():
  global wilted_list, game_over, garden_happy
  if(len(wilted_list) > 0):
    for wilted_since in wilted_list:
      if(not wilted_since == "happy"):
        time_wilted = int(time.time() - wilted_since)
        if(time_wilted > 10.0):
          garden_happy = False
          game_over = True
          break

def wilt_flower():
  global flower_list, wilted_list, game_over
  if(not game_over):
    if(len(flower_list) > 0):
      rand_flower = randint(0, len(flower_list) - 1)
      if(flower_list[rand_flower].image == "flower"):
        flower_list[rand_flower].image = "flower-wilt"
        wilted_list[rand_flower] = time.time
    clock.schedule(wilt_flower, 3)

def check_flower_collision():
  global cow, flower_list, wilted_list, game_over
  index = 0
  for flower in flower_list:
    if(flower.colliderect(cow) and flower.image == "flower-wilt"):
      flower.image = "flower"
      wilted_list[index] = "happy"
      break
    index = index + 1

def check_fangflower_collision():
    pass

def velocity():
    pass

def mutate():
    pass

def update_fangflowers():
    pass

def reset_cow():
  global game_over
  if(not game_over):
    cow.image = "cow"

def update():
  global game_over, time_elapsed
  check_wilt_times()
  if(not game_over):
    if(keyboard.space):
      cow.image = "cow-water"
      clock.schedule(reset_cow, 0.5)
      check_flower_collision()
    if(keyboard.left and cow.x > 0):
      cow.x -=5
    if(keyboard.right and cow.x < WIDTH):
      cow.x += 5
    if(keyboard.up and cow.y > 150):
      cow.y -= 5
    if(keyboard.down and cow.y < HEIGHT):
      cow.y += 5

add_flowers()
wilt_flower()
pgzrun.go()                         
                       
