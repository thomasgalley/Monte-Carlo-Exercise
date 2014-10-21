# do a test for a really simple energy function to see if get right difference

from Energycomparison import compare
from diffusion_model import energy 
from numpy.random import randint 
from particlechange import moveparticle
from numpy import exp, divide
from numpy import absolute

def test_P_lies_in_correct_interval():
    
      # From the given example have looped over vectors of differing sizes
      
  for vector_size in randint(1, 1000, size=30): 

    # Create random density of size N (code used from given example)
    density = randint(50, size=vector_size) 
    passdensity = moveparticle(density)
    T=randint(1,100) 
    E1 = energy(density,coefficient=1)
    E2 = energy(passdensity,coefficient=1)
    E3 = E2-E1
    if E3 >= 0:
        P=exp(-divide(E3,T))
    assert (P>= 0 and 1>=P)
    
def test_only_one_particle_moves():
#This tests whether the code can move two particle in a single step

    for vector_size in randint(1, 1000, size=30): 

# Create random density of size N (code used from given example)
        density = randint(50, size=vector_size) 
        T=randint(1,100)
#check that for every entry the difference between the density and the density after the comparison (and potential move) is either one or zero
        
        for i in (0,vector_size-1):
            assert absolute(compare(density,T)[i]-density[i])<=1