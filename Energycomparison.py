from diffusion_model import energy 
from particlechange import moveparticle 
from numpy import exp, divide 
from random import random

def compare(density,T):
    
    if T<=0:
        raise TypeError ("Temperature should be strictly positive.")
        
    passdensity = moveparticle(density)
    
    #we define two new arrays both equal to the input density
    
    E1 = energy(density,coefficient=1)
    E2 = energy(passdensity,coefficient=1)
    
    # the output of moveparticle(passdensity) is passdensity which is now different from density
    
    E3 = E2-E1
    #need to make sure T is not 0 via raise error type message
    
    if E3<0:
        density=passdensity
        #in this case we want the compare function to return the density for a particle having moved
        
    else:
        P=exp(-divide(E3,T))
        P1=random()
        
        if P>P1:
            density=passdensity
            
        else:
            density=density
            #in this case we want the function compare to return the initial imput density (the particle hasn't moved)
        
    return density