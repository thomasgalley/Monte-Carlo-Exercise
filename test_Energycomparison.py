# do a test for a really simple energy function to see if get right difference

from Energycomparison import compare
from diffusion_model import energy 
from numpy.random import randint 
from particlechange import moveparticle
from numpy import exp, divide

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