# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 01:02:04 2025

@author: riasa
"""
'''
Need to update with n*pi_bar>=5 condition check
'''
def pHypothesis_prop(pi_bar,pi0,n,alpha,analysis):
    from scipy.stats import norm
    import numpy as np
    SE = np.sqrt((pi0*(1-pi0))/n)
    z_obs = (pi_bar-pi0)/SE
    if analysis == 'left tailed':
        p_val = norm.cdf(z_obs)
    elif analysis == 'right tailed':
        p_val = 1-norm.cdf(z_obs)
    elif analysis == 'two tailed':
        p_val = 2*(1-norm.cdf(z_obs))
    
    if p_val<alpha:
        hypothesis = True
        print(f'Researchers Hypothesis is {hypothesis}')
    else:
        hypothesis = False
        print(f'Researchers Hypothesis is {hypothesis}')
    return hypothesis

if __name__ == "__main__":

    #============================== INPUT ===============================================
if __name__ == "__main__":
    print('Hypothesis Testing Calculator for Proportion')
    #============================== INPUT ===============================================
    
    n = float(input('What is your sample size? '))
    yay = float(input('How many people say yes! '))
    
    pi_bar = yay/n
    pi0 = float(input('What is your assumed mean? '))
    alpha = float(input('What is your significance level (in decimal point)? '))
    analysis = input('left tailed or right tailed or two tailed? ')
    pHypothesis_prop(pi_bar,pi0,n,alpha,analysis)