#Snake.py
import turtle

def drawSnake(rad,angle,len,neckrad):#！debug：neckrad report sth wrong。
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(fd)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)#turtle.setup(width,height,startx,starty)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)#turtle.seth(angle),StandardMode:0 is to east in the right hand,90 is to north in upword.LogoMode:0 to north,90 to east.
    drawSnake(40,80,5,pythonsize/2)

main ()


