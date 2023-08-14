import numpy as np
from hwk07_p2_soln import project, rotate

# NOTE: you do NOT need to rewrite the `project` or `rotate` functions 
# as they are imported above

def moveTo(start, end):
    """
    returns the matrix corresponding to moving an obj 
    from position 'start' to position 'end.'
    positions are given in 3D homogeneous coordinates.
    """
    
    p_matrix = np.array([[1, 0, 0,(end[0]-start[0])],
                        [0, 1, 0, (end[1]-start[1])], 
                        [0, 0, 1, (end[2]-start[2])], 
                        [0, 0, 0, 1]])
    return p_matrix

def ballTransform3(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    p_matrix = project(100)
    end_loc = np.array([20*i/150, 0, 0, 0])
    end_loc = loc + end_loc
    p_matrix = p_matrix @ moveTo(loc, end_loc)
    return p_matrix
