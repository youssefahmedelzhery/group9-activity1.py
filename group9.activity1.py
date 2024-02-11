from turtle import Screen, Turtl

#student 1: yousef ahmed elzheiri
#student 2: khalid abdulkader
#student 3: mohamed gawi
 
wind = Screen()
wind.title("activity 1")
wind.bgcolor("light yellow")



def hexigon(turta, border_color, hexa_color):
    turta.penup()
    turta.setpos(-250, 250)
    turta.pendown()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.setheading(0)
    turta.end_fill()

    turta.penup()
    turta.setpos(-150, 150)
    turta.pendown()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.setheading(0)
    turta.end_fill()

    turta.penup()
    turta.setpos(-50, 50)
    turta.pendown()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.setheading(0)
    turta.end_fill()



def circle(turta, border_color, circle_color):
    turta.penup()
    turta.setpos(-100, 165)
    turta.pendown()
    turta.begin_fill()
    turta.color(circle_color)
    turta.pencolor(border_color)
    turta.circle(45)
    turta.end_fill()
    turta.setheading(0)
    

    turta.penup()
    turta.setpos(0, 65)
    turta.pendown()
    turta.begin_fill()
    turta.color(circle_color)
    turta.pencolor(border_color)
    turta.circle(45)
    turta.end_fill()
    turta.setheading(0)

    turta.penup()
    turta.setpos(100, -35)
    turta.pendown()
    turta.begin_fill()
    turta.color(circle_color)
    turta.pencolor(border_color)
    turta.circle(45)
    turta.end_fill()
    turta.setheading(0)

    

def square(turta, border_color, square_color):
    turta.penup()
    turta.setpos(0, 250)
    turta.pendown()
    turta.begin_fill()
    turta.color(square_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.color(square_color)
    turta.pencolor(border_color)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.end_fill()
    
    turta.penup()
    turta.setpos(100, 150)
    turta.pendown()
    turta.begin_fill()
    turta.color(square_color)
    turta.pencolor(border_color)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.end_fill()

    turta.penup()
    turta.setpos(200, 50)
    turta.pendown()
    turta.begin_fill()
    turta.color(square_color)
    turta.pencolor(border_color)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.end_fill()



def pattern(turta, hexa_color, circle_color, square_color, border_color):

    border_color = input("enter Border Color: ")
    hexa_color = input("enter Hexagon Color: ")
    square_color = input("enter Circle Color: ")
    circle_color = input("enter square Color: ")

    hexigon(turta, border_color, hexa_color)
    circle(turta, border_color, circle_color)
    square(turta, border_color, square_color)

    



def main():

    turta = Turtle()
    turta.pensize(4)

    pattern(turta, "hexa_color", "circle_color", "square_color", "border_color")

    wind.exitonclick()

    

    
main()
