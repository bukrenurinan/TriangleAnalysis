import math
from math import acos, degrees
# a. First your code should get these 6 parameters from the user as floating-values.
vertex_x1=float(input("Enter the x-coordinate of the  vertex A of the triangle :"))
vertex_y1=float(input("Enter the y-coordinate of the  vertex A of the triangle :"))


vertex_x2=float(input("Enter the x-coordinate of the vertex B the triangle :"))
vertex_y2=float(input("Enter the y-coordinate of the vertex B the triangle :"))


vertex_x3=float(input("Enter the x-coordinate of the vertex C the triangle :"))
vertex_y3=float(input("Enter the y-coordinate of the vertex C the triangle :"))
print("------------------------------------------------------------------------------------------")
# Printing the coordinates of points A , B and C
print("A = (",vertex_x1,",",vertex_y1,")")
print("B = (",vertex_x2,",",vertex_y2,")")
print("C = (",vertex_x3,",",vertex_y3,")")
print("------------------------------------------------------------------------------------------")
# b. Then your code should determine and print the length of the sides.
sides_length=[] # Edge lengths are kept in this list
sides_name = [] # Edge names are kept in this list
AB = math.sqrt(((vertex_x2-vertex_x1)*(vertex_x2-vertex_x1))+((vertex_y2-vertex_y1)*(vertex_y2-vertex_y1))) # The formula for calculating the distance between two points whose coordinates are known is applied.
sides_length.append(AB)
sides_name.append("AB")

BC = math.sqrt(((vertex_x3-vertex_x2)*(vertex_x3-vertex_x2))+((vertex_y3-vertex_y2)*(vertex_y3-vertex_y2))) # The formula for calculating the distance between two points whose coordinates are known is applied.
sides_length.append(BC)
sides_name.append("BC")

AC = math.sqrt(((vertex_x3-vertex_x1)*(vertex_x3-vertex_x1))+((vertex_y3-vertex_y1)*(vertex_y3-vertex_y1))) # The formula for calculating the distance between two points whose coordinates are known is applied.
sides_length.append(AC)
sides_name.append("AC")

# Checks whether the given coordinates form a triangle
if (vertex_x1==vertex_x2 and vertex_y1==vertex_y2) and (vertex_x3==vertex_x1 and vertex_y3==vertex_y1): # Warns if the same point is entered 3 times
    print(" The entered coordinates represent a point ")

elif AB<=(BC+AC) and AB>= abs(BC-AC):

    # c. Then your script should determine and print the angles between the sides.

    A_angle = degrees(acos((AB * AB + BC * BC - AC * AC) / (2.0 * AB * BC)))  # https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
    print("Vertex A of triangle is :",A_angle,"degrees")
    B_angle = degrees(acos((AC * AC + AB * AB - BC * BC) / (2.0 * AC * AB)))  # https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
    print("Vertex B of triangle is :", B_angle,"degrees")
    C_angle = degrees(acos((BC * BC + AC * AC - AB * AB) / (2.0 * BC * AC)))  # https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
    print("Vertex C of triangle is :", C_angle,"degrees")
    print("------------------------------------------------------------------------------------------")
    # d. Then it should calculate the perimeter and area of this triangle.
    perimeter = 0 # Variable created to sum all edges
    for i in range(len(sides_length)):
        print("Length of side",sides_name[i],"is", sides_length[i]) # Edge lengths are printed
        perimeter += sides_length[i]  # d.Then it should calculate the perimeter of this triangle

    print("------------------------------------------------------------------------------------------")
    print("Perimeter of triangle is : ", perimeter) # Perimeter is printed

    half_of_perimeter = float(perimeter / 2)
    area = float(math.sqrt(half_of_perimeter))  # Area= square root( perimeter/2)
    for i in sides_length:
        area = area * float(math.sqrt((half_of_perimeter - i)))  # Area= square root( perimeter/2*((perimeter/2)- (1. side length ))*((perimeter/2)- (2. side length ))*((perimeter/2)- (3. side length )))

    print("Area of triangle is : ", area) # Area is printed

else:
    print("The entered coordinates cannot form a triangle ") #Warns if the entered variables do not form a triangle



