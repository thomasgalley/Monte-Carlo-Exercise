def moveparticle(density):
    
    from diffusion_model import energy 
    from random import randint, choice
    r=randint(0,len(density)-1)
    
    
    if density[r] != 0: 
        
        density[r]=density[r]-1 #here we have taken away a particle from a random position
    
        g=choice([-1,1])
    
    # in the following loop we want to add a particle to either the left or the right of the position, in order to avoid list size errors 
    #we account for several extremum cases
    
        if len(density) != 1:
        # in the case of there being a single entry the particle has moved outside the array and we cannot add it to either side
    
        
           if r == 0:
              if g==1:
                 density[r+g]=density[r+g]+1
          
          #in the case of moving the particle from the first entry, it either moves to the right or outside the array 
    
           elif r==(len(density)-1):
              if g== -1:
                  density[r+g]=density[r+g]+1
          # similarly for the particles on the other end of the array
           else:
               density[r+g]=density[r+g]+1
        
        #do a test to check that if r is 0 and g is -1 the program runs without giving a "not in list" error same if r is last entry 
        # and g is 1
    
    return density 