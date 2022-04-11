#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:08:35 2022

@author: claraiglhaut
"""
import random

random.seed(128)


#%% HELPER FUNCTIONS

def determineT(min_S, S_M, S_X, S_Y):
    '''
    Sets the traceback pointer, in case of a tie the pointer is chosen uniformly 
    at random between the possibilities.

    Parameters
    ----------
    min_S : float
        Minimum value for the scoring matrix.
    S_M : float
        Score reached when matching two columns of the left and right alignment.
    S_X : float
        Score reached when matching the left alignment column with a gap column.
    S_Y : float
        Score reached when matching the right alignment column with a gap column.

    Returns
    -------
    T : int
        Returns the pointer.

    '''
    if (min_S == S_M and 
        min_S == S_X and 
        min_S == S_Y):
        T = random.sample([1,2,3],1)[0]
    elif (min_S == S_M and 
          min_S == S_X):
        T = random.sample([1,3],1)[0]
    elif (min_S == S_M and 
          min_S == S_Y):
        T = random.sample([1,2],1)[0]
    elif (min_S == S_X and 
          min_S == S_Y):
        T = random.sample([2,3],1)[0] 
    elif min_S == S_M:
        T = 1 #move diagonal
    elif min_S == S_X:
        T = 3 #move vertical
    elif min_S == S_Y:
        T = 2 #move horizontal
        
    return T

def setcurrentT(currentT_value, T_M, T_X, T_Y):
    '''
    Changes the current trace back matrix depending on the recorded value.

    Parameters
    ----------
    currentT_value : int
        The current pointer.
    T_M : np.array
        Trace back matrix for matching.
    T_X : np.array
        Trace back matrix for matching the left alignment column with a gap column.
    T_Y : np.array
        Trace back matrix for matching the right alignment column with a gap column..

    Returns
    -------
    current_T : np.array
        The new trace back matrix.

    '''
    if currentT_value == 1:
        current_T = T_M
    elif currentT_value == 2:
        current_T = T_Y
    elif currentT_value == 3:
        current_T = T_X
    return current_T

        
#%%