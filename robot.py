

#Decompose into functions
    
def move_square(size,degrees):
    
    print("Moving in a square of size "+str(size))
    for i in range(4):
        
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
        """This prints the information about moving in a square,ranges for 4 times, the parameters
        are size,degrees"""


def move_rectangle(length, width, degrees):  
    
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
        """ It concentrates  on the rectangle checking the length,
        width,degrees,then ranges for 2 times"""
    

def move_circle():    
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        """this prints out moving in the circle and ranges it for 360 times"""


def move_square_dancing(size, length, degrees):    
    print("Square dancing - 3 squares of size 20")
    size += 10
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(size, degrees) 
        """It prints the square_dancing which is supposed to be printed 3 times under
        square dancing with the size of 20
         ,the +=10 adds so that it gives the correct size which is 20""" 


def move_crop_circles(length):
    print("Crop circles - 4 circles")
    
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()
        """it prints circle 4 times under Crop circles adding the parameter length
        which is 20"""


def move():

    size = 10
    degrees = 90
    length = 20
    width = 10
    move_square(size, degrees)
    move_rectangle(length, width, degrees)
    move_circle()
    move_square_dancing(size, length, degrees)
    move_crop_circles(length)
    

def robot_start():
    move()
    """Descriptive name would be: moving_shapes,because the program basically moves shapes,
    and prints shapes"""
    

if __name__ == "__main__":
    robot_start()
