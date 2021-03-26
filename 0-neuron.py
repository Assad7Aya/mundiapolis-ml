import numpy as np
Class Neuron :
def __init__(self,int):
    if not isinstance(nx,int):
        raise TypeError ('nx must be an integer')
    if nx < 1 :
        raise ValueError ('nx must be positive integer')
    self.W=np.random.normal(0,1,(1,nx))
    self.b=0
    self.A=0
