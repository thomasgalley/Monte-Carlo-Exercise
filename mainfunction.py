from Energycomparison import compare

#include number of iterations and temperature as input
def Montemain(density,nbit,T):
    
    if nbit<1:
        raise TypeError ("Number of iterations should be greater or equal to 1.")
    
    while nbit>0:
        
        print compare(density,T)
        nbit-=1
        
    return 

 
    
    