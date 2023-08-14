import numpy as np
from hwk07_p3_soln import project, rotate, moveTo

# NOTE: you do NOT need to rewrite the `project`, `rotate`, or `moveTo` functions 
# as they are imported above

def ballTransform4(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    p_matrix = project(100)
    
    end_loc = np.array([20*i/150, 0, 0, 0])
    end_loc = loc + end_loc
    origin = np.array([0, 0, 0, 1])
    
    
    p_matrix = p_matrix @ moveTo(loc, end_loc) @ moveTo(origin, loc)
    p_matrix = p_matrix @ rotate(0, 0, -2 * np.pi * i/150)
    p_matrix = p_matrix @ moveTo(loc, origin)
    
    return p_matrix
