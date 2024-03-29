from turtle import *
from time import sleep

colormode(255)
red=(223,35,35)
green=(75,183,75)
yellow=(252,210,9)
blue=(86,146,195)
r=120
speed(2)#turtle speed
seth(-150)#angle
up()#directions
#The Red Petal
color(red)
begin_fill()
fd(r)
down()
right(90)
circle(-r,120)
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
end_fill()
#The Green Petal
left(180)
color(green)
begin_fill()
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
left(180)
circle(-r,120)
end_fill()
#The Yellow Petal
left(180)
circle(r,120)
color(yellow)
begin_fill()
circle(r,120)
right(180)
fd(r*3**.5)
right(60)
circle(-2*r,120)
right(120)
fd(r*3**.5)
end_fill()
#The Blue Disk
up()
left(90)
fd(r/20)
seth(60)
color(blue)
down()
begin_fill()
circle(distance(0,0))
end_fill()
ht()
sleep(5)#5 Seconds
