def eat_ghost(power_pellet_active, touching_ghost):
    return(power_pellet_active and touching_ghost)
    
def score(touching_power_pellet, touching_dot):
    return(touching_power_pellet or touching_dot)

def lose(power_pellet_active, touching_ghost):
    if (power_pellet_active == False and touching_ghost == True):
        return True
    else:
        return False    

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots:
        check = lose(power_pellet_active, touching_ghost)
        if check:
            return False
        else:
            return True
    else:
        return False


        
    
