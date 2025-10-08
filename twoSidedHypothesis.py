# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 13:12:59 2025

@author: riasat
"""

## Not sure about the np.abs() thing that I did
def twoSidedHypothesis(y1_bar, y2_bar, n1, n2, s1, s2, alpha, analysis):
    
    from scipy.stats import t
    import numpy as np

    #============================== CALCULATION ===============================================
    df = n1+n2-2
    
    sp_den = df 
    sp_num = (n1-1)*s1**2 + (n2-1)*s2**2
    sp= np.sqrt(sp_num/sp_den)
    
#============================== p Value Has To Be Calculated Using t_observed ===============================================#
    t_obs = np.abs(y1_bar-y2_bar)/(sp*np.sqrt(1/n1+1/n2))
#============================== range of lower and upper bound has To Be Calculated Using t_observed ============================#
    if analysis == 'two tailed':
        p_val =2*(1-t.cdf(t_obs,df))
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}')
        t_critical = t.ppf(1 - alpha/2, df)# For a two tailed it is alpha/2- not alpha in t.ppf equation
        
    elif analysis == 'left tailed':
        p_val = t.cdf(t_obs,df)
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}') 
        t_critical = t.ppf(1 - alpha, df)  # For a right/left tailed it is alpha- not alpha/2 in t.ppf equation

    elif analysis == 'right tailed':
        p_val =1-t.cdf(t_obs,df)
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}')
        t_critical = t.ppf(1 - alpha, df) # For a right/left tailed it is alpha- not alpha/2 in t.ppf equation

    upperBound = np.abs((y1_bar-y2_bar))+t_critical*(sp*np.sqrt(1/n1+1/n2))
    lowerBound = np.abs((y1_bar-y2_bar))-t_critical*(sp*np.sqrt(1/n1+1/n2))
    
    if p_val<alpha:
        hypothesis = True
        print(f'Researchers Hypothesis is {hypothesis}')
    else:
        hypothesis = False
        print(f'Researchers Hypothesis is {hypothesis}')
    print(f'Lower Bound and Upper Bound Range is: {lowerBound} to {upperBound}')
if __name__ == '__main__':
    print('Confidence Interval Calculator')
    #============================== INPUT ===============================================
    n1 = float(input('What is your sample size for SAMPLE 1? '))
    n2 = float(input('What is your sample size for SAMPLE 2? '))

    alpha = float(input('What is your significance level (In decimal)? '))
    y1_bar = float(input('What is your sample mean for SAMPLE 1? '))
    y2_bar = float(input('What is your sample mean for SAMPLE 2? '))
    s1 = float(input('What is your std. deviation for SAMPLE 1? '))
    s2 = float(input('What is your std. deviation for SAMPLE 2? '))
    analysis = input('left tailed or right tailed or two tailed? ')
    twoSidedHypothesis(y1_bar, y2_bar, n1, n2, s1, s2, alpha, analysis)
