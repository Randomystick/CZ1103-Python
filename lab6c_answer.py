
#Exerise 7c
from sense_hat import SenseHat 
from time import sleep 
from time import time

sense = SenseHat() 
sense.clear() 

def move_marble(pitch,roll,x,y): 
  new_x = x 
  new_y = y 
  if 1 < pitch < 179 and x != 0: 
     new_x -= 1 
  elif 359 > pitch > 179 and x != 7 : 
     new_x += 1 
     
  if 1 < roll < 179 and y != 7: 
     new_y += 1 
  elif 359 > roll > 179 and y != 0 : 
     new_y -= 1

  return new_x,new_y 
  
r=(0,0,0)
b=(0,0,0)
w=(255,255,255)

board = [[b,b,b,b,b,b,b,b], 
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b], 
         [b,b,b,b,b,b,b,b] ]



game_over = False
x=2
y=2

while not game_over:
    pitch = sense.get_orientation()['pitch'] 
    roll = sense.get_orientation()['roll'] 
#    print("pitch {0} roll {1}".format(round(pitch,0), round(roll,0)))
    x,y = move_marble(pitch,roll,x,y) 
#    print(x,y)
    board[y][x] = w
    sense.set_pixels(sum(board,[])) 
    sleep(0.05) 
    board[y][x] = b
