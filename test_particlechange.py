
from diffusion_model import energy
from particlechange import moveparticle 

#test that move particle on empty array returns an empty array

def test_empty_particle():
    densities = [ [0], [0,0],[0,0,0]]
    for density in densities: assert moveparticle(density) == density
    