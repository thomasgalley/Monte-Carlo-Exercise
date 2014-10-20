from diffusion_model import energy 
from particlechange import moveparticle 
from numpy import exp, divide 
from random import random

def compare(density,T):
    
    if T<=0:
        raise TypeError ("Temperature should be strictly positive.")
        
    passdensity = density
    faildensity = density
    E1 = energy(density,coefficient=1)
    E2 = energy(moveparticle(passdensity),coefficient=1)
    E3 = E2-E1
    #need to make sure T is not 0 via raise error type message
    if E3<0:
        density=passdensity
        
    else:
        P=exp(-divide(E3,T))
        P1=random()
        
        if P>P1:
            density=passdensity
            
        else:
            density=faildensity
        
    return density