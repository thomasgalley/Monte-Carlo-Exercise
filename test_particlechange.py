

from particlechange import moveparticle 
from numpy.random import randint 


#test that move particle on empty array returns an empty array

def test_empty_particle():
    densities = [ [0], [0,0],[0,0,0]]
    for density in densities: assert moveparticle(density) == density
    
#test that all entries are positive after the move has been made

def test_densities_are_positive():
      # From the given example have looped over vectors of differing sizes
      
  for vector_size in randint(1, 1000, size=30): 

    # Create random density of size N (code used from given example)
    density = randint(50, size=vector_size)
    
    #Check that every component is positive
    
    for i in (0,vector_size-1): 
        assert moveparticle(density)[i] >= 0
    

    

        
    