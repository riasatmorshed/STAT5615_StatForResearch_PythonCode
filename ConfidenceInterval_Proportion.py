# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 20:01:29 2025

@author: riasa
"""
"""
If n*pi_bar>=5 and n(1-pi_bar)>=5, you don't need to use t-distribution rather normal distribution works

Now, n = sample size
     y = in favor of your proposition
     pi_bar = y/n
     
     range = pi_bar +- CV*SE
     
     CV = z critical value-----------> is different from typical problem,because typically we use t critical value
     SE = sqrt((pi_bar*(pi_bar-1))/n)-----------> is different from typical problem, you need std deviation of sample to get SE

"""


def ConfidenceInterval_Proportional(n, yay,confdLevel):
    from scipy.stats import norm
    import numpy as np
    pi_bar = yay/n
    alpha = 1-confdLevel/100
    z_critical = norm.ppf(1-alpha/2) # two-tailed and #critical value- not cdf
    confdIntrvl1 = pi_bar + z_critical * np.sqrt((pi_bar*(1-pi_bar))/n)
    confdIntrvl2 = pi_bar - z_critical * np.sqrt((pi_bar*(1-pi_bar))/n)
    return confdIntrvl1, confdIntrvl2

if __name__ == "__main__":
    print('Confidence Interval for Proportion Calculator')
    #============================== INPUT ===============================================
    n = float(input('What is your sample size? '))
    yay = float(input('How many people say yes! '))
    confdLevel = float(input('What is your confidence level (In Percentage)? '))
    upBound, lowBound = ConfidenceInterval_Proportional(n, yay,confdLevel)
    print(f"The interval ranges from {upBound*100: 6.3f}% to {lowBound*100: 6.3f}%")
    