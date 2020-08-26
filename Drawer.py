import turtle

wn = turtle.Screen()
wn.title("drawer")
wn.setup(800, 600)
wn.bgcolor("black")
wn.tracer(0)



tut = turtle

move = tut.Turtle()
move.color("blue")
    
def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")



wn.listen()




#Main loop

while True :
    wn.update()
