#  The final project challenges us to write code in Reeborg's world to enable a robot to navigate through a maze and reach the goal, regardless of the maze's configuration. If you already have the link open, you can proceed; otherwise, click the direct link provided in the course resources to access Reeborg's world.

# In Reeborg's world, select the maze from the dropdown menu. Although the maze layout remains constant, the robot's starting position and facing direction are randomized each time the game restarts. For example, the robot might face up in one instance and down in another, starting at different locations within the maze.

# Understanding the Maze Navigation Strategy
# The secret to successfully navigating the maze is to have the robot follow the right edge of the maze. Starting anywhere within the maze, if the robot continuously follows the right wall, it will eventually reach the final destination.

# This approach is algorithmic rather than direct; the robot does not see the exit but follows a set of instructions to navigate.

# The algorithm hierarchy is as follows:

# If the right side is clear, turn right and move forward.
# If the right side is not clear but the front is clear, move forward.
# If neither right nor front is clear, turn left.
# This sequence guides the robot along the right edge of the maze.

# Implementing the Algorithm Using Python
# To implement this, you will use functions such as move(), turn_left(), and tests like front_is_clear(), right_is_clear(), and at_goal(). A while loop will allow the robot to continue executing instructions until it reaches the goal, and conditional statements (if, elif, else) will enforce the decision hierarchy.

left_turn = turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

