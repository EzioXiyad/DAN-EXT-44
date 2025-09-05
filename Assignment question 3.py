!pip install mobilechelonian

from mobilechelonian import Turtle

def draw_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3
        draw_edge(t, segment, depth-1)
        t.left(60)
        draw_edge(t, segment, depth-1)
        t.right(120)
        draw_edge(t, segment, depth-1)
        t.left(60)
        draw_edge(t, segment, depth-1)


def draw_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(t, length, depth)
        t.right(angle)

def main():
    
    sides = int(input("Enter the number of sides: "))
    length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

 
    t = Turtle()
    t.color = "blue"   
    t.speed(10)        

    t.penup()
    t.left(90)
    t.backward(length / 2)
    t.right(90)
    t.pendown()

    draw_polygon(t, sides, length, depth)

if __name__ == "__main__":
    main()
