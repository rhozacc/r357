import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Wright's Law aims to provide a framework for forecasting cost declines as a function of cumulative production
# More info available at:
# https://ark-invest.com/wrights-law/

def WrightsLaw(X, a, b):
    ''' Returns Cumulative average time (or cost) per unit
    X ... Cumulative number of units produced
    a ... Time (or cost) required to produce 1st unit
    b ... Slope of the function
    '''
    return (a*(X**b))




    
    
    
    
