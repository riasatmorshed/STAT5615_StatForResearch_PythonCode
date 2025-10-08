# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 13:13:21 2025

@author: riasat
"""
''' 
    Problem: n = Sample size 
            \alpha = significance level 
            choice = your chosen distribution
            1. It calculates the critical value only, so it uses t.ppf()
            2. If you want the area under the curve, you need to use t.cdf() till the lower tail
            3. if you want only upper tail then just 1-t.cdf(f)
            4. ASSUMPTION: we assume the distribution (t or normal) to be symmetric
            5.  If you want 95% confidence interval that means you have 5% on both tails, 
            hence, \alpha 0.05 and in the coding, you need to use \alpha/2
            6. If your \alpha=5% that means 'SIGNIFICANCE LEVEL = 5%' and 'CONFIDENCE LEVEL = 95%'
            7. CV = t_critical/z_critical, SE = margin_of_error, POINT_ESTIMATE = Y_BAR and
                CONFIDENCE_INTERVAL = POINT_ESTIMATE+CV*SE
'''

def ConfidenceInterval(choice, n, confdLevel,y_bar,s):
    from scipy.stats import norm, t
    import numpy as np

    #============================== CALCULATION ===============================================
    alpha = 1-confdLevel/100
    df = n - 1

    if choice == 'normal':
        z_critical = norm.ppf(1-alpha/2) # two-tailed and #critical value- not cdf
        print(f'Z critical value- Normal Distribution is: {z_critical: .4f}')
        margin_of_error1 = y_bar+z_critical*s/np.sqrt(n)
        margin_of_error2 = y_bar-z_critical*s/np.sqrt(n)
        

    elif choice == 't':
        t_critical = t.ppf(1 - alpha/2, df)
        print(f't critical value- Students t-Distribution is: {t_critical: .4f}')
        margin_of_error1 = y_bar+t_critical*s/np.sqrt(n)
        margin_of_error2 = y_bar-t_critical*s/np.sqrt(n)
        
    return margin_of_error1, margin_of_error2

if __name__ == '__main__':
    print('Confidence Interval Calculator')
    #============================== INPUT ===============================================
    n = float(input('What is your sample size? '))
    choice = input('What distribution are you looking for- normal or t? ')
    confdLevel = float(input('What is your confidence level (In Percentage)? '))
    y_bar = float(input('What is your sample mean? '))
    s = float(input('What is your std. deviation for sample? '))
    MoE1, MoE2= ConfidenceInterval(choice, n, confdLevel,y_bar,s)
    
    print(f"The confidence interval is: {MoE2: 6.3f} to {MoE1: 6.3f}")