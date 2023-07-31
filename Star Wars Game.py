#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#First Part:

import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Star Wars Game")
window.bgcolor("black")

window.tracer(0)

vertex = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
window.register_shape("player", vertex)

asVertex = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("stone", asVertex)

####################
# Second Part:


class user(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.speed(0)
        self.penup()


def user1(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    cal = math.atan2(y1 - y2, x1 - x2)
    cal = cal * 180.0 / 3.14159
    
    return cal


player = user()
player.color("white")
player.shape("player")
player.score = 0

####################
#Third Part

missiles = []
for _ in range(3):
    missile = user()
    missile.color("red")
    missile.shape("arrow")
    missile.speed = 1
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)

pen = user()
pen.color("white")
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0", False, align = "center", font = ("Arial", 24, "normal"))

####################
# Fourth Part


stones = []

for _ in range(5):   
    stone = user()
    stone.color("brown")
    stone.shape("arrow")

    stone.speed  = random.randint(2, 3)/50
    stone.goto(0, 0)
    cal = random.randint(0, 260)
    distance = random.randint(300, 400)
    stone.setheading(cal)
    stone.fd(distance)
    stone.setheading(user1(player, stone))
    stones.append(stone)

####################
#Functions for Defence Part

def left_turn():
    player.lt(20)
    
def right_turn():
    player.rt(20)
    
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break


window.listen()
window.onkey(left_turn, "Left")
window.onkey(right_turn, "Right")
window.onkey(fire_missile, "space")

####################
#Functioning the Code Part-1

winner = False
while True:

    window.update()
    player.goto(0, 0)
    

    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "ready"

    for stone in stones:    
        stone.fd(stone.speed)
        
        for missile in missiles:
            if stone.distance(missile) < 20:
                cal = random.randint(0, 260)
                distance = random.randint(600, 800)
                stone.setheading(cal)
                stone.fd(distance)
                stone.setheading(user1(player, stone))
                stone.speed += 0.01
                
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"
                
                player.score += 10
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))

        ####################
        # Functioning the Code Part-2

        if stone.distance(player) < 20:
            cal = random.randint(0, 260)
            distance = random.randint(600, 800)
            stone.setheading(cal)
            stone.fd(distance)
            stone.setheading(user1(player, stone))
            stone.speed += 0.005
            winner = True
            player.score -= 30
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))
    if winner == True:
        player.hideturtle()
        missile.hideturtle()
        for a in stones:
            a.hideturtle()
        pen.clear()
        break

window.mainloop()







