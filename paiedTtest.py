# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 14:22:49 2025

@author: riasa
"""

## Need to add all other hypothesis- this just calculated righ tailed problem
def paiedTtest(y1, y2, n, alpha, analysis):
    from scipy.stats import t 
    import numpy as np
    
    y_d = np.mean(y1-y2)
    s_d = np.std(y1-y2, ddof=1) #### This ddof = 1 is very critical
    df = n-1
#============================== p Value Has To Be Calculated Using t_observed ===============================================#
#============================== range of lower and upper bound has To Be Calculated Using t_observed ============================#
    if analysis == 'right tailed':
        t_obs = y_d/(s_d/np.sqrt(n))
        p_val = 1 - t.cdf(t_obs,df)
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}')
        t_critical = t.ppf(1 - alpha, df) # For a right/left tailed it is alpha- not alpha/2 in t.ppf equation
    elif analysis == 'left tailed':
        t_obs = y_d/(s_d/np.sqrt(n))
        p_val = t.cdf(t_obs, df)
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}')
        t_critical = t.ppf(1 - alpha, df) # For a right/left tailed it is alpha- not alpha/2 in t.ppf equation
    elif analysis == 'two tailed':
        t_obs = y_d/(s_d/np.sqrt(n))
        p_val = 2 * (1 - t.cdf(np.abs(t_obs), df))
        print(f't observed value is: {t_obs: 6.4f} and p_value is {p_val}')
        t_critical = t.ppf(1 - alpha/2, df) # For a two tailed it is alpha/2- not alpha in t.ppf equation
    SE = s_d/np.sqrt(n)
    upperBound = y_d+t_critical*SE
    lowerBound = y_d-t_critical*SE
    if p_val<alpha:
        hypothesis = True
        print(f'Researchers Hypothesis is {hypothesis}')
    else:
        hypothesis = False
        print(f'Researchers Hypothesis is {hypothesis}')
    print(f'Lower Bound and Upper Bound Range is: {lowerBound} to {upperBound}')  
    
#%%
if __name__ == "__main__":
    print('Paired t-test Calculator')
    #============================== INPUT ===============================================
    import pandas as pd
    import numpy as np
    df = pd.read_csv(r"C:\Users\riasa\RiasatFolders\Academics\Fall25\STAT5615_StatForResearch\Lesson09_PairedTtestAndTwoSampleHypothesisTestingforProportions\9b_stimulus.csv")
    col_name = df.columns
    y1 = np.array(df[col_name[0]])
    y2 = np.array(df[col_name[1]])
    n = y1.shape[0]

    alpha = float(input('What is your significance level? '))
    analysis = input('left tailed or right tailed or two tailed? ')
    paiedTtest(y1, y2, n, alpha, analysis)
