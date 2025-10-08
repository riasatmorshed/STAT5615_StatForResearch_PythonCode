# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 21:43:30 2025

@author: riasa
"""

def pHypothesis(y_bar,mu,s,n,alpha,analysis):
    from scipy.stats import t
    import numpy as np
    df = n-1
    t_obs = (y_bar-mu)/(s/np.sqrt(n))
    if analysis == 'left tailed':
        p_val = t.cdf(t_obs,df)
    elif analysis == 'right tailed':
        p_val = 1-t.cdf(t_obs,df)
    elif analysis == 'two tailed':
        p_val = 2*(1-t.cdf(t_obs,df))
    
    if p_val<alpha:
        hypothesis = True
        print(f'Researchers Hypothesis is {hypothesis}')
    else:
        hypothesis = False
        print(f' Researchers Hypothesis is {hypothesis}')
    return hypothesis

if __name__ == "__main__":
    print('Hypotesis Testing')
    #============================== INPUT ===============================================
#%%
if __name__ == "__main__":
    print('Hypothesis Testing Calculator')
    #============================== INPUT ===============================================
    import pandas as pd
    df = pd.read_excel(r"C:\Users\riasa\RiasatFolders\Academics\Fall25\STAT5615_StatForResearch\Lesson07_OneSampleHypothesisTesting\7c_Pressure.xlsx")
    col_name = df.columns()
    y_bar = df[col_name[1]].mean()
    s = df[col_name[1]].std()
    mu = float(input('What is your assumed mean? '))
    n = len(df['Pressure'])
    alpha = float(input('What is your significance level? '))
    analysis = input('left tailed or right tailed or two tailed? ')
    pHypothesis(y_bar,mu,s,n,alpha,analysis)
