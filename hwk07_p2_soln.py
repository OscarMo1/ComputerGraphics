import numpy as np
from hwk07_p1_soln import project

# NOTE: you do NOT need to rewrite the `project` function 
# as it is imported above

def rotate(x, y, z):
    """
    returns the matrix corresponding to first rotating a value 'x' 
    around the x-axis, 
    then rotating 'y' around the y-axis, 
    and then 'z' around the z-axis.   
    All angles are in radians. 
    The center of rotation is at point given by 'loc' 
    (3D homogeneous coord).
    These matrices obey the right-hand rule: 
    a positive rotation is counter-clockwise
    when looking along the axis of rotation 
    from the positive direction toward the origin.  
    """
    #reflect over x axis
    Rx = np.array([[1, 0, 0, 0],
                          [0, np.cos(x), -np.sin(x), 0],
                          [0, np.sin(x), np.cos(x), 0],
                          [0, 0, 0, 1]])
    Ry = np.array([[np.cos(y), 0, np.sin(y), 0],
                          [0, 1, 0, 0],
                          [-np.sin(y), 0, np.cos(y), 0],
                          [0, 0, 0, 1]])
    Rz = np.array([[np.cos(z), -np.sin(z), 0, 0],
                          [np.sin(z), np.cos(z), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
    final_rotate = Rz @ Ry @ Rx
    return final_rotate
    

def houseTransform2(i, loc):
    """
    returns the appropriate transformation matrix for the house.  
    The center of the house before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    p_matrix = project(100)
    p_matrix = p_matrix @ rotate(0, 2 * np.pi * i/150, 0)
    return p_matrix
