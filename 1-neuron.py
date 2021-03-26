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

@property
    def get_W(self)
    return self.__W

@property
    def get_b(self)
    return self.__b

@property
    def get_A(self)
    return self.__A

@property
    def set_W(self,W)
    self.__W = W

@property
    def set_b(self,b)
    self.__b = b

@property
    def set_A(self,A)
    self.__A = A
   
   
     
