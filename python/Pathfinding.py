import random
xc = int(input("What is the desired x position: "))
yc = int(input("What is the desired y position: "))
x = 0
y = 0
times = 0
movement = []
directions = ["left"], ["right"], ["up"], ["down"]
while True:
  while len(movement) != abs(xc) + abs(yc):
   movement += random.choice(directions)
   if movement[times] == "left":
     x -= 1
   elif movement[times] == "right":
     x += 1
   elif movement[times] == "up":
     y += 1
   elif movement[times] == "down":
     y -= 1
   times += 1
  if x == xc and y == yc:
    print(movement)
    break
  else:
    times = 0
    movement = []
    x, y = 0, 0